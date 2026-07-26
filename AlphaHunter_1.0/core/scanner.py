"""
=========================================
AlphaHunter Scanner
=========================================
"""

import json

from api.api_manager import fetch_pairs
from core.analysis import normalize_pair


class Scanner:

    def download(self):

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} pairs")

        print("\nNormalizing data...\n")

        coins = []

        for pair in pairs:
            coin = normalize_pair(pair)
            coins.append(coin)

        print(f"Normalized {len(coins)} coins")

        if pairs:

            print("\nFIRST RAW API OBJECT\n")

            print(json.dumps(pairs[0], indent=4))