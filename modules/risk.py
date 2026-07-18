def risk(coin):

    score = 0
    warnings = []

    if coin["liquidity"] < 150000:
        score += 25
        warnings.append("Low liquidity")

    if coin["volume"] < 200000:
        score += 15
        warnings.append("Weak volume")

    if abs(coin["m5"]) > 30:
        score += 20
        warnings.append("Extreme volatility")

    if abs(coin["h1"]) > 80:
        score += 20
        warnings.append("Parabolic movement")

    score = min(score, 100)

    return {
        "risk": score,
        "warnings": warnings
    }