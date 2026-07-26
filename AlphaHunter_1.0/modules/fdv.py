"""
==========================================
ALPHA HUNTER
FDV ENGINE
==========================================
"""


class FDVEngine:

    @staticmethod
    def score(fdv):

        # Sweet spot for meme coins
        if 50000 <= fdv <= 250000:
            return 25

        elif 250000 < fdv <= 500000:
            return 20

        elif 25000 <= fdv < 50000:
            return 15

        elif 500000 < fdv <= 1000000:
            return 10

        elif 1000000 < fdv <= 5000000:
            return 5

        else:
            return 0