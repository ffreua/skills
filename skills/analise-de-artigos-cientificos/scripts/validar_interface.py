#!/usr/bin/env python3
"""Validação estática de uma interface gerada a partir de assets/interface-template.html.

Uso: python3 scripts/validar_interface.py caminho/para/interface.html

Verifica: placeholders ⟦ ⟧ restantes; JSON de fontes válido e com campos mínimos;
IDs de fonte duplicados; referências (data-fonte) para IDs inexistentes; JSON de cada
gráfico; existência das 4 etapas; seletores com data-mostrar correspondentes.
Não substitui a revisão metodológica — apenas pega erros mecânicos.
"""
import json
import re
import sys
from html.parser import HTMLParser


class Coletor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.passos, self.refs, self.graficos, self.grupos, self.mostrar = [], [], [], {}, []
        self.fontes_json = None
        self._script = None  # ("fontes"|"grafico", tipo)
        self._buf = []
        self._grafico_tipo = None
        self._grupo_atual = None
        self._pilha_grupo = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "data-passo" in a:
            self.passos.append(a["data-passo"])
        if "data-fonte" in a:
            self.refs.extend(i.strip() for i in a["data-fonte"].split(",") if i.strip())
        if tag == "div" and "lit-grafico" in a.get("class", "") and "data-tipo" in a:
            self._grafico_tipo = a["data-tipo"]
        if "data-grupo" in a and "lit-seletor" in a.get("class", ""):
            self._grupo_atual = a["data-grupo"]
            self.grupos.setdefault(self._grupo_atual, set())
        if tag == "button" and "data-valor" in a and self._grupo_atual:
            self.grupos[self._grupo_atual].add(a["data-valor"])
        if "data-mostrar" in a:
            self.mostrar.append(a["data-mostrar"])
        if tag == "script":
            if "data-lit-fontes-dados" in a:
                self._script, self._buf = ("fontes", None), []
            elif a.get("type") == "application/json" and self._grafico_tipo:
                self._script, self._buf = ("grafico", self._grafico_tipo), []
                self._grafico_tipo = None

    def handle_endtag(self, tag):
        if tag == "script" and self._script:
            texto = "".join(self._buf)
            if self._script[0] == "fontes":
                self.fontes_json = texto
            else:
                self.graficos.append((self._script[1], texto))
            self._script = None
        if tag == "div" and self._grupo_atual:
            # seletores não têm divs internas; o primeiro </div> fecha o seletor
            self._grupo_atual = None

    def handle_data(self, data):
        if self._script:
            self._buf.append(data)


def main(caminho):
    html = open(caminho, encoding="utf-8").read()
    erros, avisos = [], []

    sem_comentarios = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    restantes = re.findall(r"⟦[^⟧]*⟧", sem_comentarios)
    if restantes:
        erros.append(f"{len(restantes)} placeholder(s) ⟦…⟧ restante(s), ex.: {restantes[:3]}")

    c = Coletor()
    c.feed(html)

    if sorted(c.passos) != ["1", "2", "3", "4"]:
        erros.append(f"etapas encontradas: {c.passos} (esperado exatamente 1, 2, 3, 4)")

    ids = []
    try:
        fontes = json.loads(c.fontes_json or "")
        for f in fontes:
            ids.append(f.get("id"))
            if f.get("origem") not in {"P", "C", "I", "ND"}:
                erros.append(f"fonte {f.get('id')}: origem inválida {f.get('origem')!r}")
            if not f.get("local") and f.get("origem") in {"P", "C"}:
                avisos.append(f"fonte {f.get('id')}: sem 'local' (página/tabela/figura)")
            if f.get("origem") == "C" and not f.get("nota"):
                avisos.append(f"fonte {f.get('id')}: cálculo [C] sem fórmula/valores em 'nota'")
    except Exception as e:  # noqa: BLE001
        erros.append(f"JSON de fontes inválido: {e}")
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        erros.append(f"IDs de fonte duplicados: {sorted(dup)}")

    for gtipo, texto in c.graficos:
        try:
            cfg = json.loads(texto)
            if cfg.get("fonte"):
                c.refs.extend(i.strip() for i in str(cfg["fonte"]).split(","))
            else:
                avisos.append(f"gráfico '{gtipo}' ({cfg.get('titulo', 'sem título')}) sem campo 'fonte'")
        except Exception as e:  # noqa: BLE001
            erros.append(f"JSON inválido em gráfico '{gtipo}': {e}")

    faltando = sorted(set(c.refs) - set(ids))
    if faltando:
        erros.append(f"referências para fontes inexistentes: {faltando}")
    nao_citadas = sorted(set(ids) - set(c.refs))
    if nao_citadas:
        avisos.append(f"fontes nunca referenciadas na interface: {nao_citadas}")

    for cond in c.mostrar:
        for parte in filter(None, (p.strip() for p in cond.split(";"))):
            if ":" not in parte:
                erros.append(f"data-mostrar malformado: {cond!r}")
                continue
            g, vs = parte.split(":", 1)
            g = g.strip()
            if g not in c.grupos:
                erros.append(f"data-mostrar usa grupo inexistente {g!r}")
                continue
            for v in (x.strip() for x in vs.split("|")):
                if v not in c.grupos[g]:
                    erros.append(f"data-mostrar usa valor {v!r} inexistente no grupo {g!r}")

    for e in erros:
        print("ERRO  ", e)
    for a in avisos:
        print("AVISO ", a)
    print("OK — nenhum erro mecânico encontrado." if not erros else f"{len(erros)} erro(s).")
    return 1 if erros else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
