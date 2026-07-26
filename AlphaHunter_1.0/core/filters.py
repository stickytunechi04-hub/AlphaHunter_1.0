"""
=========================================
AlphaHunter Quality Filter
=========================================
"""


class QualityFilter:

    def check(self, coin):

        reasons = []

        # Liquidity
        if coin["liquidity"] < 10000:
            reasons.append("Low Liquidity")

        # Volume
        if coin["volume"] < 25000:
            reasons.append("Low Volume")

        # FDV
        if coin["fdv"] < 25000:
            reasons.append("Low FDV")

        if reasons:

            return False, reasons

        return True, []