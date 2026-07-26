"""
=========================================
AlphaHunter Scanner
=========================================
"""

from api.api_manager import fetch_pairs

from core.analysis import normalize_pair
from core.filters import QualityFilter
from core.scoring import HunterScore


class Scanner:

    def download(self):

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} pairs")

        print("\nFiltering market...\n")

        filter_engine = QualityFilter()

        scorer = HunterScore()

        coins = []

        for pair in pairs:

            coin = normalize_pair(pair)

            passed, reasons = filter_engine.check(coin)

            if not passed:
                continue

            coin["hunter_score"] = scorer.calculate(coin)

            coins.append(coin)

        coins.sort(
            key=lambda x: x["hunter_score"],
            reverse=True
        )

        print(f"Qualified {len(coins)} coins\n")

        print("=" * 55)
        print("TOP OPPORTUNITIES")
        print("=" * 55)

        for coin in coins[:10]:

            print(
                f"{coin['symbol']:<10}"
                f" Score:{coin['hunter_score']:>3}"
                f"  Price:${coin['price']}"
            )