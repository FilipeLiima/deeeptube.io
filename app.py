import streamlit as st
from main import process_url

st.set_page_config(page_title="Deep Tube", page_icon="🎬", layout="centered")
st.title("🎬 Deep Tube - YouTube Downloader")

st.markdown(
    "Cole a URL do vídeo do YouTube abaixo e clique em **Download**."
)

# Campo de input
url = st.text_input("YouTube URL:")

# Botão para processar
if st.button("Download"):
    if url.strip() == "":
        st.warning("Por favor, insira uma URL.")
    else:
        with st.spinner("Processando..."):
            result = process_url(url.strip())
            st.success(result)  # <-- parêntese fechado corretamente

