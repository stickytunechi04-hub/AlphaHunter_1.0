def show_dashboard(coins):

    print("\n" + "=" * 60)
    print("🔥 ALPHA HUNTER DASHBOARD")
    print("=" * 60)

    for i, coin in enumerate(coins[:10], start=1):

        print(
            f"{i:2}. "
            f"{coin['name']} "
            f"({coin['symbol']})"
        )

        print(
            f"    Score: {coin['score']}/100"
        )

        print(
            f"    Volume: ${coin['volume']:,.0f}"
        )

        print(
            f"    Liquidity: ${coin['liquidity']:,.0f}"
        )

        print()