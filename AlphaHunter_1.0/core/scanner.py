"""
==========================================
ALPHA HUNTER SCANNER v2
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
from modules.smart_money import SmartMoneyEngine
from modules.narrative import NarrativeEngine


class Scanner:

    def download(self):

        print("\n==================================================")
        print("🚀 AlphaHunter v1.0.0")
        print("==================================================")

        print("\nDownloading market data...")

        pairs = fetch_pairs()

        print(f"Downloaded {len(pairs)} market pairs")

        print("\nFiltering market...\n")

        filter_engine = QualityFilter()

        hunter = HunterScore()
        momentum = MomentumEngine()
        whale = WhaleEngine()
        smart = SmartMoneyEngine()
        narrative = NarrativeEngine()
        risk = RiskEngine()

        decision = DecisionEngine()
        ranking = RankingEngine()

        coins = []
        seen = set()

        for pair in pairs:

            coin = normalize_pair(pair)

            ####################################
            # Remove duplicates
            ####################################

            address = coin.get("address", "")

            if address in seen:
                continue

            seen.add(address)

            ####################################
            # Filter
            ####################################

            passed, reasons = filter_engine.check(coin)

            if not passed:
                continue

            ####################################
            # Intelligence Engines
            ####################################

            coin["hunter_score"] = hunter.calculate(coin)

            coin["momentum_score"] = momentum.score(coin)

            coin["whale_score"] = whale.score(coin)

            coin["smart_money_score"] = smart.score(coin)

            coin["narrative_score"] = narrative.score(coin)

            coin["risk_score"] = risk.score(coin)

            ####################################
            # Future Engines
            ####################################

            coin["wallet_score"] = 0

            coin["conviction_score"] = 0

            ####################################
            # Final Decision
            ####################################

            coin = decision.evaluate(coin)

            ####################################
            # Print first enriched coin
            ####################################

            if len(coins) == 0:

                print("=" * 60)
                print("FIRST ENRICHED COIN")
                print("=" * 60)
                print()

                for key, value in coin.items():
                    print(f"{key:<20}: {value}")

                print()

            coins.append(coin)

        ####################################
        # Rank
        ####################################

        coins = ranking.rank(coins)

        print(f"Qualified {len(coins)} coins")

        print()

        print("=" * 170)
        print("TOP OPPORTUNITIES")
        print("=" * 170)

        for i, coin in enumerate(coins[:10], start=1):

            print(
                f"{i:>2}. "
                f"{coin['symbol']:<12}"
                f" Grade:{coin['grade']:<2}"
                f" Score:{coin['final_score']:>3}"
                f" Conf:{coin['confidence']:>3}%"
                f" Hunter:{coin['hunter_score']:>3}"
                f" Momentum:{coin['momentum_score']:>3}"
                f" Whale:{coin['whale_score']:>3}"
                f" Smart:{coin['smart_money_score']:>3}"
                f" Narrative:{coin['narrative_score']:>3}"
                f" Risk:{coin['risk_score']:>3}"
                f" Price:${coin['price']}"
            )

        print()
        print("=" * 170)