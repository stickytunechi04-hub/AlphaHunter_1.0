"""
=========================================
AlphaHunter Hunter Score Engine
=========================================
"""


class HunterScore:

    def calculate(self, coin):

        score = 0

        # ------------------------
        # Liquidity
        # ------------------------

        if coin["liquidity"] >= 100000:
            score += 25

        elif coin["liquidity"] >= 50000:
            score += 20

        elif coin["liquidity"] >= 25000:
            score += 15

        elif coin["liquidity"] >= 10000:
            score += 10

        # ------------------------
        # Volume
        # ------------------------

        if coin["volume"] >= 1000000:
            score += 25

        elif coin["volume"] >= 500000:
            score += 20

        elif coin["volume"] >= 100000:
            score += 15

        elif coin["volume"] >= 25000:
            score += 10

        # ------------------------
        # FDV
        # ------------------------

        if 50000 <= coin["fdv"] <= 500000:
            score += 25

        elif coin["fdv"] <= 1000000:
            score += 15

        else:
            score += 5

        # ------------------------
        # Final
        # ------------------------

        return min(score, 100)