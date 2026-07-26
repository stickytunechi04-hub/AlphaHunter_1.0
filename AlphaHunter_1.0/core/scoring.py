"""
==========================================
ALPHA HUNTER
HUNTER SCORE ENGINE
==========================================
"""

from modules.liquidity import LiquidityEngine
from modules.volume import VolumeEngine
from modules.fdv import FDVEngine
from modules.age import AgeEngine


class HunterScore:

    def calculate(self, coin):

        liquidity_score = LiquidityEngine.score(coin)
        volume_score = VolumeEngine.score(coin)
        fdv_score = FDVEngine.score(coin)
        age_score = AgeEngine.score(coin)

        total = (
            liquidity_score
            + volume_score
            + fdv_score
            + age_score
        )

        coin["liquidity_score"] = liquidity_score
        coin["volume_score"] = volume_score
        coin["fdv_score"] = fdv_score
        coin["age_score"] = age_score

        return min(total, 100)