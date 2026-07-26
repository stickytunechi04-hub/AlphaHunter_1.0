"""
=========================================
AlphaHunter Ranking Engine
=========================================
"""


class RankingEngine:

    def rank(self, coins):

        return sorted(
            coins,
            key=lambda x: x["final_score"],
            reverse=True
        )