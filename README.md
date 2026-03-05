# 🎬 Deep Tube

Deep Tube é um sistema em Python para **baixar vídeos do YouTube** de forma simples e automatizada.  
O projeto possui uma **interface web interativa com Streamlit** e também pode ser usado via terminal.

Ele valida URLs, baixa vídeos em baixa resolução (360p) e registra logs de download.

ACESSO APP DISPONÍVEL EM: https://deeptube-youtube.streamlit.app/ <br>
APRESENTAÇÃO: 

## 📌 Funcionalidades

- Validação de URLs do YouTube
- Download automático de vídeos em até 360p
- Criação automática da pasta `videos/` para armazenar os arquivos
- Registro de logs de download e erros no arquivo `download_log.txt`
- Interface web simples usando **Streamlit** para usuários não técnicos
- Suporte a execução via terminal

---

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) – para download de vídeos do YouTube
- [**Streamlit**](https://streamlit.io/) – para interface web interativa

---

## 📁 Estrutura do Projeto

deeptube/
├── main.py
│ Lógica principal de download e validação
├── app.py
│ Interface web Streamlit
├── utils/
│ Funções auxiliares
│ ├── downloader.py
│ │ Função para baixar vídeos
│ ├── logger.py
│ │ Função para registrar logs
│ └── validators.py
│ Função para validar URLs
├── videos/
│ Pasta onde os vídeos baixados são salvos
└── download_log.txt
Log de downloads e erros

## ⚡ Como Executar

1. Clonar o repositório:

```bash
git clone https://github.com/FilipeLiima/deeeptube.io.git
cd deeeptube.io
Instalar dependências:

python -m pip install --upgrade pip
python -m pip install streamlit yt-dlp
Executar:

Opção 01 - Via terminal: python main.py

Opção 02 - Via interface web: python -m streamlit run app.py → abre no navegador em http://localhost:8501

Cole a URL do YouTube e clique em Download. O vídeo será salvo na pasta videos/ e os logs serão atualizados.
```
