
import csv
from pathlib import Path

LOG_FILE = Path("index/metrics.csv")

def log_metrics(query, latency):
    LOG_FILE.parent.mkdir(exist_ok=True)
    write_header = not LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["query", "latency_seconds"])
        writer.writerow([query, latency])
