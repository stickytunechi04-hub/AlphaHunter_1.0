"""
==========================================
ALPHA HUNTER
SMART MONEY ENGINE
==========================================
"""


class SmartMoneyEngine:

    @staticmethod
    def score(coin):

        score = 0

        buys = coin.get("buys_1h", 0)
        sells = coin.get("sells_1h", 0)

        liquidity = coin.get("liquidity", 0)
        volume = coin.get("volume", 0)
        market_cap = coin.get("market_cap", 1)

        # Buyer dominance
        if buys > sells * 3:
            score += 10

        elif buys > sells * 2:
            score += 7

        elif buys > sells:
            score += 4

        # Healthy liquidity
        if liquidity >= 50000:
            score += 5

        # Volume compared to market cap
        if market_cap > 0:

            ratio = volume / market_cap

            if ratio >= 2:
                score += 10

            elif ratio >= 1:
                score += 6

            elif ratio >= 0.5:
                score += 3

        return min(score, 20)