# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |
| `dados_ficticios_educacao_financeira_viagens.csv` | CSV | Simulação de planejamento financeiro para viagens com custos, poupança mensal e milhas |
| `base_perfis_viajantes_educacao_financeira.csv` | CSV | Perfis fictícios de viajantes com renda, hábitos financeiros e objetivos de viagem |
| `base_perfil_destino_ideal_viagens.csv` | CSV | Cruzamento entre perfil financeiro do viajante e destino ideal com tempo estimado para realização |
| `base_destinos_por_epoca_do_ano.csv` | CSV | Destinos do Brasil e do mundo organizados por mês, temporada, clima e perfil ideal |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Dados adaptados para pessoas que desejam poupar para viajar

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

'''
import pandas as pd
import json

#CSV
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')
planejamento_viagens = pd.read_csv('data/dados_ficticios_educacao_financeira_viagens.csv')
perfis_viajantes = pd.read_csv('data/base_perfis_viajantes_educacao_financeira.csv')
perfil_destino = pd.read_csv('data/base_perfil_destino_ideal_viagens.csv')
destinos_epoca = pd.read_csv('data/base_destinos_por_epoca_do_ano.csv')

#Json
with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)

  with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)
'''

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados podem ser injetados no prompt para garantir que o agente tenha o melhor contexto. Para informações mais robustas o ideal é que as informações sejam carregadas de formas dinâmica.

'''text
`historico_atendimento.csv` :  Contextualizar interações anteriores 
`perfil_investidor.json` : Personalizar recomendações 
`produtos_financeiros.json` : Sugerir produtos adequados ao perfil
`transacoes.csv` : Analisar padrão de gastos do cliente 
`dados_ficticios_educacao_financeira_viagens.csv` : Simulação de planejamento financeiro para viagens com custos, poupança mensal e milhas
`base_perfis_viajantes_educacao_financeira.csv` : CSV | Perfis fictícios de viajantes com renda, hábitos financeiros e objetivos de viagem
`base_perfil_destino_ideal_viagens.csv` : Cruzamento entre perfil financeiro do viajante e destino ideal com tempo estimado para realização
`base_destinos_por_epoca_do_ano.csv` : Destinos do Brasil e do mundo organizados por mês, temporada, clima e perfil ideal
'''
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
