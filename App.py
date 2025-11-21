import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
X = df[['diametro']]
y = df[['preco']]
modelo.fit(X, y)

st.title('Previsão de Preço de Pizza')
st.divider()
diametro = st.number_input("Digite o diâmetro da pizza (em cm):", min_value=10, max_value=50, step=1, key='diametro_input')

if diametro: 
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O preço previsto para uma pizza de {diametro} cm é R$ {preco_previsto:.2f}")