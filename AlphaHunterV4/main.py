from scanner import scan


def main():

    coins = scan()

    print("\n==============================")
    print("TOP PICKS")
    print("==============================")

    if not coins:
        print("No coins found.")
        return

    for coin in coins[:10]:

        print(
            f"{coin['symbol']} | "
            f"Score: {coin['score']} | "
            f"{coin['decision']['verdict']} | "
            f"{coin['age_minutes']} min"
        )


if __name__ == "__main__":
    main()