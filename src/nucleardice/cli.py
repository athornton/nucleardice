#!/usr/bin/env python3
"""
CLI for the Nuclear Dice roller.  If we're only rolling it once, roll and
report the sum.  If we're rolling it multiple times, report statistics for
the rolls.
"""
import argparse
import random

from . import NuclearDice, NuclearDiceStatistics


def main() -> None:
    """Roll the dice.

    Create an argument parser, get our arguments, create an instance of
    NuclearDice and optionally a statistics instance for it, and roll the
    dice.
    """
    parser = argparse.ArgumentParser(description="Solve a Wordle puzzle")
    parser.add_argument(
        "dice", metavar="n", type=int, help="number of nuclear dice"
    )
    parser.add_argument("faces", metavar="x", type=int, help="faces per die")
    parser.add_argument(
        "-r",
        "--rolls",
        type=int,
        help="Number of times to roll the nuclear dice (default: 1)",
        default=1,
    )
    parser.add_argument(
        "-d", "--debug", help="debug", action="store_true", default=False
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Integer for random seed (for testing)",
        default=0,
    )
    args = parser.parse_args()
    if args.seed:
        random.seed(args.seed)
    if args.rolls == 1:
        nd = NuclearDice(args.dice, args.faces, debug=args.debug)
        nd.roll()
        print(nd.total)
    else:
        st = NuclearDiceStatistics(
            args.rolls, args.dice, args.faces, debug=args.debug
        )
        st.roll()
        st.report()


if __name__ == "__main__":
    main()
