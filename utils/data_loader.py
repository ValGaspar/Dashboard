import pandas as pd
import streamlit as st

@st.cache_data # Decorator que lê o csv apenas uma vez(otimização)
def carregar_dados():
    caminho_arquivo = './dataset/car_price_prediction_.csv'
    
    df = pd.read_csv(caminho_arquivo)
    
    return df