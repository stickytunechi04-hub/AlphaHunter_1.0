"""
=========================================
AlphaHunter DexScreener API
=========================================
"""

import requests

DISCOVERY_URL = "https://api.dexscreener.com/token-profiles/latest/v1"
MARKET_URL = "https://api.dexscreener.com/latest/dex/tokens/{}"


def latest_profiles():

    print("Loading DexScreener...")

    response = requests.get(DISCOVERY_URL, timeout=15)

    response.raise_for_status()

    profiles = response.json()

    print(f"Latest Profiles: {len(profiles)}")

    return profiles


def market_data(token_address):

    url = MARKET_URL.format(token_address)

    response = requests.get(url, timeout=15)

    response.raise_for_status()

    data = response.json()

    return data.get("pairs", [])