# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações para nossos viajantes |
| `produtos_financeiros.json` | JSON | conhecer produtos disponíveis no mercado |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para saber como poupar para viagens |
| `dados_ficticios_educacao_financeira_viagens.csv` | CSV | Simulação de planejamento financeiro para viagens com custos, poupança mensal e milhas |
| `base_perfis_viajantes_educacao_financeira.csv` | CSV | Perfis fictícios de viajantes com renda, hábitos financeiros e objetivos de viagem |
| `base_perfil_destino_ideal_viagens.csv` | CSV | Cruzamento entre perfil financeiro do viajante e destino ideal com tempo estimado para realização |
| `base_destinos_por_epoca_do_ano.csv` | CSV | Destinos do Brasil e do mundo organizados por mês, temporada, clima e perfil ideal |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
