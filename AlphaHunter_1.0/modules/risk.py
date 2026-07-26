"""
==========================================
ALPHA HUNTER
RISK ENGINE
==========================================
"""


class RiskEngine:

    @staticmethod
    def score(coin):

        risk = 0

        # Very low liquidity
        if coin["liquidity"] < 15000:
            risk += 10

        elif coin["liquidity"] < 25000:
            risk += 5

        # Sell pressure
        if coin["sells_5m"] > coin["buys_5m"]:
            risk += 5

        # Huge pump
        if coin["price_change_5m"] > 100:
            risk += 5

        # Overvalued
        if coin["fdv"] > 1000000:
            risk += 5

        return min(risk, 25)