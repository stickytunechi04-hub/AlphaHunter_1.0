import time


def get_launch_info(pair):

    pair_created = pair.get("pairCreatedAt", 0)

    if not pair_created:
        return {
            "age_minutes": None,
            "launch_note": "❓ Unknown",
        }

    age_minutes = (time.time() - pair_created / 1000) / 60

    if age_minutes < 30:
        note = "🔥 Fresh Launch"
    elif age_minutes < 180:
        note = "🟢 New Token"
    elif age_minutes < 1440:
        note = "🟡 Today's Launch"
    else:
        note = "⚪ Established"

    return {
        "age_minutes": round(age_minutes, 1),
        "launch_note": note,
    }