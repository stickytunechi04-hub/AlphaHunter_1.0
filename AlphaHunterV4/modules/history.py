import json
import os

FILE = "data/history.json"


def load_history():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)


def save_history(history):

    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)


def seen_before(address):

    history = load_history()

    return address in history


def remember(coin):

    history = load_history()

    history[coin["address"]] = {
        "symbol": coin["symbol"],
        "score": coin["decision"]["score"],
        "age": coin["age_minutes"],
    }

    save_history(history)