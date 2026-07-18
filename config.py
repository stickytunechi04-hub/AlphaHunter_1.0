import os
from dotenv import load_dotenv

load_dotenv()

# ======================================
# Telegram
# ======================================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ======================================
# Scanner
# ======================================

SCAN_INTERVAL = 30

MIN_VOLUME = 100000
MIN_LIQUIDITY = 100000

SEARCH_TERMS = [
    "pump",
    "meme",
    "bonk",
    "pepe",
    "dog",
    "cat",
    "frog",
    "ai"
]

# ======================================
# Alpha Hunter
# ======================================

MAX_RESULTS = 25
MIN_CONFIDENCE = 70
CHAIN = "solana"