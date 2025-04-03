import streamlit as st
import pandas as pd
import random

def gerar_dados():
    # Gera dados 
    agora = pd.to_datetime("now")
    temperatura_ar = random.uniform(20.0, 35.0)
    umidade_ar = random.uniform(40.0, 90.0)
    temperatura_solo = random.uniform(18.0, 32.0)
    umidade_solo = random.uniform(20.0, 70.0)
    
    return {
        "Data/Hora": agora,
        "Temperatura Ar": temperatura_ar,
        "Umidade Ar": umidade_ar,
        "Temperatura Solo": temperatura_solo,
        "Umidade Solo": umidade_solo
    }

def avaliar_condicoes(temperatura_ar, umidade_ar, temperatura_solo, umidade_solo):
    alertas = []

    # ADAPTAR - - - - - - - - - ADAPTAR
    temp_ar_segura = (27, 32)
    umid_ar_segura = (50, 80)
    temp_solo_segura = (26, 30)
    umid_solo_segura = (30, 60)

    if not (temp_ar_segura[0] <= temperatura_ar <= temp_ar_segura[1]):
        alertas.append(f"⚠️ **Temperatura do Ar fora do ideal ({temperatura_ar:.2f}°C)**")
    if not (umid_ar_segura[0] <= umidade_ar <= umid_ar_segura[1]):
        alertas.append(f"⚠️ **Umidade do Ar fora do ideal ({umidade_ar:.2f}%)**")
    if not (temp_solo_segura[0] <= temperatura_solo <= temp_solo_segura[1]):
        alertas.append(f"⚠️ **Temperatura do Solo fora do ideal ({temperatura_solo:.2f}°C)**")
    if not (umid_solo_segura[0] <= umidade_solo <= umid_solo_segura[1]):
        alertas.append(f"⚠️ **Umidade do Solo fora do ideal ({umidade_solo:.2f}%)**")

    return alertas

def view_data():
    st.title("📡 Monitoramento de Temperatura e Umidade")

    dados = gerar_dados()
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="🌡️ Temperatura do Ar", value=f"{dados['Temperatura Ar']:.2f} °C")
        st.metric(label="💧 Umidade do Ar", value=f"{dados['Umidade Ar']:.2f} %")

    with col2:
        st.metric(label="🌍 Temperatura do Solo", value=f"{dados['Temperatura Solo']:.2f} °C")
        st.metric(label="🌱 Umidade do Solo", value=f"{dados['Umidade Solo']:.2f} %")

    # Analisando segurança dos ovos
    alertas = avaliar_condicoes(
        dados["Temperatura Ar"], dados["Umidade Ar"], 
        dados["Temperatura Solo"], dados["Umidade Solo"]
    )
    # Verificando se há alertas pendentes
    if alertas:
        st.error("⚠️ **Atenção! Algumas condições podem estar colocando os ovos em risco!**")
        for alerta in alertas:
            st.write(alerta)
    else:
        st.success("✅ **Todas as condições estão dentro dos níveis ideais para os ovos.**")

    # Mostrando o horário da última atualização
    st.write(f"📅 Última atualização: {dados['Data/Hora']}")

