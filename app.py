import streamlit as st
import pandas as pd
from main import process_url
from utils.logger import HISTORY_FILE
import os

st.set_page_config(page_title="Deep Tube", page_icon="🎬")
st.title("🎬 Deep Tube - Multi-download YouTube")
st.write("Cole uma ou várias URLs do YouTube (uma por linha) para baixar vídeos.")

# Text area para múltiplas URLs
urls_text = st.text_area("URLs do YouTube", height=150)
urls = [u.strip() for u in urls_text.splitlines() if u.strip()]

if st.button("Iniciar Download") and urls:
    progress_bar = st.progress(0)
    results = []

    for i, url in enumerate(urls):
        res = process_url(url)
        results.append(res)
        st.write(f"{i+1}/{len(urls)}: {res['mensagem']}")
        progress_bar.progress((i+1)/len(urls))

    st.success("Todos os downloads foram processados!")

# Mostrar histórico
st.write("---")
st.subheader("📜 Histórico de Downloads")
if os.path.isfile(HISTORY_FILE):
    df = pd.read_csv(HISTORY_FILE)
    st.dataframe(df)
else:
    st.write("Nenhum histórico encontrado.")
