import streamlit as st
import pandas as pd
import numpy as np

def view_historico():
    st.title("📊 Histórico de Temperatura e Umidade")

    st.write("Aqui você pode visualizar o histórico das medições de temperatura e umidade do ambiente.")

    # Simulando dados históricos de 10 dias
    dias = np.arange(1, 11)
    temperatura = np.random.uniform(25, 35, 10)  # Valores aleatórios de temperatura
    umidade = np.random.uniform(40, 70, 10)  # Valores aleatórios de umidade

    # Criando um dataframe
    df = pd.DataFrame({
        "Dias": dias,
        "Temperatura (°C)": temperatura,
        "Umidade (%)": umidade
    })

    # Encontrando os extremos
    temp_max = df.loc[df["Temperatura (°C)"].idxmax()]
    temp_min = df.loc[df["Temperatura (°C)"].idxmin()]

    # Exibindo o gráfico de linha
    st.line_chart(df.set_index("Dias"))

    # Destaques de Temperatura Máxima e Mínima
    st.subheader("📌 Destaques do Histórico")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🌡️ Temperatura Máxima", value=f"{temp_max['Temperatura (°C)']:.2f} °C", delta="Mais quente")
    with col2:
        st.metric(label="❄️ Temperatura Mínima", value=f"{temp_min['Temperatura (°C)']:.2f} °C", delta="Mais frio")

    st.info("🔍 Acompanhe os padrões de temperatura para melhor controle da chocadeira.")

