from __future__ import annotations

import math
from typing import Dict

import numpy as np


def _as_1d_float(values: np.ndarray | list[float]) -> np.ndarray:
    array = np.asarray(values, dtype=float).reshape(-1)
    if array.size == 0:
        raise ValueError("Metric input must not be empty.")
    return array


def _paired_arrays(y_true: np.ndarray | list[float], y_pred: np.ndarray | list[float]) -> tuple[np.ndarray, np.ndarray]:
    actual = _as_1d_float(y_true)
    forecast = _as_1d_float(y_pred)
    if actual.shape != forecast.shape:
        raise ValueError("y_true and y_pred must have the same shape.")
    return actual, forecast


def rmse(y_true: np.ndarray | list[float], y_pred: np.ndarray | list[float]) -> float:
    actual, forecast = _paired_arrays(y_true, y_pred)
    return float(math.sqrt(np.mean(np.square(actual - forecast))))


def smape(y_true: np.ndarray | list[float], y_pred: np.ndarray | list[float]) -> float:
    actual, forecast = _paired_arrays(y_true, y_pred)
    denominator = np.abs(actual) + np.abs(forecast)
    terms = np.zeros_like(actual, dtype=float)
    np.divide(2 * np.abs(forecast - actual), denominator, out=terms, where=denominator != 0)
    return float(100 * np.mean(terms))


def mase(
    y_true: np.ndarray | list[float],
    y_pred: np.ndarray | list[float],
    y_train: np.ndarray | list[float],
) -> float:
    actual, forecast = _paired_arrays(y_true, y_pred)
    train = _as_1d_float(y_train)
    if train.size < 2:
        raise ValueError("y_train must contain at least two values for MASE.")

    scale = np.mean(np.abs(np.diff(train)))
    if scale == 0:
        raise ValueError("MASE is undefined when the in-sample naive error is zero.")
    return float(np.mean(np.abs(actual - forecast)) / scale)


def rmsle(y_true: np.ndarray | list[float], y_pred: np.ndarray | list[float]) -> float:
    actual, forecast = _paired_arrays(y_true, y_pred)
    if np.any(actual < 0) or np.any(forecast < 0):
        raise ValueError("RMSLE requires non-negative values.")
    return float(math.sqrt(np.mean(np.square(np.log1p(forecast) - np.log1p(actual)))))


def evaluate_forecast(
    y_true: np.ndarray | list[float],
    y_pred: np.ndarray | list[float],
    y_train: np.ndarray | list[float],
) -> Dict[str, float]:
    return {
        "rmse": rmse(y_true, y_pred),
        "smape": smape(y_true, y_pred),
        "mase": mase(y_true, y_pred, y_train),
        "rmsle": rmsle(y_true, y_pred),
    }

