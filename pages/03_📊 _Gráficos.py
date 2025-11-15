import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import carregar_dados

st.set_page_config(
    page_title="Gráficos", 
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análise Gráfica dos Preços de Carros")
st.markdown("---")

df = carregar_dados()

#adicionamos os filtros na sidebar
st.sidebar.header("Filtros")

# Filtro por Marca
marcas = st.sidebar.multiselect(
    "Selecione a Marca",
    options=sorted(df['Brand'].unique()),
    default=None
)

# Filtro por Tipo de Combustível
tipos_combustivel = st.sidebar.multiselect(
    "Selecione o Tipo de Combustível",
    options=sorted(df['Fuel Type'].unique()),
    default=None
)

# Filtro por Ano de Fabricação
min_ano, max_ano = int(df['Year'].min()), int(df['Year'].max())
anos_selecionados = st.sidebar.slider(
    "Selecione o Intervalo de Anos",
    min_value=min_ano,
    max_value=max_ano,
    value=(min_ano, max_ano)
)

df_filtrado = df.copy()

if marcas:
    df_filtrado = df_filtrado[df_filtrado['Brand'].isin(marcas)]

if tipos_combustivel:
    df_filtrado = df_filtrado[df_filtrado['Fuel Type'].isin(tipos_combustivel)]

df_filtrado = df_filtrado[
    (df_filtrado['Year'] >= anos_selecionados[0]) & 
    (df_filtrado['Year'] <= anos_selecionados[1])
]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
else:
    st.subheader("Métricas Chave")
    col1, col2, col3 = st.columns(3)
    preco_medio = f"${df_filtrado['Price'].mean():,.2f}"
    km_media = f"{df_filtrado['Mileage'].mean():,.0f} km"
    qtd_carros = f"{df_filtrado.shape[0]}"
    col1.metric("Preço Médio", preco_medio)
    col2.metric("Quilometragem Média", km_media)
    col3.metric("Quantidade de Carros", qtd_carros)
    st.markdown("---")

    st.subheader("Visualizações")
    col_graf1, col_graf2 = st.columns(2)

    #Preço vs. Quilometragem (Interativo)
    fig_scatter = px.scatter(
        df_filtrado, 
        x='Mileage', 
        y='Price', 
        color='Brand',
        hover_data=['Model', 'Year'],
        title='Preço vs. Quilometragem por Marca'
    )
    col_graf1.plotly_chart(fig_scatter, use_container_width=True)

    #Preço Médio por Marca
    df_preco_marca = df_filtrado.groupby('Brand')['Price'].mean().sort_values(ascending=False).reset_index()
    fig_bar = px.bar(
        df_preco_marca, 
        x='Brand', 
        y='Price', 
        title='Preço Médio por Marca'
    )
    col_graf2.plotly_chart(fig_bar, use_container_width=True)

    col_graf3, col_graf4 = st.columns(2)

    #Contagem de Carros por Tipo de Transmissão
    fig_pie = px.pie(
        df_filtrado, 
        names='Transmission', 
        title='Proporção por Tipo de Transmissão'
    )
    col_graf3.plotly_chart(fig_pie, use_container_width=True)

    #Preço Médio por Ano de Fabricação
    df_preco_ano = df_filtrado.groupby('Year')['Price'].mean().reset_index()
    fig_line = px.line(
        df_preco_ano, 
        x='Year', 
        y='Price', 
        title='Evolução do Preço Médio por Ano de Fabricação'
    )
    col_graf4.plotly_chart(fig_line, use_container_width=True)