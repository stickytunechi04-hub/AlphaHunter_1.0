def confidence(coin):

    score = coin["score"]

    confidence = score

    reasons = []

    if coin["volume"] >= 500000:
        confidence += 5
        reasons.append("Strong volume")

    if coin["liquidity"] >= 250000:
        confidence += 5
        reasons.append("Healthy liquidity")

    if coin["m5"] > 5:
        confidence += 5
        reasons.append("5m momentum")

    if coin["h1"] > 15:
        confidence += 5
        reasons.append("1h momentum")

    confidence = min(confidence, 100)

    return {
        "confidence": confidence,
        "reasons": reasons
    }