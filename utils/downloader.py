import os
from yt_dlp import YoutubeDL

VIDEOS_DIR = "videos"

def download_video(url: str):
    """
    Baixa o vídeo do YouTube na pasta 'videos/' em qualidade <= 360p.
    Retorna título e duração em segundos.
    """
    os.makedirs(VIDEOS_DIR, exist_ok=True)

    ydl_opts = {
        "format": "best[height<=360]",
        "outtmpl": f"{VIDEOS_DIR}/%(title)s.%(ext)s",
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "Unknown")
        duration = info.get("duration", 0)

    return title, duration
