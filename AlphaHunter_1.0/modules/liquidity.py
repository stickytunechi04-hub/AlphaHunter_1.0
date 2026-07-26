"""
==========================================
ALPHA HUNTER
LIQUIDITY ENGINE
==========================================
"""


class LiquidityEngine:

    @staticmethod
    def score(liquidity):

        if liquidity >= 500000:
            return 25

        elif liquidity >= 250000:
            return 22

        elif liquidity >= 100000:
            return 18

        elif liquidity >= 50000:
            return 14

        elif liquidity >= 25000:
            return 10

        elif liquidity >= 10000:
            return 6

        else:
            return 0