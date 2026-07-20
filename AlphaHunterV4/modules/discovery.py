import requests


def discover_pairs(search_terms):

    pairs = []

    for term in search_terms:

        try:
            response = requests.get(
                f"https://api.dexscreener.com/latest/dex/search?q={term}",
                timeout=10,
            )

            if response.status_code == 200:
                pairs.extend(response.json().get("pairs", []))

        except Exception as e:
            print(f"Discovery error: {e}")

    return pairs