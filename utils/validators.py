import re

# Regex simples para URLs do YouTube
YOUTUBE_REGEX = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"

def is_valid_youtube_url(url: str) -> bool:
    """
    Retorna True se a URL é um link válido do YouTube.
    """
    return re.match(YOUTUBE_REGEX, url) is not None
