from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

PRICE_COLUMNS: Tuple[str, ...] = ("Open", "High", "Low", "Close", "Volume")


def read_price_frame(path: str | Path) -> pd.DataFrame:
    """Read a CSV or XLSX price file used by the project."""

    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(file_path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)
    raise ValueError(f"Unsupported price file type: {file_path.suffix}")


def clean_price_frame(df: pd.DataFrame, columns: Iterable[str] = PRICE_COLUMNS) -> pd.DataFrame:
    """Convert comma-formatted price columns to numeric values and drop incomplete rows."""

    clean = df.copy()
    missing = [column for column in columns if column not in clean.columns]
    if missing:
        raise ValueError(f"Missing required price columns: {', '.join(missing)}")

    for column in columns:
        clean[column] = clean[column].astype(str).str.replace(",", "", regex=False)
        clean[column] = pd.to_numeric(clean[column], errors="coerce")

    clean = clean.dropna(subset=list(columns)).reset_index(drop=True)
    if clean.empty:
        raise ValueError("No usable rows remain after cleaning price data.")
    return clean


def split_train_validation(data: np.ndarray, train_fraction: float = 0.8) -> tuple[np.ndarray, np.ndarray]:
    """Split a time-ordered array without shuffling."""

    values = np.asarray(data)
    if values.ndim != 2:
        raise ValueError("Expected a two-dimensional feature array.")
    if not 0 < train_fraction < 1:
        raise ValueError("train_fraction must be between 0 and 1.")

    split_at = int(len(values) * train_fraction)
    if split_at == 0 or split_at == len(values):
        raise ValueError("train_fraction leaves an empty train or validation split.")
    return values[:split_at], values[split_at:]


def scale_train_test(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    columns: Iterable[str] = PRICE_COLUMNS,
) -> tuple[pd.DataFrame, pd.DataFrame, Dict[str, MinMaxScaler]]:
    """Fit MinMax scalers on training data and transform train/test frames."""

    train_scaled = train_df.copy()
    test_scaled = test_df.copy()
    scalers: Dict[str, MinMaxScaler] = {}

    for column in columns:
        if column not in train_scaled.columns or column not in test_scaled.columns:
            raise ValueError(f"Column {column!r} is required in both train and test data.")
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_scaled[column] = scaler.fit_transform(train_scaled[[column]])
        test_scaled[column] = scaler.transform(test_scaled[[column]])
        scalers[column] = scaler

    return train_scaled, test_scaled, scalers

