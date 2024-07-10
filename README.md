# Financial Analysis App

Este projeto é uma aplicação de análise financeira desenvolvida utilizando Python, Django, MongoDB e Streamlit. A aplicação busca dados de ativos da bolsa de valores utilizando a API da Brapi.dev e apresenta esses dados em um dashboard interativo utilizando o Streamlit.

## Funcionalidades Atuais

- API de Dados: Integração com a API da Brapi.dev para buscar informações sobre símbolos de ativos da bolsa.

- Dashboard Interativo: Utilização do Streamlit para visualizar dados em tempo real dos ativos selecionados.

- Análise Financeira Básica: Apresentação de informações como preço atual, variação percentual, volume, entre outros dados relevantes dos ativos.

## Como Executar

### 1. Pré-requisitos

- Python 3.12 instalado
- MongoDB instalado e configurado

### 2. Instalação das Dependências

```text
pip install -r requirements.txt
```

### 3. Configuração do Ambiente

- Renomeie o arquivo `.env.example` para `.env` e configure as variáveis de ambiente necessárias, como chaves de API.`

### 4. Executar o Backend (Django)

```text
python manage.py runserver
```

### 5. Executar o Frontend (Streamlit)

```text
streamlit run streamlit_app/app.py
```

### 6. Acessar a Aplicação

- Acesse a URL local fornecida pelo Streamlit para visualizar o dashboard.

## Escalabilidade

Para escalar a aplicação financeira:

- Otimização de Código: Refatoração para melhorar a eficiência do código e otimizar consultas de dados.

- Cache de Dados: Implementação de cache para reduzir o tempo de resposta e minimizar chamadas frequentes à API.

- Banco de Dados Distribuído: Considerar a migração para um banco de dados distribuído para lidar com volumes maiores de dados.

- Servidores e Balanceamento de Carga: Utilização de servidores dedicados e balanceamento de carga para suportar um grande número de usuários simultâneos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar pull requests com melhorias ou novas funcionalidades.
