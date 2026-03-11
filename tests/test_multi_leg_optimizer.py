"""
test_multi_leg_optimizer.py

Unit tests for ParlayOptimizer class to ensure correct expected value calculation and multi‑leg combination generation.
"""

import pandas as pd
import pytest

from src.optimizer.multi_leg_optimizer import ParlayOptimizer


def test_expected_value_calculation():
    """Test EV calculation and parlay generation on a small dataset."""
    # Example small dataset
    data = pd.DataFrame({
        "selection_id": [1, 2],
        "prob": [0.6, 0.5],
        "odds": [120, 100],
        "event_id": ["A", "B"],
    })
    optimizer = ParlayOptimizer(max_legs=2, min_ev=0.0)
    parlays = optimizer.optimize_parlays(data)
    # There should be at least one parlay
    assert len(parlays) > 0
    # Each parlay EV should be computed as a float and non‑negative
    for p in parlays:
        assert isinstance(p["expected_value"], float)
        assert p["expected_value"] >= 0


def test_exclude_same_game():
    """Test that same game selections are excluded from parlay generation."""
    data = pd.DataFrame({
        "selection_id": [1, 2],
        "prob": [0.6, 0.4],
        "odds": [120, 110],
        "event_id": ["A", "A"],
    })
    optimizer = ParlayOptimizer(max_legs=2, min_ev=0.0)
    parlays = optimizer.optimize_parlays(data)
    # Should be zero because both selections belong to the same event
    assert len(parlays) == 0
