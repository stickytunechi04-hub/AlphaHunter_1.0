"""
=========================================
AlphaHunter Decision Engine
=========================================
"""


class DecisionEngine:

    def evaluate(self, coin):

        hunter = coin.get("hunter_score", 0)

        # Future modules
        risk = coin.get("risk_score", 0)
        momentum = coin.get("momentum_score", 0)
        narrative = coin.get("narrative_score", 0)
        wallet = coin.get("wallet_score", 0)
        smart = coin.get("smart_money_score", 0)
        whale = coin.get("whale_score", 0)
        conviction = coin.get("conviction_score", 0)

        # Current version only uses Hunter Score.
        # Future versions will increase the weight of the
        # additional intelligence modules.

        final = hunter

        coin["final_score"] = round(final)

        return coin