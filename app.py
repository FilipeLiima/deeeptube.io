import streamlit as st
import pandas as pd
import os
from main import process_urls_batch
from utils.logger import HISTORY_FILE

st.set_page_config(
    page_title="Deep Tube",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 DeepTube - Multi-download YouTube")
st.write("Cole uma ou mais URLs do YouTube (uma por linha) para baixar vídeos.")

urls_text = st.text_area("URLs do YouTube:", height=150)
urls = [u.strip() for u in urls_text.splitlines() if u.strip()]

if st.button("⬇️ Iniciar Download") and urls:
    progress = st.progress(0)
    total = len(urls)
    with st.spinner("Processando downloads em fila..."):
        results = process_urls_batch(urls)

    for i, r in enumerate(results):
        if r["status"] == "sucesso":
            st.success(f"{i+1}/{total} ✅ {r['mensagem']}")
        else:
            st.error(f"{i+1}/{total} ❌ {r['mensagem']}")
        progress.progress((i+1)/total)

    st.success("Todos os downloads foram processados!")

st.write("---")
st.subheader("📜 Histórico de Downloads")

if os.path.isfile(HISTORY_FILE):
    df = pd.read_csv(HISTORY_FILE)
    st.dataframe(df)
else:
    st.info("Nenhum histórico registrado ainda.")
