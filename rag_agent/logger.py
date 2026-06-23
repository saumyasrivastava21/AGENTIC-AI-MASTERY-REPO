from pathlib import Path
from datetime import datetime

LOG_FILE = Path("logs/rag.log")


def log_event(title: str, message: str):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 80 + "\n")
        file.write(f"{datetime.now()} | {title}\n")
        file.write("-" * 80 + "\n")
        file.write(str(message))
        file.write("\n")