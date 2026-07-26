"""
=========================================
AlphaHunter API Manager
=========================================
"""

from api.dexscreener import latest_profiles, market_data


def fetch_pairs():

    profiles = latest_profiles()

    all_pairs = []

    for profile in profiles:

        address = profile.get("tokenAddress")

        if not address:
            continue

        try:

            pairs = market_data(address)

            if pairs:
                all_pairs.extend(pairs)

        except Exception:
            continue

    print(f"Downloaded {len(all_pairs)} market pairs")

    return all_pairs