def show_dashboard(results):

    print("\n" + "=" * 60)
    print("🦅 ALPHA HUNTER DASHBOARD")
    print("=" * 60)

    results = sorted(
        results,
        key=lambda x: x["decision"]["confidence"],
        reverse=True
    )

    for i, result in enumerate(results[:10], start=1):

        coin = result["coin"]
        decision = result["decision"]

        print(
            f"{i}. {coin['name']} ({coin['symbol']})"
        )

        print(
            f"   Confidence : {decision['confidence']}%"
        )

        print(
            f"   Risk       : {decision['risk']}%"
        )

        print(
            f"   Verdict    : {decision['verdict']}"
        )

        print()