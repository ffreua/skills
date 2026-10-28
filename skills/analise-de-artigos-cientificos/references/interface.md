# Interface interativa: especificação, direção visual e uso do template

## Sumário

1. Estrutura global (regiões A, B, C)
2. Conteúdo de cada uma das 4 etapas
3. Exploração adicional (controles secundários)
4. Direção visual e regras gráficas
5. Acessibilidade
6. Rastreabilidade (painel Fontes)
7. Como usar o template — catálogo de componentes
8. Modos de entrega

---

## 1. Estrutura global

Mantenha **exatamente quatro etapas principais**, qualquer que seja o delineamento. Adapte títulos secundários, métricas e visualizações ao estudo.

No topo, fora do contêiner principal:
- Título: `[Autor principal e ano] | Da evidência à interpretação`
- Subtítulo: `Delineamento identificado · Resultado central · Horizonte temporal ou contexto relevante`

Um único contêiner principal com:
- **Região A — mapa persistente:** rótulo "MAPA DA EVIDÊNCIA · SEMPRE VISÍVEL", indicador "n de 4", cartão com a pergunta clínica central, legenda (Delineamento · População ou estudos incluídos · Objetivo principal) e quatro segmentos navegáveis: 1. Estrutura do estudo; 2. Resultados observados; 3. Efeito e incerteza; 4. Interpretação clínica. Permanece visível durante toda a navegação.
- **Região B — conteúdo progressivo:** uma etapa por vez.
- **Região C — controles:** "← Voltar" (desabilitado na etapa 1), "Fontes" (abre painel independente), "Avançar →" (vira "Recomeçar" na etapa 4). Navegação direta pelos segmentos. Estado dos controles preservado durante a navegação.

O template já implementa tudo isso.

## 2. Conteúdo das etapas

### Etapa 1 — O que foi investigado?
- Pergunta clínica em linguagem simples.
- Delineamento identificado e, brevemente, como os dados foram obtidos.
- A estrutura efetivamente presente: intervenção e comparador; expostos e não expostos; casos e controles; população transversal; teste índice e padrão de referência; estudos incluídos na revisão; coorte prognóstica; ou outra.
- Tamanhos amostrais e populações de análise (o fluxo elegíveis → incluídos → analisados é muito útil aqui).
- NÃO imponha artificialmente dois grupos a estudos sem comparação.
- Camada avançada: randomização/sigilo/mascaramento, critérios de elegibilidade, definições operacionais, registro, financiamento e conflitos de interesse.
- Pergunta didática: *"Como o desenho deste estudo influencia aquilo que podemos concluir?"*

### Etapa 2 — O que os pesquisadores observaram?
Resultados primários antes das medidas comparativas, quando essa decomposição for válida. Adapte:
- **Ensaios:** valores observados por grupo.
- **Coortes:** eventos, seguimento e medidas de frequência.
- **Caso-controle:** distribuição de casos, controles e exposições, com denominadores amostrais (sem riscos absolutos!).
- **Transversais:** prevalências e distribuições.
- **Diagnósticos:** matriz 2 × 2 e medidas de acurácia.
- **Revisões:** estudos e participantes incluídos, características principais e resultados por estudo.
- **Metanálises:** resultados individuais e síntese, preservando sua relação.
- **Prognósticos:** eventos, distribuições e métricas de desempenho.
- **Descritivos:** frequências, observações e evolução clínica.

Inclua horizonte temporal e unidades. Identifique dados diretamente observados e estimativas modeladas.
Pergunta didática: *"O que os dados realmente mostram antes de interpretarmos seu significado?"*

### Etapa 3 — Qual é a magnitude do resultado e sua incerteza?
Medida principal apropriada ao estudo (diferença absoluta, RR, OR, HR, razão de prevalências, razão de taxas, diferença média, sensibilidade e especificidade, RV, AUC, estimativa combinada, heterogeneidade, estimativa descritiva). Inclua: estimativa pontual, unidade ou escala, IC ou incerteza disponível, direção do resultado, referência de ausência de efeito, limiares clínicos se definidos, tipo de análise, origem da estimativa.

- Metanálise: heterogeneidade e intervalo de predição, se publicados.
- Diagnóstico: o significado prático de sensibilidade, especificidade e resultados falsos (frequências naturais ajudam; se usar prevalência ilustrativa, rotule-a e marque como [C]).
- Estudo sem comparação: NÃO invente medida de efeito entre grupos.

