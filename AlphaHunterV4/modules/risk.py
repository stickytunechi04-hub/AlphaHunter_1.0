def risk_score(coin):

    risk = 0
    warnings = []

    if coin["liquidity"] < 30000:
        risk += 35
        warnings.append("⚠️ Low liquidity")

    if coin["volume"] < 50000:
        risk += 20
        warnings.append("⚠️ Low volume")

    if coin["m5"] < -10:
        risk += 25
        warnings.append("📉 Heavy 5m selloff")

    if coin["h1"] < -20:
        risk += 20
        warnings.append("🔻 Heavy 1h selloff")

    risk = min(risk, 100)

    return risk, warnings