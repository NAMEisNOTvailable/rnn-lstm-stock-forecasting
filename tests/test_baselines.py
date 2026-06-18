import pandas as pd
import pytest

from rnn_lstm_stock_forecasting.baselines import evaluate_persistence_baseline, persistence_forecast


def test_persistence_forecast_uses_previous_observed_close():
    forecast = persistence_forecast([8.0, 9.0, 10.0], [11.0, 12.0, 13.0])

    assert forecast.tolist() == [10.0, 11.0, 12.0]


def test_evaluate_persistence_baseline_returns_reviewer_metrics():
    train = pd.DataFrame({"Close": [8.0, 9.0, 10.0]})
    test = pd.DataFrame({"Close": [11.0, 12.0]})

    row = evaluate_persistence_baseline("Demo", train, test)

    assert row["asset"] == "Demo"
    assert row["model"] == "persistence_baseline"
    assert row["test_rows"] == 2
    assert row["mase"] == pytest.approx(1.0)