Pergunta didática: *"Qual é o tamanho do resultado e quais valores permanecem compatíveis com sua incerteza?"*

### Etapa 4 — O que podemos concluir para a prática clínica?
Quatro blocos curtos:
- **A. Achado principal** — magnitude e direção.
- **B. Grau de incerteza** — precisão e limitações da estimativa.
- **C. Validade e limitações** — questões metodológicas capazes de modificar a interpretação.
- **D. Relevância clínica** — o que o estudo acrescenta e até onde permite orientar decisões.

Cartão final **"Exemplo de conclusão sustentada pelos dados"**: duas ou três frases com população, exposição/intervenção/teste/fenômeno, comparação (se existir), desfecho, horizonte (se pertinente), estimativa principal e incerteza, limitação central à inferência e implicação clínica proporcional. Nunca ultrapasse as inferências permitidas pelo delineamento.

## 3. Exploração adicional

Quando houver informação suficiente, ofereça controles secundários discretos para: seleção de desfecho, de comparação ou de horizonte temporal; ajustado vs não ajustado; principal vs sensibilidade; absoluto vs relativo (quando ambos válidos); benefícios vs eventos adversos; detalhes metodológicos; glossário contextual.

- Cada seleção deve atualizar simultaneamente todos os elementos dependentes (o template faz isso pelo grupo do seletor, em todas as etapas).
- NÃO misture estimativas de análises incompatíveis.
- NÃO crie controles decorativos ou sem função. Se só existe uma análise, não crie seletor.

## 4. Direção visual e regras gráficas

**Identidade:** estética científica contemporânea, sóbria, editorial, minimalista. Fundo off-white; cor principal #35B4A2; cor de contraste #D97757; texto escuro de alto contraste; bordas discretas; cantos levemente arredondados; tipografia limpa e hierarquizada; números importantes em destaque. Evite gradientes decorativos, ícones irrelevantes e animações desnecessárias. Priorize legibilidade e densidade informacional adequada ao uso profissional.

Observação de contraste: #35B4A2 sobre branco tem contraste baixo para texto pequeno; o template usa #35B4A2 em preenchimentos e bordas e uma variante escura (#1F7A6D) para texto e botões. O template também tem modo escuro automático.

**Visualizações condicionais** (use a mais simples que preserve a informação): cartões comparativos, barras proporcionais, dot plots, estimativas com IC, forest plots, matrizes 2 × 2, diagramas de fluxo, curvas de sobrevida (só com dados publicados suficientes), ROC e calibração (só quando disponíveis), gráficos de prevalência, frequências naturais, quadros de certeza da evidência (quando fundamentados). Se o estudo publica apenas estimativas agregadas, NÃO reconstrua curvas nem dados individuais hipotéticos.

**Regras gráficas:** escala matematicamente coerente; unidade informada; grupos identificados; direção preservada; incerteza mostrada quando disponível; fonte informada; limites de eixo apropriados; distinguir observado, ajustado e calculado.
- Medidas de razão: escala log, com a referência de nulidade (1) marcada.
- Medidas de diferença: zero como referência.
- NÃO trunque eixos de forma a exagerar visualmente.
- NÃO coloque medidas incompatíveis na mesma escala sem distinção.
- NÃO use cores para insinuar benefício sem considerar a direção clínica do desfecho (o template usa cores neutras para as estimativas; os rótulos de direção são texto definido por você).
- Não crie números hipotéticos para preencher figuras.

## 5. Acessibilidade

Responsividade; legibilidade em telas pequenas (os gráficos do template mudam para layout empilhado em telas estreitas); contraste adequado; identificação textual além das cores (formas distintas e tabelas de dados automáticas); legendas compreensíveis; controles com estados visíveis; navegação intuitiva; nada dependente apenas de animação.

## 6. Rastreabilidade

**Regra absoluta:** todo valor numérico apresentado deve ter origem documental verificável ou ser identificado como cálculo derivado.

Para cada resultado relevante, mantenha no registro de fontes: nome da variável/desfecho, valor, unidade, população, grupo/comparação, horizonte, tipo de análise, modelo, origem P/C, página, tabela/figura/seção e ressalvas. Para [C], registre fórmula e valores usados.

**Inconsistências** entre texto, tabela e figura: identifique, não escolha silenciosamente, não corrija por intuição, declare a consequência interpretativa (use `.lit-alerta`) e limite a conclusão se necessário.

