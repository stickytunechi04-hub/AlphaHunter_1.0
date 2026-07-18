from config import SEARCH_TERMS


def main():
    print("=" * 60)
    print("🚀 Alpha Hunter v1")
    print("=" * 60)

    print("\nSearch Terms:")

    for term in SEARCH_TERMS:
        print("•", term)


if __name__ == "__main__":
    main()