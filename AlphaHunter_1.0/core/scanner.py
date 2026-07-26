"""
=========================================
AlphaHunter Scanner
=========================================
"""

from api.api_manager import fetch_pairs
from core.analysis import normalize_pair
from core.filters import QualityFilter


class Scanner:

    def download(self):

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} pairs")

        print("\nFiltering market...\n")

        filter_engine = QualityFilter()

        coins = []

        for pair in pairs:

            coin = normalize_pair(pair)

            passed, reasons = filter_engine.check(coin)

            if passed:
                coins.append(coin)

        print(f"Qualified {len(coins)} coins")

        if coins:

            print("\nFIRST QUALIFIED COIN\n")

            print(coins[0])