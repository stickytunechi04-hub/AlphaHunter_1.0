"""
=========================================
AlphaHunter Data Normalizer
=========================================
"""


def normalize_pair(pair):
    """
    Converts a DexScreener pair into the AlphaHunter format.
    """

    base = pair.get("baseToken", {})

    liquidity = pair.get("liquidity", {})

    volume = pair.get("volume", {})

    coin = {

        "address": base.get("address", ""),

        "symbol": base.get("symbol", ""),

        "name": base.get("name", ""),

        "price": float(pair.get("priceUsd") or 0),

        "liquidity": float(liquidity.get("usd") or 0),

        "volume": float(volume.get("h24") or 0),

        "fdv": float(pair.get("fdv") or 0),

        "market_cap": float(pair.get("marketCap") or 0),

        "pair_created": pair.get("pairCreatedAt", 0),

        "url": pair.get("url", "")
    }

    return coin