import os
from yt_dlp import YoutubeDL

# Pasta onde os vídeos serão salvos
VIDEOS_DIR = "videos"

def download_video(url: str):
    """
    Baixa o vídeo do YouTube na pasta 'videos/' em qualidade <= 360p.
    Retorna o título do vídeo e a duração em segundos.
    """
    # Cria a pasta 'videos/' se não existir
    os.makedirs(VIDEOS_DIR, exist_ok=True)

    # Configurações do yt-dlp
    ydl_opts = {
        "format": "best[height<=360]",  # baixa a melhor qualidade até 360p
        "outtmpl": f"{VIDEOS_DIR}/%(title)s.%(ext)s",  # define o nome do arquivo
        "quiet": True  # modo silencioso, sem logs do yt-dlp
    }

    # Executa o download do vídeo
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "Desconhecido")
        duration = info.get("duration", 0)

    # Retorna título e duração
    return title, duration
