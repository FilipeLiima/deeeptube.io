from utils.validators import is_valid_youtube_url
from utils.logger import log_event, save_history
from utils.downloader import download_video

def process_url(url: str):
    """
    Processa uma URL do YouTube:
    - Valida a URL
    - Baixa o vídeo
    - Registra logs
    - Salva histórico
    Retorna mensagem de status e dados do vídeo
    """
    if not is_valid_youtube_url(url):
        log_event(f"URL inválida recebida: {url}")
        return {"status": "erro", "mensagem": "URL do YouTube inválida"}

    try:
        title, duration = download_video(url)
        log_event(f"SUCESSO | URL: {url} | Título: {title} | Duração: {duration}s")
        save_history(title, url, duration)  # salva histórico
        return {"status": "sucesso", "mensagem": f"Download concluído!\nTítulo: {title}\nDuração: {duration} segundos", "title": title, "url": url, "duration": duration}

    except Exception as e:
        log_event(f"ERRO | URL: {url} | Erro: {str(e)}")
        return {"status": "erro", "mensagem": f"Ocorreu um erro: {str(e)}"}
        

if __name__ == "__main__":
    urls = input("Cole a(s) URL(s) do YouTube, separadas por vírgula: ").split(",")
    for url in urls:
        url = url.strip()
        res = process_url(url)
        print(res["mensagem"])
