def hunter_brain(coin):

    score = coin["score"]
    momentum = coin["momentum"]
    risk = coin["risk"]

    age = coin.get("age_minutes")

    final_score = score + momentum - risk

    # Age penalty
    if age is None:
        pass
    elif age > 10080:          # 7 days
        final_score -= 40
    elif age > 1440:           # 1 day
        final_score -= 20
    elif age > 180:            # 3 hours
        final_score -= 10
    elif age > 30:             # 30 minutes
        final_score -= 5

    final_score = max(0, min(100, final_score))

    if final_score >= 90:
        verdict = "🚀 GEM"

    elif final_score >= 80:
        verdict = "🟢 STRONG BUY"

    elif final_score >= 65:
        verdict = "🟢 BUY"

    elif final_score >= 50:
        verdict = "🟡 WATCH"

    else:
        verdict = "🔴 PASS"

    return {
        "score": final_score,
        "verdict": verdict,
        "confidence": final_score,
        "risk": risk,
    }