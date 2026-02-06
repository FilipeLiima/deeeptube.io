from datetime import datetime
import csv
import os

LOG_FILE = "download_log.txt"
HISTORY_FILE = "download_history.csv"

def log_event(message: str):
    """
    Salva logs de download ou erro em download_log.txt
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")  # só data + hora, sem segundos
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def save_history(title: str, url: str, duration: int):
    """
    Salva histórico de downloads em CSV
    """
    exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["Data", "Título", "URL", "Duração"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), title, url, duration])  # só data + hora
