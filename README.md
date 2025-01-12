Dashboard Interativo de Vendas do Supermercado
Este projeto cria um dashboard interativo utilizando Python, Streamlit e Plotly para visualizar e analisar os dados de vendas de um supermercado. A aplicação apresenta gráficos para faturamento, desempenho de produtos e formas de pagamento, além de avaliações por filial.

📋 Funcionalidades
Faturamento por dia: Gráfico de barras exibindo o faturamento diário por cidade.
Tipo de produto mais vendido: Visualização horizontal do volume de vendas por linha de produto.
Contribuição por filial: Gráfico de barras mostrando o faturamento total por filial.
Desempenho das formas de pagamento: Gráfico de pizza detalhando a participação de cada método de pagamento.
Avaliações por loja: Gráfico das médias de avaliação por cidade.
🛠️ Tecnologias Utilizadas
Python 3.9+
Streamlit: Para criar o dashboard interativo.
Pandas: Para manipulação e análise dos dados.
Plotly: Para visualizações interativas.
📂 Estrutura do Projeto
bash
Copiar código
.
├── supermarket_sales.csv    # Base de dados do projeto
├── dashboard.py             # Código principal da aplicação
└── README.md                # Documentação do projeto
⚙️ Instalação e Configuração
1. Pré-requisitos
Certifique-se de que o Python 3.9+ está instalado em sua máquina. Para verificar:

bash
Copiar código
python --version
2. Instalar dependências
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
Instale as bibliotecas necessárias:

bash
Copiar código
pip install streamlit pandas plotly
3. Base de Dados
A base de dados utilizada, supermarket_sales.csv, contém as informações de vendas do supermercado e deve ser colocada no mesmo diretório do arquivo dashboard.py.

Certifique-se de que o arquivo está formatado com:

Separador: ;
Decimais representados por ,.
4. Executando o projeto
Para iniciar o dashboard:

bash
Copiar código
streamlit run dashboard.py
🗂️ Descrição do Código
1. Importações
python
Copiar código
import streamlit as st
import pandas as pd
import plotly.express as px
As bibliotecas necessárias são carregadas para criar o dashboard, manipular dados e gerar gráficos interativos.

2. Configuração do Layout
O layout do Streamlit é configurado como "wide" para melhor visualização.

python
Copiar código
st.set_page_config(layout="wide")
3. Leitura e Preparação dos Dados
Os dados são lidos do arquivo CSV e tratados:

python
Copiar código
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
4. Filtro por Mês
Um seletor de meses permite ao usuário escolher o período a ser analisado:

python
Copiar código
month = st.sidebar.selectbox("Mês", df["Month"].unique())
dt_filtered = df[df["Month"] == month]
5. Criação dos Gráficos
Faturamento por dia
Gráfico de barras agrupado por cidade:

python
Copiar código
fig_date = px.bar(dt_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_widt=True)
Tipo de produto mais vendido
Gráfico horizontal mostrando o desempenho dos produtos:

python
Copiar código
fig_prod = px.bar(dt_filtered, x="Date", y="Product line", color="City", title="Tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_widt=True)
Contribuição por filial
Soma do faturamento total por cidade:

python
Copiar código
city_total = dt_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_widt=True)
Desempenho das formas de pagamento
Gráfico de pizza com participação por método de pagamento:

python
Copiar código
fig_kind = px.pie(dt_filtered, values="Total", names="Payment", title="Desempenho das formas de pagamento")
col4.plotly_chart(fig_kind, use_container_widt=True)
Avaliações por loja
Média de avaliações por cidade:

python
Copiar código
city_total = dt_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(dt_filtered, y="Rating", x="City", title="Avaliações")
col5.plotly_chart(fig_rating, use_container_widt=True)
💡 Notas
Responsividade: O layout é adaptado para telas maiores, oferecendo uma experiência agradável.
Exploração de Dados: Permite selecionar meses e visualizar detalhes específicos de faturamento e avaliações.
🖼️ Exemplo de Uso
Ao executar o projeto, selecione um mês no menu lateral.
Analise os gráficos interativos para obter insights sobre:
Desempenho diário de vendas.
Tipos de produtos mais vendidos.
Faturamento por filial.
Preferências de pagamento.
Avaliações dos clientes.
