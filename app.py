import streamlit as st
import os

st.set_page_config(
    page_title="Dashboard Funil · Pródentis",
    page_icon="📊",
    layout="wide"
)

# Remove padding do Streamlit para o HTML ocupar tela toda
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        header { display: none !important; }
        footer { display: none !important; }
    </style>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "Dashboard_Funil.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1100, scrolling=True)
