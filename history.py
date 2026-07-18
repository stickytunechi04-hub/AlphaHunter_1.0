import json
import os

FILE_NAME = "history.json"


def load_history():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def save_history(history):
    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)


def should_alert(address, score, volume, liquidity):
    history = load_history()

    if address not in history:
        history[address] = {
            "score": score,
            "volume": volume,
            "liquidity": liquidity
        }

        save_history(history)
        return True, "🆕 New coin discovered"

    old = history[address]

    reasons = []

    if score >= old["score"] + 15:
        reasons.append(f"⭐ Score increased ({old['score']} → {score})")

    if volume >= old["volume"] * 1.5:
        reasons.append("📈 Volume increased")

    if liquidity >= old["liquidity"] * 1.25:
        reasons.append("💧 Liquidity increased")

    history[address] = {
        "score": score,
        "volume": volume,
        "liquidity": liquidity
    }

    save_history(history)

    if reasons:
        return True, "\n".join(reasons)

    return False, ""