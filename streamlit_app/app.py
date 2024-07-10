import os
import requests
import pandas as pd
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Carregar a chave da API do arquivo .env
api_token = os.getenv("BRAPI_API_TOKEN")

# Função para buscar dados da API
def fetch_stock_data(symbol):
    url = f'https://brapi.dev/api/quote/{symbol}?token={api_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results'][0]
    else:
        st.error(f"Erro {response.status_code}: {response.text}")
        return None

# Função para converter dados para DataFrame
def convert_to_dataframe(stock_data):
    df = pd.json_normalize(stock_data)
    return df

# Configuração do Streamlit
st.title("Análise Financeira")
st.sidebar.header("Configurações")

# Seleção de ações
stock_symbols = ['PETR4',
                'VALE3',
                'ITUB4', 
                'B3SA3', 
                'JBSS3', 
                'LREN3', 
                'MGLU3', 
                'AZUL4', 
                'BOVA11', 
                'SMAL11']
selected_stock = st.selectbox("Selecione a ação", stock_symbols)

# Buscar dados da API
stock_data = fetch_stock_data(selected_stock)

if stock_data:
    # Exibir dados básicos
    st.subheader(f"Dados da ação: {stock_data['symbol']}")
    st.write("Nome:", stock_data['longName'])
    st.write("Preço:", stock_data['regularMarketPrice'])
    st.write("Volume:", stock_data['regularMarketVolume'])

    try:
        # Exibir a data usando datetime.fromisoformat
        market_time = datetime.fromisoformat(stock_data['regularMarketTime'].replace("Z", "+00:00"))
        st.write("Data:", market_time)
    except ValueError:
        st.error("Erro ao converter 'regularMarketTime' para datetime")

    # Converter dados para DataFrame e exibir tabela
    df = convert_to_dataframe(stock_data)
    st.write("Tabela de Dados")
    st.dataframe(df)

    # Verifique a existência da coluna 'regularMarketTime'
    if 'regularMarketTime' in df.columns:
        # Converta a coluna de timestamp para data sem especificar a unidade
        df['date'] = pd.to_datetime(df['regularMarketTime'])
        st.write("Dados com datas:", df)
        
        # Exibir gráfico de preços (exemplo)
        st.line_chart(df.set_index('date')[['regularMarketPrice']])
    else:
        st.error("A coluna 'regularMarketTime' não está presente nos dados")

else:
    st.error("Falha ao buscar dados da API")
