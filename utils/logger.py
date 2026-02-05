from datetime import datetime

LOG_FILE = "download_log.txt"

def log_event(message: str):
    """
    Escreve uma linha de log no arquivo download_log.txt
    com timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
