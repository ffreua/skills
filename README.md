# Skills — Fernando Freua

Coleção de skills para agentes de IA (Claude Code, Cursor, Codex, OpenCode e outros), com foco em medicina baseada em evidências, neurologia e comunicação científica em português brasileiro.

## Skills disponíveis

| Skill | O que faz |
|---|---|
| [`analise-de-artigos-cientificos`](skills/analise-de-artigos-cientificos) | Interpretação crítica e interativa de artigos científicos da saúde: identifica o delineamento, extrai resultados com rastreabilidade, avalia magnitude, incerteza, vieses e relevância clínica, e entrega uma interface interativa em 4 etapas. |

## Instalação

Requer Node.js 22.20 ou superior.

Ver as skills da coleção:

```bash
npx skills add ffreua/skills --list
```

Instalar uma skill específica:

```bash
npx skills add ffreua/skills --skill analise-de-artigos-cientificos
```

Instalar direto no Claude Code, disponível em todos os projetos:

```bash
npx skills add ffreua/skills --skill analise-de-artigos-cientificos -a claude-code -g -y
```

Sem `--skill`, o instalador mostra a lista e pergunta quais instalar.

Atualizar as skills já instaladas:

```bash
npx skills update
```

### Claude.ai (web e app)

O `npx skills` instala em agentes de linha de comando e IDEs. Para usar no Claude.ai, baixe o arquivo `.skill` da página de [Releases](../../releases) e envie em **Configurações → Capacidades → Skills**.

## analise-de-artigos-cientificos

A partir de um artigo (PDF, DOI ou link), a skill:

- identifica o **delineamento efetivo** do estudo (ECR, coorte, caso-controle, transversal, acurácia diagnóstica, revisão sistemática, metanálise, prognóstico, descritivo…);
- extrai os resultados com **rastreabilidade** (cada número ligado a página, tabela ou figura, e classificado como Publicado, Calculado, Interpretado ou Não disponível);
- avalia **magnitude, incerteza, vieses e relevância clínica** com as regras específicas de cada desenho;
- entrega uma **interface interativa em 4 etapas** (estrutura do estudo → resultados observados → efeito e incerteza → interpretação clínica), com painel de fontes e gráficos (IC, forest plot, matriz 2 × 2, frequências naturais).

Uso: basta pedir naturalmente, anexando o artigo — "analisa criticamente esse artigo", "esse estudo muda a prática?", "prepara a leitura crítica desse trial para o journal club".

A skill apoia a leitura crítica da literatura e não substitui o julgamento clínico, diretrizes ou avaliações formais de risco de viés e certeza da evidência.

## Estrutura do repositório

```
skills/
└── analise-de-artigos-cientificos/
    ├── SKILL.md
    ├── references/
    ├── assets/
    └── scripts/
```

Para adicionar uma skill nova, crie uma pasta em `skills/<nome-da-skill>/` com um `SKILL.md`.

## Licença

MIT © Fernando Freua
