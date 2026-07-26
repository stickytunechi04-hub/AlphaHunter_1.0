"""
==========================================
ALPHA HUNTER
NARRATIVE ENGINE
==========================================
"""


class NarrativeEngine:

    @staticmethod
    def score(coin):

        score = 0

        # Website
        if coin.get("website"):
            score += 3

        # Twitter/X
        if coin.get("twitter"):
            score += 5

        # Telegram
        if coin.get("telegram"):
            score += 5

        # Token image
        if coin.get("image"):
            score += 2

        # Paid boosts
        boosts = coin.get("boosts", 0)

        if boosts > 0:
            score += 5

        return min(score, 20)