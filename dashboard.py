import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# visão mensal de

# Faturamento por unidade... 
# Tipo de produto mais vendido, 
# Contribuição por Filial
# Desempenho das formas de pagamento
# Como estão as Avaliações de cada loja

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"]) #para o pandas entender que a data da planilha não é um obejeto 
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

dt_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5= st.columns(3)

# Faturamento por dia
fig_date = px.bar(dt_filtered, x="Date", y="Total", color="City" , title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_widt=True)

# Tipo de produto
fig_prod = px.bar(dt_filtered, x="Date", y="Product line", 
        color="City" , title="Tipo de produto", 
        orientation="h")
col2.plotly_chart(fig_prod, use_container_widt=True)


# Contribuição por Filial
city_total = dt_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", 
        title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_widt=True)


#Desempenho das formas de pagamento
fig_kind = px.pie(dt_filtered, values="Total", names="Payment", 
        title="Desempenho das formas de pagamento")
col4.plotly_chart(fig_kind, use_container_widt=True)

city_total = dt_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(dt_filtered, y="Rating", x="City", 
        title="Avaliações")
col5.plotly_chart(fig_rating, use_container_widt=True)