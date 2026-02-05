from utils.validators import is_valid_youtube_url
from utils.logger import log_event
from utils.downloader import download_video


def process_url(url: str) -> str:
    """
    Processa a URL do YouTube:
    - Valida se a URL é válida
    - Baixa o vídeo em baixa resolução (360p)
    - Registra logs de sucesso ou erro

    Retorna uma mensagem de status para exibir no terminal ou na interface.
    """
    if not is_valid_youtube_url(url):
        log_event(f"URL inválida recebida: {url}")
        return "URL do YouTube inválida"

    try:
        title, duration = download_video(url)
        log_event(
            f"SUCESSO | URL: {url} | Título: {title} | Duração: {duration}s"
        )
        return f"Download concluído!\nTítulo: {title}\nDuração: {duration} segundos"

    except Exception as e:
        log_event(
            f"ERRO | URL: {url} | Erro: {str(e)}"
        )
        return f"Ocorreu um erro: {str(e)}"


if __name__ == "__main__":
    # Solicita ao usuário a URL do YouTube
    url = input("Insira a URL do vídeo do YouTube: ").strip()
    result = process_url(url)
    print(result)
