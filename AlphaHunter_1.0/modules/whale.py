"""
==========================================
ALPHA HUNTER
WHALE ENGINE
==========================================
"""


class WhaleEngine:

    @staticmethod
    def score(coin):

        score = 0

        buys = coin.get("buys_1h", 0)
        sells = coin.get("sells_1h", 0)
        volume = coin.get("volume", 0)
        liquidity = coin.get("liquidity", 0)

        # Strong buy dominance
        if buys > sells * 2:
            score += 10
        elif buys > sells:
            score += 5

        # High trading volume
        if volume > 500000:
            score += 5
        elif volume > 250000:
            score += 3

        # Healthy liquidity
        if liquidity > 50000:
            score += 5
        elif liquidity > 25000:
            score += 2

        return min(score, 20)