import re

def is_valid_youtube_url(url: str) -> bool:
    """
    Verifica se a URL é um link válido do YouTube
    """
    regex = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return bool(re.match(regex, url))
