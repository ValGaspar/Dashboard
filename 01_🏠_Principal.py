import streamlit as st

st.set_page_config(
  page_title="Principal",
  page_icon="🏠",
  layout="wide"
)

st.title("Dashboard de Análise de Preços de Carros")
st.sidebar.success("Navegue pelas páginas acima.")

st.markdown("---")

# documentação
st.markdown(
    """
    ## 📄 Documentação da Página Interativa de Análises

    Essa página é onde a gente realmente brinca com os dados e deixa tudo dinâmico.  
    Aqui os gráficos mudam conforme você mexe nos filtros, e dá pra analisar os carros de um jeito bem visual e sem complicação.

    ---

    ### 🔍 Filtros
    Na lateral você encontra os filtros que controlam tudo na página.  
    Dá pra escolher:

    - **Marca**
    - **Ano**
    - **Tipo de combustível**
    - **Transmissão**
    - **Condição**
    
    Qualquer mudança nesses filtros já reflete de imediato nos gráficos, sem precisar clicar em nada.

    ---

    ### 📊 Gráficos disponíveis
    Aqui ficam todos os gráficos interativos que ajudam a entender os dados de forma rápida:

    **• Relação entre características (gráfico interativo)**  
    Mostra como diferentes variáveis do carro se relacionam, ajudando a identificar padrões.

    **• Preço médio por marca**  
    Um gráfico de barras que ajuda a ver quais marcas têm maior valor médio.

    **• Distribuição por tipo de combustível**  
    Um gráfico de pizza mostrando a proporção de cada combustível na base.

    **• Preço médio por ano**  
    Permite ver se os carros mais novos realmente têm preços mais altos.

    **• Preço por condição (boxplot)**  
    Mostra como o preço muda dependendo se o carro é novo, seminovo, usado, etc.

    Todos os gráficos são totalmente interativos (Plotly), permitindo zoom, hover, esconder/mostrar séries e exportar.

    ---

    ### 📈 Métricas principais
    No topo da página aparecem três números rápidos pra já ter uma noção geral:

    - Preço médio dos carros
    - Quilometragem média
    - Total de veículos na base

    São só informações rápidas pra situar antes de olhar os gráficos.

    ---

    ### 🎯 Resumo 
    Esta página tem como objetivo oferecer uma visualização clara, dinâmica e interativa dos dados, 
    permitindo que o usuário explore preços, quilometragem, marcas e demais características de maneira flexível.  
    Os filtros atualizam os gráficos instantaneamente, facilitando a identificação de padrões, tendências 
    e comparações relevantes dentro do conjunto de dados.

    """
)
