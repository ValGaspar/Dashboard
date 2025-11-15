import streamlit as st
from utils.data_loader import carregar_dados

st.set_page_config(
    page_title="Conjunto de Dados", 
    page_icon="🎲",
    layout="wide"
)

st.title("Visualização do Conjunto de Dados")
st.markdown("---")

df = carregar_dados()

st.markdown("### Dados Brutos")
st.dataframe(df)

st.markdown("---")

st.markdown("### Estatísticas Descritivas")
st.write(df.describe())

st.markdown("---")

with st.expander("Dicionário de Dados (Descrição das Colunas)"):
    st.markdown("""
    - **ID**: Identificador único para cada veículo listado.
    - **Price**: O preço de venda do veículo em Dólares Americanos (USD). **(Nossa variável alvo)**
    - **Brand**: A marca do fabricante do veículo (ex: Toyota, Ford, Honda).
    - **Model**: O modelo específico do veículo (ex: Camry, F-150, Civic).
    - **Year**: O ano de fabricação do veículo.
    - **Engine Capacity (l)**: A capacidade do motor em litros.
    - **Fuel Type**: O tipo de combustível que o veículo utiliza (ex: Gasolina, Diesel, Elétrico).
    - **Transmission**: O tipo de transmissão do veículo (Manual ou Automática).
    - **Mileage (km)**: A quilometragem total percorrida pelo veículo em quilômetros.
    - **Condition**: O estado de conservação do veículo (Novo, Usado, etc.).
    """)


with st.expander("Entenda as Métricas"):
    st.markdown("""
    - **count**: O número total de registros ou linhas não nulas.
    - **mean**: A média aritmética de todos os valores na coluna.
    - **std** (Standard Deviation): O desvio padrão, que mede a dispersão ou variabilidade dos dados. Um valor baixo indica que os dados estão próximos da média.
    - **min**: O menor valor encontrado na coluna.
    - **25%** (Primeiro Quartil): 25% dos dados estão abaixo deste valor.
    - **50%** (Mediana ou Segundo Quartil): O valor do meio, que divide os dados em duas metades iguais. 50% dos dados estão abaixo deste valor.
    - **75%** (Terceiro Quartil): 75% dos dados estão abaixo deste valor.
    - **max**: O maior valor encontrado na coluna.
    """)

    st.markdown("---")