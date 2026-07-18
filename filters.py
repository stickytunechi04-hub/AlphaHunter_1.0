def score_coin(volume, liquidity, dex, m5, h1, h24):

    score = 0
    notes = []

    # -------------------
    # Liquidity (25 pts)
    # -------------------

    if liquidity >= 100000:
        score += 10
        notes.append("💧 Good liquidity")

    if liquidity >= 500000:
        score += 10
        notes.append("💧 Strong liquidity")

    if liquidity >= 2000000:
        score += 5
        notes.append("💧 Excellent liquidity")

    # -------------------
    # Volume (25 pts)
    # -------------------

    if volume >= 100000:
        score += 10
        notes.append("📈 Good volume")

    if volume >= 500000:
        score += 10
        notes.append("📈 Strong volume")

    if volume >= 2000000:
        score += 5
        notes.append("🚀 Massive volume")

    # -------------------
    # Momentum (35 pts)
    # -------------------

    if m5 > 5:
        score += 10
        notes.append("⚡ Strong 5m momentum")

    if h1 > 15:
        score += 10
        notes.append("🔥 Strong 1h momentum")

    if h24 > 50:
        score += 15
        notes.append("🚀 Explosive 24h trend")

    # -------------------
    # DEX (15 pts)
    # -------------------

    if dex.lower() in [
        "raydium",
        "orca",
        "meteora",
        "pumpswap"
    ]:
        score += 15
        notes.append("🏦 Trusted DEX")

    return score, notes


def rating(score):

    if score >= 90:
        return "🟢 EXCELLENT"

    elif score >= 75:
        return "🔥 HIGH POTENTIAL"

    elif score >= 60:
        return "👀 WATCHLIST"

    elif score >= 40:
        return "⚠️ SPECULATIVE"

    return "❌ IGNORE"