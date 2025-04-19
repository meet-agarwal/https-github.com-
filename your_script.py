from datetime import datetime

with open("output.txt", "w") as f:
    f.write(f"Script ran at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
