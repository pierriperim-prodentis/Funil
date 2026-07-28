import streamlit as st
import os

st.set_page_config(
    page_title="Dashboard Funil · Pródentis",
    page_icon="📊",
    layout="wide"
)

# ── Proteção por chave na URL ──────────────────────
CHAVE_CORRETA = "prodentis2026"

params = st.query_params
chave = params.get("chave", "")

if chave != CHAVE_CORRETA:
    st.markdown("""
        <style>
            .block-container { padding: 3rem 2rem !important; }
            header { display: none !important; }
        </style>
    """, unsafe_allow_html=True)
    st.error("🔒 Acesso restrito. Utilize o link correto fornecido pela equipe.")
    st.stop()

# ── Dashboard ──────────────────────────────────────
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
