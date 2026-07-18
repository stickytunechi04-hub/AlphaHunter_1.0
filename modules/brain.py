from modules.confidence import confidence
from modules.risk import risk


def hunter_brain(coin):

    conf = confidence(coin)
    danger = risk(coin)

    confidence_score = conf["confidence"]
    risk_score = danger["risk"]

    if confidence_score >= 90 and risk_score <= 25:
        verdict = "🟢 STRONG WATCH"

    elif confidence_score >= 80 and risk_score <= 40:
        verdict = "🟡 WATCH"

    else:
        verdict = "🔴 PASS"

    return {
        "confidence": confidence_score,
        "risk": risk_score,
        "verdict": verdict,
        "reasons": conf["reasons"],
        "warnings": danger["warnings"]
    }