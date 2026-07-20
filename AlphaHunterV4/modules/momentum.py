def momentum_score(coin):

    score = 0
    reasons = []

    if coin["m5"] > 5:
        score += 25
        reasons.append("🔥 Strong 5m")

    if coin["h1"] > 15:
        score += 25
        reasons.append("🚀 Strong 1h")

    if coin["volume"] > 100000:
        score += 20
        reasons.append("📈 High volume")

    if coin["liquidity"] > 50000:
        score += 20
        reasons.append("💧 Good liquidity")

    if coin["h24"] > 30:
        score += 10
        reasons.append("🌙 24h breakout")

    return score, reasons