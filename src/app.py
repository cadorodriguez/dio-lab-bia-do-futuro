import json
import streamlit as st
import pandas as pd
import requests

# ========= CONFIG OLLAMA (GRATUITO LOCAL) =========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3:latest"

# ========= CARREGAR DADOS =========
perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))

transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")

base_destinos = pd.read_csv("./data/base_destinos_por_epoca_do_ano.csv")
base_perfil_destino = pd.read_csv("./data/base_perfil_destino_ideal_viagens.csv")
base_perfis = pd.read_csv("./data/base_perfis_viajantes_educacao_financeira.csv")
dados_educacao = pd.read_csv("./data/dados_ficticios_educacao_financeira_viagens.csv")

# ========= MONTAR CONTEXTO =========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}

PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES (últimas 10):
{transacoes.tail(10).to_string(index=False)}

ATENDIMENTOS ANTERIORES (últimos 10):
{historico.tail(10).to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========= SYSTEM PROMPT =========
SYSTEM_PROMPT = """Você é Tami, uma agente especializada em educação financeira para viagens.

Seu objetivo é ajudar usuários a planejar viagens de forma consciente, prática e realista, respeitando renda, prazo e capacidade de poupança.

REGRAS:
1. Sempre baseie cálculos nos dados fornecidos pelo usuário.
2. Não invente renda ou valores financeiros.
3. Quando estimar custos, deixe claro que são projeções.
4. Priorize realismo financeiro.
5. Não incentive endividamento irresponsável.
6. Não peça nem forneça dados sensíveis (senhas, cartões etc.).
7. Se a pergunta estiver fora do escopo financeiro de viagens, informe e redirecione.

TOM: claro, direto, didático e estratégico. Motivador sem falsas expectativas.
"""

# ========= CHAMAR OLLAMA =========
def perguntar(msg: str) -> str:
    prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False},
            timeout=300
        )
        r.raise_for_status()
        data = r.json()
        return data.get("response", "Não consegui gerar uma resposta agora.")
    except requests.exceptions.ConnectionError:
        return "Não consegui conectar ao Ollama. Confere se ele está rodando (ollama serve / ollama run llama3)."
    except Exception as e:
        return f"Ocorreu um erro ao consultar o modelo: {e}"

# ========= INTERFACE =========
st.title("Olá sou a Tami, uma agente especializada em educação financeira para viagens")

if pergunta := st.chat_input("Sua dúvida sobre viagem..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))