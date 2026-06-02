import streamlit as st
import time

st.set_page_config(page_title="Dispensador Inteligente", page_icon="🧵", layout="centered")

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "Inicio"
if "longitud" not in st.session_state:
    st.session_state.longitud = 120
if "cantidad" not in st.session_state:
    st.session_state.cantidad = 8
if "velocidad" not in st.session_state:
    st.session_state.velocidad = "Media"

st.title("🧵 DISPENSADOR INTELIGENTE")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    if st.button("🏠 Inicio"): st.session_state.pantalla = "Inicio"
with c2:
    if st.button("📏 Longitud"): st.session_state.pantalla = "Longitud"
with c3:
    if st.button("🔢 Cantidad"): st.session_state.pantalla = "Cantidad"
with c4:
    if st.button("✂️ Corte"): st.session_state.pantalla = "Corte"
with c5:
    if st.button("⚙️ Ajustes"): st.session_state.pantalla = "Ajustes"

st.divider()

if st.session_state.pantalla == "Inicio":
    st.metric("Longitud", f"{st.session_state.longitud} cm")
    st.metric("Cantidad", st.session_state.cantidad)

elif st.session_state.pantalla == "Longitud":
    st.session_state.longitud = st.number_input("Longitud (cm)", 10, 500, st.session_state.longitud)

elif st.session_state.pantalla == "Cantidad":
    st.session_state.cantidad = st.number_input("Cantidad", 1, 100, st.session_state.cantidad)

elif st.session_state.pantalla == "Corte":
    if st.button("▶ INICIAR CORTE"):
        barra = st.progress(0)
        for i in range(101):
            time.sleep(0.02)
            barra.progress(i)

elif st.session_state.pantalla == "Ajustes":
    st.session_state.velocidad = st.selectbox("Velocidad", ["Baja","Media","Alta"])
