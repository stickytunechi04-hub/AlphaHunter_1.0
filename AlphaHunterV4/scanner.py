import requests

from config import (
    SEARCH_TERMS,
    MIN_VOLUME,
    MIN_LIQUIDITY,
)

from filters import score_coin, rating
from modules.discovery import discover_pairs
from modules.pipeline import process_coin
from modules.history import seen_before, remember


def scan():

    print("=" * 60)
    print("🚀 Alpha Hunter V6.1")
    print("=" * 60)

    all_pairs = discover_pairs(SEARCH_TERMS)

    print(f"\nDownloaded {len(all_pairs)} pairs")

    coins = []
    seen = set()

    for pair in all_pairs:

        if pair.get("chainId") != "solana":
            continue

        base = pair.get("baseToken", {})
        address = base.get("address")

        if not address:
            continue

        # Skip duplicates during this scan
        if address in seen:
            continue

        # Skip coins already alerted before
        if seen_before(address):
            continue

        seen.add(address)

        volume = float(
            pair.get("volume", {}).get("h24", 0) or 0
        )

        liquidity = float(
            pair.get("liquidity", {}).get("usd", 0) or 0
        )

        if volume < MIN_VOLUME:
            continue

        if liquidity < MIN_LIQUIDITY:
            continue

        price_change = pair.get("priceChange", {})

        m5 = float(price_change.get("m5", 0) or 0)
        h1 = float(price_change.get("h1", 0) or 0)
        h24 = float(price_change.get("h24", 0) or 0)

        score, notes = score_coin(
            volume,
            liquidity,
            pair.get("dexId", ""),
            m5,
            h1,
            h24,
        )

        coin = {
            "address": address,
            "name": base.get("name", ""),
            "symbol": base.get("symbol", "").upper(),
            "price": pair.get("priceUsd", "0"),
            "volume": volume,
            "liquidity": liquidity,
            "dex": pair.get("dexId", ""),
            "m5": m5,
            "h1": h1,
            "h24": h24,
            "score": score,
            "rating": rating(score),
            "notes": notes,
        }

        try:
            coin = process_coin(coin, pair)

        except Exception as e:
            print(f"Pipeline Error ({coin['symbol']}): {e}")
            continue

        if coin["decision"]["verdict"] == "🔴 PASS":
            continue

        # Save to history
        remember(coin)

        coins.append(coin)

    coins.sort(
        key=lambda c: c["decision"]["score"],
        reverse=True,
    )

    print(f"\nQualified coins: {len(coins)}")

    return coins