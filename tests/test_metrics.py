import math

import pytest

from rnn_lstm_stock_forecasting.metrics import evaluate_forecast, mase, rmse, rmsle, smape


def test_forecast_metrics_match_simple_expected_values():
    actual = [100.0, 110.0, 120.0]
    forecast = [100.0, 100.0, 130.0]
    train = [80.0, 90.0, 100.0]

    assert rmse(actual, forecast) == pytest.approx(math.sqrt(200 / 3))
    assert smape(actual, forecast) == pytest.approx(100 * ((0.0 + 20 / 210 + 20 / 250) / 3))
    assert mase(actual, forecast, train) == pytest.approx((0 + 10 + 10) / 3 / 10)
    assert rmsle(actual, forecast) > 0


def test_evaluate_forecast_returns_named_metrics():
    metrics = evaluate_forecast([2, 3], [2, 4], [1, 2, 3])

    assert set(metrics) == {"rmse", "smape", "mase", "rmsle"}


def test_mase_rejects_flat_training_series():
    with pytest.raises(ValueError, match="undefined"):
        mase([2, 3], [2, 4], [1, 1, 1])

