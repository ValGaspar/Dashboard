#  dar pip install streamlit e importar
# set config pra onfigurar as páginas com título e entre outros

import streamlit as st

st.set_page_config(
  page_title="Início",
  page_icon="🏠",
)

st.title("Bem-vindo ao App de gráficos!")
st.sidebar.success("Selecione uma página acima.")
st.markdown(
  """
  Esta é a página inicial da sua aplicação multi-páginas Streamlit.
  👈 Selecione uma página na barra lateral para começar!
  """
)