**Dados ausentes:** "não relatado" + consequência prática da ausência; nunca preencha com especulação. Ausência de relato não é prova de ausência do fenômeno.

---

## 7. Como usar o template

Arquivo: `assets/interface-template.html`. Copie-o, substitua todos os `⟦…⟧`, preencha as quatro seções `[data-passo]` e o JSON de fontes. Não edite o motor (bloco `<script>` final), exceto para corrigir bugs. Antes de entregar, procure `⟦` no arquivo: não pode sobrar nenhum.

### Etiquetas de proveniência
```html
<span class="lit-tag P">P</span>  <span class="lit-tag C">C</span>
<span class="lit-tag I">I</span>  <span class="lit-tag ND">ND</span>
```

### Referência a uma fonte (abre o painel e destaca o item)
```html
<button type="button" class="lit-ref" data-fonte="F3"></button>
<button type="button" class="lit-ref" data-fonte="F3,F4"></button>
```
O texto do botão é preenchido automaticamente. IDs inexistentes ficam marcados em vermelho e geram aviso no console — corrija antes de entregar.

### Registro de fontes (JSON no final do template)
```json
{"id":"F3","rotulo":"Desfecho primário — HR ajustado","valor":"0,74 (IC 95% 0,61 a 0,90)","origem":"P",
 "local":"Tabela 2, p. 6","populacao":"ITT, n = 1.204","analise":"Cox estratificado por centro","nota":""}
```
Para cálculos: `"origem":"C"` e `"nota":"RAR = 12,0% − 8,5% = 3,5 p.p. (dados da Tabela 2, mesma população e horizonte de 24 meses)"`.

### Cartões e números em destaque
```html
<div class="lit-grade">
  <div class="lit-cartao realce"><h4>Intervenção</h4>
    <div class="lit-numero">8,5% <small>(51/600)</small></div>
    <p class="lit-nota">Evento em 24 meses <span class="lit-tag P">P</span> <button type="button" class="lit-ref" data-fonte="F3"></button></p></div>
  <div class="lit-cartao realce-contraste"><h4>Controle</h4> … </div>
</div>
```

### Fluxo de participantes
```html
<div class="lit-fluxo">
  <div>Avaliados<b>2.310</b></div><span>→</span>
  <div>Randomizados<b>1.210</b></div><span>→</span>
  <div>Analisados (ITT)<b>1.204</b></div>
</div>
```

### Camada avançada, pergunta didática, alerta, tabela
```html
<details class="lit-avancado"><summary>Randomização e mascaramento</summary><div>…</div></details>
<aside class="lit-didatica"><strong>Pergunta didática</strong>…</aside>
<div class="lit-alerta">O texto (p. 5) informa 312 eventos; a Tabela 2 informa 318. …</div>
<div class="lit-tabela-wrap"><table class="lit-tabela">…</table></div>
```

### Seletores (controles secundários)
```html
<div class="lit-seletor" data-grupo="analise">
  <span class="lit-seletor-rotulo">Análise:</span>
  <button data-valor="ajustada" data-padrao>Ajustada</button>
  <button data-valor="bruta">Não ajustada</button>
</div>
<div data-mostrar="analise:ajustada">…conteúdo da análise ajustada…</div>
<div data-mostrar="analise:bruta">…conteúdo da análise não ajustada…</div>
```
- O mesmo `data-grupo` pode aparecer em várias etapas; todos ficam sincronizados.
- `data-mostrar` aceita alternativas (`desfecho:obito|internacao`) e condições combinadas (`desfecho:obito; analise:ajustada`).
- Cada combinação exibida precisa ter conteúdo real. Se não existir dado para uma combinação, mostre um bloco explicando que não foi relatado — nunca deixe vazio nem misture análises.

### Gráficos
Cada gráfico é um `div.lit-grafico` com `data-tipo` e um `<script type="application/json">` com a configuração. Números podem ser strings (`"0.80"`) para preservar as casas decimais publicadas — use ponto decimal no JSON; a exibição converte para vírgula. Se a configuração tiver erro, aparece uma caixa vermelha "Gráfico não renderizado" — a entrega final não pode ter nenhuma.

