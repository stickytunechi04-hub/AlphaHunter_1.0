"""
==========================================
ALPHA HUNTER
NORMALIZATION ENGINE
==========================================
"""


def normalize_pair(pair):

    base = pair.get("baseToken", {})

    liquidity = pair.get("liquidity", {})

    volume = pair.get("volume", {})

    price_change = pair.get("priceChange", {})

    txns = pair.get("txns", {})

    m5 = txns.get("m5", {})

    h1 = txns.get("h1", {})

    boosts = pair.get("boosts", {})

    return {

        # Identity
        "address": base.get("address", ""),
        "symbol": base.get("symbol", ""),
        "name": base.get("name", ""),

        # Price
        "price": float(pair.get("priceUsd") or 0),

        # Market
        "liquidity": liquidity.get("usd", 0),
        "volume": volume.get("h24", 0),
        "fdv": pair.get("fdv", 0),
        "market_cap": pair.get("marketCap", 0),

        # Age
        "pair_created": pair.get("pairCreatedAt", 0),

        # Price movement
        "price_change_5m": price_change.get("m5", 0),
        "price_change_1h": price_change.get("h1", 0),
        "price_change_24h": price_change.get("h24", 0),

        # Transactions
        "buys_5m": m5.get("buys", 0),
        "sells_5m": m5.get("sells", 0),

        "buys_1h": h1.get("buys", 0),
        "sells_1h": h1.get("sells", 0),

        # Dex boosts
        "boosts": boosts.get("active", 0),

        # Link
        "url": pair.get("url", "")
    }