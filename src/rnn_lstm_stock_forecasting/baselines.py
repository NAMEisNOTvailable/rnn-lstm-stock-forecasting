from __future__ import annotations

from typing import Dict

import numpy as np
import pandas as pd

from .metrics import evaluate_forecast


def persistence_forecast(train_close: np.ndarray | list[float], test_close: np.ndarray | list[float]) -> np.ndarray:
    """Forecast each test close with the most recent observed close."""

    train = np.asarray(train_close, dtype=float).reshape(-1)
    test = np.asarray(test_close, dtype=float).reshape(-1)
    if train.size == 0:
        raise ValueError("train_close must not be empty.")
    if test.size == 0:
        raise ValueError("test_close must not be empty.")

    return np.concatenate(([train[-1]], test[:-1]))


def evaluate_persistence_baseline(
    asset: str,
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    close_column: str = "Close",
) -> Dict[str, float | str | int]:
    """Evaluate a one-step persistence baseline for reviewer comparison."""

    if close_column not in train_df.columns or close_column not in test_df.columns:
        raise ValueError(f"Column {close_column!r} is required in train and test data.")

    train_close = train_df[close_column].to_numpy(dtype=float)
    test_close = test_df[close_column].to_numpy(dtype=float)
    forecast = persistence_forecast(train_close, test_close)
    metrics = evaluate_forecast(test_close, forecast, train_close)

    return {
        "asset": asset,
        "model": "persistence_baseline",
        "test_rows": int(test_close.size),
        **metrics,
    }

