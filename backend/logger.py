import datetime

LOG_FILE = "system_logs.txt"

def log_change(event):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.datetime.now()} - {event}\n")
