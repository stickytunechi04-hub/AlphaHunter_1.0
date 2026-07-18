from modules.brain import hunter_brain


def process_coin(coin):

    decision = hunter_brain(coin)

    return {
        "coin": coin,
        "decision": decision
    }