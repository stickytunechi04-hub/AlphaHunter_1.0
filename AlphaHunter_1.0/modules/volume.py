"""
==========================================
ALPHA HUNTER
VOLUME ENGINE
==========================================
"""


class VolumeEngine:

    @staticmethod
    def score(volume):

        if volume >= 5000000:
            return 25

        elif volume >= 1000000:
            return 22

        elif volume >= 500000:
            return 18

        elif volume >= 250000:
            return 14

        elif volume >= 100000:
            return 10

        elif volume >= 50000:
            return 6

        else:
            return 0