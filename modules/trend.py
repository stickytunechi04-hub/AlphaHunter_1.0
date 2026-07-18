def trend_score(coin):

    score = 0
    reasons = []

    # Strong short-term momentum
    if coin["m5"] > 5:
        score += 20
        reasons.append("Strong 5m momentum")

    # Sustained momentum
    if coin["h1"] > 15:
        score += 20
        reasons.append("Strong 1h momentum")

    # Healthy daily trend
    if coin["h24"] > 30:
        score += 20
        reasons.append("Strong 24h trend")

    # Good trading activity
    if coin["volume"] >= 500000:
        score += 20
        reasons.append("High trading volume")

    # Healthy liquidity
    if coin["liquidity"] >= 250000:
        score += 20
        reasons.append("Healthy liquidity")

    score = min(score, 100)

    return {
        "trend": score,
        "reasons": reasons
    }