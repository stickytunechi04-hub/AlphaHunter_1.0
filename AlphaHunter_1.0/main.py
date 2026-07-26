"""
=========================================
AlphaHunter v1.0.0
=========================================
"""

from core.scanner import Scanner


def main():

    print("=" * 50)
    print("🚀 AlphaHunter v1.0.0")
    print("=" * 50)

    scanner = Scanner()

    scanner.download()


if __name__ == "__main__":
    main()