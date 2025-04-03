import streamlit as st
import pandas as pd
import numpy as np

def main_view():
    st.title("🌍 Bem-Vindo ao Sistema de Visualização")
    
    st.subheader("📊 Interface Interativa para Monitoramento Ambiental")
    st.write("""
        Este sistema permite a visualização de dados de sensores de temperatura e umidade do ar e solo, 
        ajudando no controle de chocadeiras de quelônios. Com ele, você pode:
        
        ✅ **Monitorar dados em tempo real**  
        📈 **Visualizar históricos e tendências**  
        🔔 **Receber alertas automáticos sobre variações perigosas**  
        📊 **Analisar gráficos e relatórios de impacto ambiental**  
    """)

    st.divider()  # Linha divisória estilizada

    st.subheader("📈 Gráfico de Exemplo")
    # Criando dados fictícios para um gráfico
    dias = np.arange(1, 11)
    temperatura = np.random.uniform(25, 35, 10)  # Simula variações de temperatura
    umidade = np.random.uniform(40, 70, 10)  # Simula variações de umidade

    # Criando um dataframe para plotar
    df = pd.DataFrame({
        "Dias": dias,
        "Temperatura (°C)": temperatura,
        "Umidade (%)": umidade
    })

    # Criando gráfico de temperatura e umidade
    st.line_chart(df.set_index("Dias"))

    st.info("🔍 Explore as opções no menu lateral para visualizar os dados detalhados.")

