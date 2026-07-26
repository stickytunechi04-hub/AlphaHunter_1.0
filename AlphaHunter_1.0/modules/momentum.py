"""
==========================================
ALPHA HUNTER
MOMENTUM ENGINE
==========================================
"""


class MomentumEngine:

    @staticmethod
    def score(coin):

        score = 0

        # 5 minute momentum
        if coin["price_change_5m"] >= 20:
            score += 8
        elif coin["price_change_5m"] >= 10:
            score += 5

        # 1 hour momentum
        if coin["price_change_1h"] >= 100:
            score += 8
        elif coin["price_change_1h"] >= 50:
            score += 5

        # Buy pressure
        if coin["buys_5m"] > coin["sells_5m"]:
            score += 5

        # Dex boost
        if coin["boosts"] > 0:
            score += 4

        return min(score, 25)