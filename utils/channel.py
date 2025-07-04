from pathlib import Path

# Fayl manzili
CHANNEL_FILE = Path("data/channel.txt")

# Kanal linkini saqlash
def save_channel_link(link: str):
    CHANNEL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with CHANNEL_FILE.open("w", encoding="utf-8") as f:
        f.write(link.strip())

# Kanal linkini o‘qish
def get_channel_link() -> str:
    if CHANNEL_FILE.exists():
        with CHANNEL_FILE.open("r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# Kanalni o‘chirish
def remove_channel_link():
    if CHANNEL_FILE.exists():
        CHANNEL_FILE.unlink()
