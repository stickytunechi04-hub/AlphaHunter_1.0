"""
==========================================
ALPHA HUNTER
AGE ENGINE
==========================================
"""

import time


class AgeEngine:

    @staticmethod
    def score(coin):

        pair_created = coin["pair_created"]

        if not pair_created:
            return 0

        now = int(time.time() * 1000)

        age_hours = (now - pair_created) / (1000 * 60 * 60)

        if age_hours <= 1:
            return 25

        elif age_hours <= 6:
            return 22

        elif age_hours <= 24:
            return 18

        elif age_hours <= 72:
            return 12

        elif age_hours <= 168:
            return 6

        return 2