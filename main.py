from utils.validators import is_valid_youtube_url
from utils.logger import log_event, save_history
from utils.downloader import download_video
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 2  # Quantos downloads simultâneos

def process_url(url: str):
    if not is_valid_youtube_url(url):
        log_event(f"URL inválida recebida: {url}")
        return {"status": "erro", "url": url, "mensagem": "URL do YouTube inválida"}

    try:
        title, duration = download_video(url)
        log_event(f"SUCESSO | URL: {url} | Título: {title} | Duração: {duration}s")
        save_history(title, url, duration)
        return {
            "status": "sucesso",
            "url": url,
            "title": title,
            "duration": duration,
            "mensagem": f"Download concluído: {title}"
        }

    except Exception as e:
        log_event(f"ERRO | URL: {url} | Erro: {str(e)}")
        return {"status": "erro", "url": url, "mensagem": str(e)}


def process_urls_batch(urls: list[str]):
    """
    Processa múltiplas URLs usando fila assíncrona com threads
    """
    resultados = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # cria as tasks
        futures = {executor.submit(process_url, url): url for url in urls}

        # pega resultados conforme vão terminando
        for future in as_completed(futures):
            resultado = future.result()
            resultados.append(resultado)

    return resultados
