"""
=========================================
AlphaHunter Scanner
=========================================
"""

from api.api_manager import fetch_pairs

from core.analysis import normalize_pair
from core.filters import QualityFilter
from core.scoring import HunterScore
from core.engine import DecisionEngine
from core.ranking import RankingEngine


class Scanner:

    def download(self):

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} pairs")

        print("\nFiltering market...\n")

        filter_engine = QualityFilter()
        hunter = HunterScore()
        decision = DecisionEngine()
        ranking = RankingEngine()

        coins = []

        for pair in pairs:

            coin = normalize_pair(pair)

            passed, reasons = filter_engine.check(coin)

            if not passed:
                continue

            coin["hunter_score"] = hunter.calculate(coin)

            # Reserved for future engines
            coin["risk_score"] = 0
            coin["momentum_score"] = 0
            coin["narrative_score"] = 0
            coin["wallet_score"] = 0
            coin["smart_money_score"] = 0
            coin["whale_score"] = 0
            coin["conviction_score"] = 0

            coin = decision.evaluate(coin)

            coins.append(coin)

        coins = ranking.rank(coins)

        print(f"Qualified {len(coins)} coins\n")

        print("=" * 70)
        print("TOP OPPORTUNITIES")
        print("=" * 70)

        for coin in coins[:10]:

            print(
                f"{coin['symbol']:<12}"
                f" Hunter:{coin['hunter_score']:>3}"
                f" Final:{coin['final_score']:>3}"
                f" Price:${coin['price']}"
            )