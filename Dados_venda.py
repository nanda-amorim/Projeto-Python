import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Assinaturas", layout="wide")
st.title("📊 Análise de Planos e Faturamento")
# Tupla de referência dos planos 
planos_original = [
    {"id_plano": 1, "regra_periodo": "Mensal", "valor_base": 56.50},
    {"id_plano": 2, "regra_periodo": "Semestral", "valor_base": 156.50},
    {"id_plano": 3, "regra_periodo": "Anual", "valor_base": 256.50}
]

#Tabela de Valores dos planos
st.write("### 💵 Tabela de Valores dos Planos")
df_precos = pd.DataFrame(planos_original)

df_precos.columns = ["ID do Plano", "Período", "Valor Base (R$)"]
st.dataframe(df_precos, hide_index=True, use_container_width=False)

st.divider() # Linha fina para separar a tabela dos gráficos

# Lista de Clientes
clientes_db = [
    {"id": 1, "nome": "Carlos Costa Marques", "estado": "BA"},
    {"id": 2, "nome": "Lucas Fernandes Martins", "estado": "CE"},
    {"id": 3, "nome": "Ana Souza Costa", "estado": "MG"},
    {"id": 4, "nome": "Gustavo Marques Nunes", "estado": "ES"},
    {"id": 5, "nome": "Laura Gomes Machado", "estado": "SP"},
    {"id": 6, "nome": "Enzo Costa Moreira", "estado": "SP"},
    {"id": 7, "nome": "Bruno Almeida Oliveira", "estado": "BA"},
    {"id": 8, "nome": "Amanda Ribeiro Gomes", "estado": "MG"},
    {"id": 9, "nome": "Nicole Andrade Nunes", "estado": "SP"},
    {"id": 10, "nome": "Amanda Gomes Costa", "estado": "RJ"}
]

# 2 Lista de assinaturas por cliente
assinaturas_db = [
    {"id_assinatura": 1, "cliente_id": 1, "plano": "Mensal", "valor": 56.50},
    {"id_assinatura": 2, "cliente_id": 2, "plano": "Anual", "valor": 256.50},
    {"id_assinatura": 3, "cliente_id": 3, "plano": "Mensal", "valor": 156.50},
    {"id_assinatura": 4, "cliente_id": 4, "plano": "Mensal", "valor": 56.50},
    {"id_assinatura": 5, "cliente_id": 5, "plano": "Anual", "valor": 256.50},
    {"id_assinatura": 6, "cliente_id": 6, "plano": "Mensal", "valor": 56.50},
    {"id_assinatura": 7, "cliente_id": 7, "plano": "Semestral", "valor": 156.50},
    {"id_assinatura": 8, "cliente_id": 8, "plano": "Mensal", "valor": 56.50},
    {"id_assinatura": 9, "cliente_id": 9, "plano": "Semestral", "valor": 256.50},
    {"id_assinatura": 10, "cliente_id": 10, "plano": "Mensal", "valor": 156.50}
]

# Transformando as duas listas em DataFrames do Pandas
df_clientes = pd.DataFrame(clientes_db)
df_assinaturas = pd.DataFrame(assinaturas_db)

# Junção das informações tabela clientes + assinaturas através do ID (chave estrangeira)
df_completo = pd.merge(df_assinaturas, df_clientes, left_on="cliente_id", right_on="id")

# --- CONSTRUÇÃO DOS GRÁFICOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.write("### 🏆 Planos Mais Vendidos")
    dados_planos = df_completo['plano'].value_counts()#contagem de planos
    st.bar_chart(dados_planos)

with col2:
    st.write("### 👥 Qtd. de Planos por Estado")
    # Conta quantos planos/assinaturas existem em cada estado
    planos_por_estado = df_completo['estado'].value_counts()
    st.bar_chart(planos_por_estado)

with col3:
    st.write("### 💰 Faturamento por Estado (R$)")
    # Soma o valor total de dinheiro por estado
    faturamento_estado = df_completo.groupby('estado')['valor'].sum()
    st.bar_chart(faturamento_estado)
