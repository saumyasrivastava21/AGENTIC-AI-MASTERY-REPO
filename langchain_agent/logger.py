from pathlib import Path
from datetime import datetime


LOG_PATH = Path("logs/agent_logs.txt")


def log_event(title: str, data: str):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 80 + "\n")
        file.write(f"{datetime.now()} | {title}\n")
        file.write("-" * 80 + "\n")
        file.write(str(data))
        file.write("\n")