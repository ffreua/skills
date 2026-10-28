# Interpretação estatística, avaliação crítica e relevância clínica

## Sumário

1. Princípios estatísticos
2. Desfechos binários
3. Desfechos contínuos
4. Tempo até evento
5. Eventos recorrentes
6. Incerteza
7. Multiplicidade
8. Cálculos adicionais
9. Avaliação crítica (domínios, instrumentos, regras de julgamento)
10. Relevância clínica e tradução para a prática
11. Lista de proibições
12. Linguagem calibrada

---

## 1. Princípios estatísticos

Preserve exatamente as definições estatísticas usadas pelos autores. Diferencie:
- Medida observada.
- Estimativa ajustada.
- Contraste entre grupos.
- Estimativa derivada.
- Associação.
- Predição.
- Inferência causal.
- Evidência de equivalência ou não inferioridade.

Nunca substitua uma medida por outra apenas por facilidade de visualização.

## 2. Desfechos binários

- Quando houver dados adequados, apresente riscos ou proporções por grupo.
- Calcule diferenças absolutas ou razões somente quando numeradores e denominadores representarem populações comparáveis e o mesmo horizonte temporal.
- Redução absoluta de risco: **RAR = risco no controle − risco na intervenção**, quando o evento for desfavorável e essa orientação for apropriada.
- NNT ou NNH: apenas com efeitos absolutos válidos, população e horizonte definidos. Marque como [C]. Não apresente NNT como propriedade universal de uma intervenção.
- Se o IC da diferença absoluta atravessar zero, evite um NNT pontual isolado que oculte a possibilidade de benefício e de dano (o "NNT" teria um intervalo que passa pelo infinito — NNTB a NNTH).
- Diferencie razão de riscos, odds ratio e hazard ratio.

## 3. Desfechos contínuos

Preserve: unidade, escala, sentido clínico do aumento ou redução, média ou mediana, DP/EP/IC, diferença no valor final ou diferença na mudança desde o basal, ajustes estatísticos.

- NÃO transforme medianas em médias.
- NÃO trate diferenças brutas como estimativas ajustadas.
- NÃO confunda diferença estatística com diferença clinicamente relevante.
- Para escalas padronizadas (DMP/SMD), explique o significado e as limitações da padronização.

## 4. Tempo até evento

Diferencie: probabilidade acumulada de evento, sobrevida, hazard instantâneo, hazard ratio, mediana de sobrevida, diferença de sobrevida em tempo específico, tempo médio de sobrevida restrito (RMST), incidência cumulativa na presença de riscos competitivos.

- NÃO interprete HR como redução percentual direta no número de pessoas com eventos.
- NÃO derive riscos absolutos diretamente de HR sem informações e pressupostos suficientes.
- Respeite os métodos usados para riscos competitivos (Fine-Gray vs causa-específico).
- Considere violações da proporcionalidade de hazards quando o estudo as examinar.
- NÃO reconstrua curvas de Kaplan-Meier a partir de estimativas agregadas.

## 5. Eventos recorrentes

Diferencie: participantes com ≥1 evento, número total de eventos, eventos por pessoa-tempo, taxas e razões de taxas.

- NÃO conte eventos recorrentes como pessoas distintas.
- NÃO interprete razão de taxas como razão de riscos.

## 6. Incerteza

Para cada estimativa, identifique: estimativa pontual; IC e nível; EP ou dispersão quando relevante; referência de ausência de efeito; direção de benefício ou dano; limiares de relevância clínica publicados.

- Intervalos de credibilidade bayesianos devem ser identificados como tais, não como ICs frequentistas.
- NÃO declare que há 95% de probabilidade de o parâmetro verdadeiro estar dentro de um IC frequentista de 95%. Formulação aceitável: "valores compatíveis com os dados, sob o modelo" ou "o procedimento captura o valor verdadeiro em 95% das repetições".
- NÃO interprete p > 0,05 como ausência de efeito.
- NÃO interprete significância estatística como importância clínica.
- Diferencie estimativa imprecisa (IC largo, compatível com efeitos importantes em ambas as direções) de estimativa pequena e precisa (IC estreito em torno de efeito trivial).

## 7. Multiplicidade

Identifique: desfechos primários e secundários, comparações múltiplas, análises intermediárias, subgrupos, testes de interação, ajustes de multiplicidade, análises exploratórias ou post hoc.

- Diferença de significância entre subgrupos NÃO é evidência suficiente de interação — procure o teste de interação.
- Preserve a distinção entre análise confirmatória e exploratória.

## 8. Cálculos adicionais

Permita cálculos apenas quando:
1. Os dados de entrada estiverem disponíveis.
2. As populações forem compatíveis.
3. O horizonte temporal estiver definido.
4. A fórmula for adequada ao delineamento.
5. As pressuposições forem defensáveis e explícitas.
6. O cálculo puder ser auditado.

Apresente, quando relevante: fórmula, valores usados, resultado, unidade, origem dos dados, limitações. Na interface, isso vai para a camada avançada ou para o painel Fontes, com a marca [C].

Se qualquer requisito essencial estiver ausente, NÃO execute o cálculo. NÃO reconstrua erros-padrão, intervalos ou estatísticas complexas mediante aproximações não justificadas. Preserve a precisão numérica pertinente; não arredonde de forma que altere a conclusão. Prefira repetir os números como publicados (mesmo número de casas decimais).

Quando fizer cálculos, faça-os de fato (ex.: com código), não de cabeça, e confira.

---

## 9. Avaliação crítica

**Objetivo:** identificar limitações capazes de alterar a interpretação, de forma proporcional às informações documentadas, sem diagnósticos de viés sem fundamento.

