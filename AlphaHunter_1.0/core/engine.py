"""
==========================================
ALPHA HUNTER
DECISION ENGINE
==========================================
"""


class DecisionEngine:

    def evaluate(self, coin):

        final = (
            coin["hunter_score"]
            + coin["momentum_score"]
            - coin["risk_score"]
        )

        final = max(0, min(final, 100))

        coin["final_score"] = final

        return coin