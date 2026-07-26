"""
==========================================
ALPHA HUNTER
DECISION ENGINE v3
==========================================
"""


class DecisionEngine:

    def evaluate(self, coin):

        ########################################
        # Weighted Final Score
        ########################################

        final = (
            coin["hunter_score"]
            + (coin["momentum_score"] * 0.40)
            + (coin["whale_score"] * 0.30)
            + (coin["smart_money_score"] * 0.30)
            + (coin["narrative_score"] * 0.30)
            - (coin["risk_score"] * 0.50)
        )

        final = round(final)

        final = max(0, min(final, 100))

        coin["final_score"] = final

        ########################################
        # Confidence
        ########################################

        confidence = round(
            (
                final
                + coin["hunter_score"]
            ) / 2
        )

        confidence = max(0, min(confidence, 100))

        coin["confidence"] = confidence

        ########################################
        # Grade
        ########################################

        if final >= 95:
            grade = "S+"

        elif final >= 90:
            grade = "S"

        elif final >= 85:
            grade = "A+"

        elif final >= 80:
            grade = "A"

        elif final >= 75:
            grade = "B+"

        elif final >= 70:
            grade = "B"

        elif final >= 60:
            grade = "C"

        elif final >= 50:
            grade = "D"

        else:
            grade = "F"

        coin["grade"] = grade

        ########################################
        # Verdict
        ########################################

        if final >= 95:
            verdict = "💎 ELITE GEM"

        elif final >= 90:
            verdict = "🔥 ALPHA CANDIDATE"

        elif final >= 80:
            verdict = "🚀 STRONG BUY"

        elif final >= 70:
            verdict = "👀 WATCHLIST"

        elif final >= 60:
            verdict = "⚠ SPECULATIVE"

        else:
            verdict = "❌ AVOID"

        coin["verdict"] = verdict

        return coin