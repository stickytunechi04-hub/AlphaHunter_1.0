def score_coin(volume, liquidity, dex, m5, h1, h24):

    score = 0
    notes = []

    if liquidity > 10000:
        score += 10
        notes.append("💧 Good liquidity")

    if liquidity > 50000:
        score += 10
        notes.append("💧 Strong liquidity")

    if liquidity > 250000:
        score += 10
        notes.append("💧 Excellent liquidity")

    if volume > 10000:
        score += 10
        notes.append("📈 Good volume")

    if volume > 100000:
        score += 10
        notes.append("📈 Strong volume")

    if dex.lower() in ["raydium", "pumpswap", "orca"]:
        score += 10
        notes.append("🏦 Trusted DEX")

    return score, notes


def rating(score):

    if score >= 80:
        return "🟢 ELITE"

    if score >= 60:
        return "🔥 STRONG"

    if score >= 40:
        return "👀 WATCHLIST"

    return "⚠️ SPECULATIVE"