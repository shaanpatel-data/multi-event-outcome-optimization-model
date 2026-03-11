#!/usr/bin/env python
"""
Generate parlay combinations using the ParlayOptimizer.

This script loads model probabilities from an input CSV file, constructs multi-leg combinations,
and outputs the top parlays ranked by expected value. It serves as a command-line entry point
for research and analysis, not for wagering.

Usage:
    python scripts/generate_parlay.py --input probabilities.csv --max_legs 3 --top_n 10
"""

import argparse
import pandas as pd

from src.optimizer.multi_leg_optimizer import ParlayOptimizer


def main() -> None:
    """Parse arguments and generate parlays."""
    parser = argparse.ArgumentParser(
        description="Generate parlay combinations and compute expected value."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help=(
            "Path to a CSV file containing model probabilities with columns "
            "['event_id', 'market', 'selection', 'probability', 'odds']"
        ),
    )
    parser.add_argument(
        "--max_legs",
        type=int,
        default=3,
        help="Maximum number of legs per parlay",
    )
    parser.add_argument(
        "--top_n", type=int, default=10, help="Number of top parlays to display"
    )
    args = parser.parse_args()

    # Load probabilities
    df = pd.read_csv(args.input)
    outcomes = df.to_dict("records")

    optimizer = ParlayOptimizer(outcomes, max_legs=args.max_legs)
    parlays = optimizer.filter_combinations()

    # Sort parlays by expected value
    sorted_parlays = sorted(parlays, key=lambda x: x["ev"], reverse=True)

    for parlay in sorted_parlays[: args.top_n]:
        print(f"Parlay EV: {parlay['ev']:.4f}, Legs: {len(parlay['legs'])}")
        for leg in parlay["legs"]:
            print(
                f"  {leg['event_id']} - {leg['market']} - {leg['selection']} | "
                f"Prob: {leg['probability']:.3f} | Odds: {leg['odds']}"
            )
        print()


if __name__ == "__main__":
    main()
