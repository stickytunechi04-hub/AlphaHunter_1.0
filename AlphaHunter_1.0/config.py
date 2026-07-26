"""
=========================================
AlphaHunter 1.0 Configuration
=========================================
"""

APP_NAME = "AlphaHunter"
VERSION = "1.0.0"

# APIs
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/search"

# Scanner Settings
MAX_PAIRS = 30
REQUEST_TIMEOUT = 10

# Filters
MIN_LIQUIDITY = 10000
MIN_VOLUME = 50000
MIN_MARKETCAP = 25000

# Scoring
MAX_SCORE = 100