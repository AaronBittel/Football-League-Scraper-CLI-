#!/usr/bin/env python3
"""Entry point"""

from bundesliga_scraper import user_input_parser


def main() -> None:
    """Main method"""
    print("Welcome to Bundesliga-Scraper!")

    parser = user_input_parser.create_parser()
    user_input_parser.parse_user_args(parser)


if __name__ == "__main__":
    main()
