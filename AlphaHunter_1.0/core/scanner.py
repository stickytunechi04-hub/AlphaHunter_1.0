"""
==========================================
ALPHA HUNTER SCANNER
==========================================
"""

from api.api_manager import fetch_pairs

from core.analysis import normalize_pair
from core.filters import QualityFilter
from core.scoring import HunterScore
from core.engine import DecisionEngine
from core.ranking import RankingEngine

from modules.momentum import MomentumEngine
from modules.risk import RiskEngine
from modules.whale import WhaleEngine


class Scanner:

    def download(self):

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} pairs")

        print("\nFiltering market...\n")

        filter_engine = QualityFilter()
        hunter = HunterScore()
        momentum = MomentumEngine()
        risk = RiskEngine()
        whale = WhaleEngine()

        decision = DecisionEngine()
        ranking = RankingEngine()

        coins = []

        for pair in pairs:

            coin = normalize_pair(pair)

            passed, reasons = filter_engine.check(coin)

            if not passed:
                continue

            coin["hunter_score"] = hunter.calculate(coin)
            coin["momentum_score"] = momentum.score(coin)
            coin["risk_score"] = risk.score(coin)
            coin["whale_score"] = whale.score(coin)

            # Future Intelligence Engines
            coin["narrative_score"] = 0
            coin["wallet_score"] = 0
            coin["smart_money_score"] = 0
            coin["conviction_score"] = 0

            coin = decision.evaluate(coin)

            if len(coins) == 0:

                print("\n======================================================")
                print("FIRST ENRICHED COIN")
                print("======================================================\n")

                for key, value in coin.items():
                    print(f"{key:<20}: {value}")

                print()

            coins.append(coin)

        coins = ranking.rank(coins)

        print(f"Qualified {len(coins)} coins\n")

        print("=" * 98)
        print("TOP OPPORTUNITIES")
        print("=" * 98)

        for coin in coins[:10]:

            print(
                f"{coin['symbol']:<12}"
                f" Hunter:{coin['hunter_score']:>3}"
                f" Momentum:{coin['momentum_score']:>3}"
                f" Whale:{coin['whale_score']:>3}"
                f" Risk:{coin['risk_score']:>3}"
                f" Final:{coin['final_score']:>3}"
                f" Price:${coin['price']}"
            )