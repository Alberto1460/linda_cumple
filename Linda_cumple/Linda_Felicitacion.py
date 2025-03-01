import streamlit as st
import time
from PIL import Image
import random

st.set_page_config(page_title="Felicitaciones ❤️", layout="wide")

# Estilos generales (fondo, animación de corazones, tipografías)
st.markdown(
    """
    <style>
        body {
            background-color: #FFB6C1;
        }
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            50% { transform: rotate(10deg); }
            100% { transform: rotate(0deg); }
        }
        .message {
            font-family: 'Pacifico', cursive;
            text-align: center;
            font-size: 26px;
            color: #8B0000;
            background: rgba(255, 255, 255, 0.8);
            padding: 25px;
            border-radius: 20px;
            margin-top: 30px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .title {
            font-family: 'Dancing Script', cursive;
            text-align: center;
            font-size: 40px;
            color: #DC143C;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        .image-container {
            text-align: center;
        }
        .rotated-image {
            width: 50%;
            max-width: 300px;
            border-radius: 20px;
            box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.3);
            animation: rotate 3s infinite ease-in-out;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<div class='title'>💖 ¡Felicitaciones para el Amor de mi Vida! 💖</div>", unsafe_allow_html=True)
st.image("https://raw.githubusercontent.com/Alberto1460/linda_cumple/main/Linda_cumple/images/lindarecuerdo.jpg", use_column_width=True)

# Mensaje de amor
st.markdown(
    """
    <div class='message'>
    🌹 *Mi amor hermoso Linda,* 🌹<br>
    ✨ Eres mi más grande bendición y mi razón de ser. 💕<br>
    Cada día a tu lado es un poema lleno de amor y felicidad. 🎶💖<br>
    Gracias por llenar mi vida con tu luz y tu alegría. 😊💫<br>
    Siempre estaré para ti, mi Reina Hermosa. TE AMO MUCHOTEEEE. ❤️❤️❤️❤️❤️
    </div>
    """,
    unsafe_allow_html=True
)

# Cálculos de tiempos
dias_totales = 8036
anos_totales = 22
dias_con_novio = 574
anos_con_novio = 1
dias_futuros = 18250
anos_futuros = 50

st.markdown(
    f"""
    <div class='message'>
    💕 Desde que llegaste a este mundo han pasado **{anos_totales} años** o **{dias_totales} días** llenos de historias, momentos y aprendizajes. 💫<br>
    💖 Juntos hemos compartido **{anos_con_novio} año o {dias_con_novio} días** de amor infinito, abrazos cálidos y sonrisas compartidas. 😊💕<br>
    ⏳ Nos espera un futuro maravilloso por delante: **{anos_futuros} años o {dias_futuros} días** más para seguir amándonos, soñando juntos y construyendo un amor eterno. 💍✨<br>
    **Mi amor por ti es para siempre, mi hermosa reina. Te amo con toda mi alma. ❤️❤️❤️**
    </div>
    """,
    unsafe_allow_html=True
)

# Pregunta de amor
st.markdown("<div class='title'>💞 ¿Me amas mi amor? 💞</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    if st.button("💖 SÍ 💖", key="yes", help="Dale click mi amor!"):
        st.markdown("<div class='message'>🎆✨ ¡Yo te amo más, mi amor! ✨🎆</div>", unsafe_allow_html=True)
        st.balloons()
        st.snow()

with col2:
    if st.button("💔 NO 💔", key="no", help="¡No puedes decir eso!"):
        st.markdown("<div class='message'>💘 Eso es imposible amor, tú me amas muchote! 💘</div>", unsafe_allow_html=True)
        st.snow()

st.image("https://raw.githubusercontent.com/Alberto1460/linda_cumple/main/Linda_cumple/images/josue.jpg", use_column_width=True)


st.balloons()
time.sleep(2)
st.snow()