**`ic` — estimativas com intervalo, forest plot, estimativa combinada**
```html
<div class="lit-grafico" data-tipo="ic"><script type="application/json">
{"titulo":"Desfecho primário","escala":"log","referencia":1,"unidade":"Hazard ratio",
 "rotuloEsquerda":"menos eventos com intervenção","rotuloDireita":"mais eventos com intervenção",
 "rotuloValores":"HR (IC 95%)","fonte":"F3",
 "limiares":[{"valor":"0.80","rotulo":"margem de NI"}],
 "itens":[
   {"rotulo":"Análise ajustada","est":"0.74","li":"0.61","ls":"0.90"},
   {"rotulo":"Não ajustada","est":"0.78","li":"0.64","ls":"0.95"}
 ]}
</script></div>
```
Campos por item: `rotulo`, `est`, `li`, `ls`, `origem` (`P` padrão; outro valor aparece como sufixo), `peso` (em %, para forest plot), `tipo:"combinado"` (losango), `ip:[li,ls]` (intervalo de predição, linha tracejada), `destaque:true`, `texto` (sobrescreve o texto do valor). Campos gerais: `escala` (`log` para razões, `linear` para diferenças), `referencia` (1 ou 0; omita para estimativas descritivas sem nulidade), `rotuloReferencia`, `dominio:[min,max]`, `limiares`, `rotuloEsquerda`/`rotuloDireita` (direção, sempre conforme o sentido clínico do desfecho), `larguraRotulo`, `fonte`, `notaFonte`. Mantenha rótulos curtos (até ~30 caracteres); o texto completo aparece na tabela.

**`barras` — proporções/valores ≥ 0 por grupo**
```html
<div class="lit-grafico" data-tipo="barras"><script type="application/json">
{"titulo":"Evento em 24 meses","sufixo":"%","unidade":"% de participantes","max":100,"fonte":"F3",
 "itens":[{"rotulo":"Intervenção","valor":"8.5","n":"51/600"},
          {"rotulo":"Controle","valor":"12.0","n":"72/600","cor":"contraste"}]}
</script></div>
```
`li`/`ls` opcionais por item; `cor` em `primaria` | `contraste` | `neutro` (apenas identificação de grupo, não juízo). Para eixos não truncados em proporções, use `"max":100` quando a escala completa for informativa; se os valores forem muito pequenos, um máximo menor é aceitável desde que o eixo comece em zero (o gráfico sempre começa em zero).

**`matriz2x2` — acurácia diagnóstica**
```html
<div class="lit-grafico" data-tipo="matriz2x2"><script type="application/json">
{"titulo":"Teste índice vs padrão de referência (n = 412)","vp":88,"fp":21,"fn":12,"vn":291,
 "rotuloTeste":"Biomarcador ≥ limiar","rotuloReferencia":"Diagnóstico clínico final","fonte":"F5"}
</script></div>
```
Células ausentes: use `null` (aparece "ND"). Totais marginais são marcados automaticamente como [C].

**`frequencias` — frequências naturais**
```html
<div class="lit-grafico" data-tipo="frequencias"><script type="application/json">
{"titulo":"Em 100 pacientes testados, com prevalência ilustrativa de 20%","total":100,
 "grupos":[{"rotulo":"verdadeiros positivos","n":18},{"rotulo":"falsos positivos","n":8}],
 "rotuloRestante":"testes negativos","nota":"Cálculo [C] com sensibilidade e especificidade publicadas e prevalência ilustrativa.","fonte":"F6"}
</script></div>
```
Cada grupo recebe cor e forma distintas (círculo, quadrado, losango). Use apenas com números publicados ou cálculos [C] explícitos.

Outros visuais (fluxogramas complexos, curvas publicadas com pontos suficientes, quadros GRADE) podem ser feitos com HTML/SVG próprios, seguindo as mesmas regras gráficas e variáveis de cor do template (`var(--primaria)`, `var(--contraste)`, `var(--tinta)` etc.).

---

## 8. Modos de entrega

- **Visual inline na conversa** (preferido quando há ferramenta de widget HTML): envie o conteúdo do template como fragmento (ele não tem `<html>`/`<body>` e é escopado em `#lit-app`). Se a ferramenta exigir leitura prévia de instruções próprias, siga-as, mas preserve as cores e a estrutura da interface.
- **Arquivo HTML/artefato:** envolva o fragmento em
  `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>[Autor Ano] — Da evidência à interpretação</title></head><body style="margin:0;background:#FAF9F6">` … `</body></html>`
  e entregue conforme o ambiente (artefato publicado, arquivo apresentado etc.).
- Antes de entregar, se houver ambiente de execução, valide: nenhum `⟦` restante; nenhuma caixa "Gráfico não renderizado"; nenhuma referência `.lit-ref.quebrada`; navegação 1→4 funcionando.
