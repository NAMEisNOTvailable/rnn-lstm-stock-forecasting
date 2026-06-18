from __future__ import annotations

import numpy as np


def create_sequences(data: np.ndarray, window_size: int, target_index: int) -> tuple[np.ndarray, np.ndarray]:
    """Create rolling supervised-learning windows for sequence forecasting."""

    values = np.asarray(data, dtype=float)
    if values.ndim != 2:
        raise ValueError("Expected a two-dimensional feature array.")
    if window_size <= 0:
        raise ValueError("window_size must be positive.")
    if target_index < 0 or target_index >= values.shape[1]:
        raise ValueError("target_index is outside the feature array.")
    if len(values) <= window_size:
        raise ValueError("Need more rows than window_size to create sequences.")

    x_values = []
    y_values = []
    for row_index in range(window_size, len(values)):
        x_values.append(values[row_index - window_size : row_index, :])
        y_values.append(values[row_index, target_index])
    return np.asarray(x_values, dtype=float), np.asarray(y_values, dtype=float)


def prepare_test_sequences(train_data: np.ndarray, test_data: np.ndarray, window_size: int) -> np.ndarray:
    """Build test windows by prepending the last training window to the test period."""

    train_values = np.asarray(train_data, dtype=float)
    test_values = np.asarray(test_data, dtype=float)
    if train_values.ndim != 2 or test_values.ndim != 2:
        raise ValueError("Expected two-dimensional train and test feature arrays.")
    if train_values.shape[1] != test_values.shape[1]:
        raise ValueError("Train and test arrays must have the same feature count.")
    if window_size <= 0:
        raise ValueError("window_size must be positive.")
    if len(train_values) < window_size:
        raise ValueError("Training data must contain at least window_size rows.")
    if len(test_values) == 0:
        raise ValueError("Test data must not be empty.")

    combined = np.concatenate((train_values, test_values), axis=0)
    start = len(train_values) - window_size
    end = len(train_values) + len(test_values)
    inputs = combined[start:end]

    windows = []
    for row_index in range(window_size, len(inputs)):
        windows.append(inputs[row_index - window_size : row_index, :])
    return np.asarray(windows, dtype=float)

