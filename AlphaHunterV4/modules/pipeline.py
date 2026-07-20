from modules.launcher import get_launch_info
from modules.momentum import momentum_score
from modules.risk import risk_score
from modules.brain import hunter_brain


def process_coin(coin, pair):

    # Launch info
    launch = get_launch_info(pair)
    coin.update(launch)

    # Momentum
    momentum, momentum_notes = momentum_score(coin)
    coin["momentum"] = momentum

    # Risk
    risk, risk_notes = risk_score(coin)
    coin["risk"] = risk

    # Merge notes
    coin["notes"].extend(momentum_notes)
    coin["notes"].extend(risk_notes)

    # Final AI decision
    coin["decision"] = hunter_brain(coin)

    return coin