**Domínios** (conforme o delineamento): seleção de participantes; confundimento; mensuração de exposição e desfechos; temporalidade; randomização e alocação; mascaramento; desvios do tratamento; dados ausentes; censura e perdas; seleção de análises relatadas; multiplicidade; adequação do modelo estatístico; precisão; comparabilidade; representatividade; viés de publicação e relato seletivo (quando pertinente); financiamento e conflitos de interesse como possíveis fontes de preocupação, sem presumir sua influência.

**Instrumentos — use só dentro do escopo:**
- RoB 2: ensaios randomizados.
- ROBINS-I: estudos não randomizados de intervenções.
- ROBINS-E: estudos observacionais de efeitos de exposições.
- QUADAS-3: acurácia diagnóstica.
- AMSTAR 2: revisões sistemáticas de intervenções.
- GRADE: certeza de um corpo de evidências, por desfecho.
- Ferramentas específicas para prognóstico/modelos preditivos (ex.: PROBAST), quando adequadas.

CONSORT, STROBE, STARD e PRISMA orientam o relato e NÃO substituem instrumentos de risco de viés. Não use instrumento fora do escopo. Não emita classificações formais sem informação suficiente e sem aplicar os critérios da ferramenta. Classificações publicadas pelos autores devem ser identificadas como avaliações dos autores. Uma apreciação independente sua deve ser identificada como "interpretação crítica preliminar", com sua base documental.

**Regras de julgamento.** Diferencie:
- Informação não relatada.
- Método inadequado documentado.
- Risco potencial de viés.
- Viés demonstrado.
- Incerteza sobre a validade.

- NÃO presuma que ausência de informação comprove viés.
- NÃO confunda risco de viés com imprecisão.
- NÃO considere tamanho amostral elevado garantia de validade interna.
- NÃO use rótulos genéricos ("estudo de alta qualidade") sem justificativa metodológica.

---

## 10. Relevância clínica e tradução para a prática

**Dimensões:**
1. Magnitude do resultado.
2. Precisão da estimativa.
3. Relevância clínica do desfecho.
4. Desfechos centrados no paciente vs substitutos.
5. Benefícios e danos.
6. Validade interna.
7. Aplicabilidade à população clínica.
8. Contexto assistencial e recursos necessários.
9. Consistência com o objetivo efetivamente estudado.
10. Limitações para decisões individuais.

**Limiar clínico.** Se os autores definirem diferença mínima clinicamente importante (DMCI/MCID) ou outro limiar, apresente-o, diferenciando limiares validados, convencionais e escolhidos pelos pesquisadores. NÃO invente limiares. NÃO transforme resultado significativo em recomendação automática.

**Transferibilidade.** Discuta aplicabilidade considerando idade e perfil clínico, estágio e gravidade, critérios diagnósticos, comorbidades, intervenções concomitantes, disponibilidade de recursos, contexto de atendimento, horizonte temporal e diferenças entre a amostra e a população assistencial. Destaque apenas diferenças verificáveis ou limitações explicitamente condicionais. NÃO presuma características da população clínica do leitor.

**"O que os resultados sugerem para a prática clínica?"** Responda de modo proporcional à evidência. Conclusões aceitáveis:
- O resultado apoia determinada interpretação.
- O achado é promissor, porém insuficiente para mudar condutas.
- Há associação, mas a direção causal permanece incerta.
- O teste apresenta desempenho diagnóstico em contexto específico.
- A evidência sintetizada favorece determinada direção de efeito, com limitações.
- Os dados são insuficientes para uma conclusão robusta.

NÃO extrapole para recomendação terapêutica individual. NÃO proponha substituir diretrizes com base exclusivamente no artigo. NÃO alegue que um estudo isolado estabelece consenso. NÃO transforme interpretação metodológica em orientação clínica personalizada.

---

## 11. Lista de proibições

É PROIBIDO:
1. Selecionar apenas resultados favoráveis à hipótese.
2. Omitir resultados primários desfavoráveis.
3. Priorizar análises post hoc sobre análises principais.
4. Confundir associação com causalidade.
5. Confundir significância estatística com importância clínica.
6. Confundir ausência de significância com ausência de efeito.
7. Confundir odds ratio com risco relativo.
8. Confundir hazard ratio com redução de risco acumulado.
9. Calcular risco populacional diretamente de amostragem caso-controle inadequada.
10. Confundir prevalência com incidência.
11. Confundir sensibilidade com valor preditivo positivo.
12. Tratar AUC como demonstração de utilidade clínica.
13. Tratar I² como avaliação completa da heterogeneidade.
14. Afirmar causalidade com base apenas em ajuste estatístico.
15. Atribuir certeza GRADE formal sem avaliação suficiente.
16. Converter desfechos substitutos automaticamente em benefícios clínicos.
17. Tratar subgrupos sem testes apropriados como diferenças confirmadas.
18. Interpretar médias populacionais como benefício individual garantido.
19. Ocultar limitações metodológicas importantes.
20. Extrapolar para populações não estudadas sem ressalvas.
21. Inventar dados, análises, referências ou métodos.
22. Apresentar julgamentos metodológicos inferidos como fatos documentados.
23. Omitir danos relevantes enquanto destaca benefícios.
24. Confundir validade do relato com validade interna.
25. Transformar associação prognóstica em alvo terapêutico comprovado.

## 12. Linguagem calibrada

Verbos adequados: observou, identificou, estimou, encontrou associação, foi compatível com, sugeriu; "demonstrou" apenas quando metodologicamente defensável.

Evite: comprovou definitivamente, eliminou o risco, garante benefício, não existe efeito, é clinicamente superior (sem sustentação adequada).

A conclusão deve ser tão precisa quanto os dados permitirem e tão cautelosa quanto as limitações exigirem.
