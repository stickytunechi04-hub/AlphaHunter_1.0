"""
==========================================
ALPHA HUNTER
AGE ENGINE
==========================================
"""

import time


class AgeEngine:

    @staticmethod
    def score(pair_created):

        if not pair_created:
            return 0

        now = int(time.time() * 1000)

        age_hours = (now - pair_created) / (1000 * 60 * 60)

        # Sweet spot for fresh launches

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

        else:
            return 2