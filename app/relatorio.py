import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcular_impacto(media):
    if media < 30:
        return "Baixo Impacto", "green"
    elif 30 <= media < 70:
        return "Médio Impacto", "orange"
    else:
        return "Alto Impacto", "red"

def gerar_relatorio(df):
    st.title("Relatório de Impacto Ambiental")
    
    if df.empty:
        st.warning("Nenhum dado disponível para análise.")
        return
    
    media = df["valor"].mean()
    impacto, cor = calcular_impacto(media)
    
    st.subheader("Média dos Últimos Dados")
    st.metric(label="Média", value=f"{media:.2f}ºC")
    
    st.subheader("Classificação de Impacto")
    st.markdown(f"<h3 style='color:{cor};'>{impacto}</h3>", unsafe_allow_html=True)
    
    st.subheader("Distribuição dos Dados")
    fig, ax = plt.subplots()
    ax.hist(df["valor"], bins=10, color=cor, alpha=0.7)
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frequência")
    ax.set_title("Histograma dos Dados")
    st.pyplot(fig)

def view_relatorio():
    data = {"valor": np.random.randint(10, 100, 50)} 
    sample_df = pd.DataFrame(data)
    gerar_relatorio(sample_df)