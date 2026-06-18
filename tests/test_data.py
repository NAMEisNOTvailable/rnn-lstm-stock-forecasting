import numpy as np
import pandas as pd
import pytest

from rnn_lstm_stock_forecasting.data import clean_price_frame, scale_train_test, split_train_validation


def test_clean_price_frame_converts_comma_numbers_and_drops_bad_rows():
    frame = pd.DataFrame(
        {
            "Date": ["2026-01-01", "2026-01-02"],
            "Open": ["1,000.50", "bad"],
            "High": ["1,010", "2"],
            "Low": ["990", "1"],
            "Close": ["1,005.25", "1"],
            "Volume": ["3,500", "4,000"],
        }
    )

    clean = clean_price_frame(frame)

    assert len(clean) == 1
    assert clean.loc[0, "Open"] == pytest.approx(1000.50)
    assert clean.loc[0, "Volume"] == pytest.approx(3500.0)


def test_split_train_validation_preserves_time_order():
    values = np.arange(20, dtype=float).reshape(10, 2)

    train, validation = split_train_validation(values, train_fraction=0.7)

    assert train.shape == (7, 2)
    assert validation.shape == (3, 2)
    assert np.array_equal(train[-1], [12.0, 13.0])
    assert np.array_equal(validation[0], [14.0, 15.0])


def test_scale_train_test_fits_on_training_range_only():
    train = pd.DataFrame({"Open": [10, 20], "High": [10, 20], "Low": [10, 20], "Close": [10, 20], "Volume": [10, 20]})
    test = pd.DataFrame({"Open": [30], "High": [30], "Low": [30], "Close": [30], "Volume": [30]})

    train_scaled, test_scaled, scalers = scale_train_test(train, test)

    assert train_scaled["Close"].tolist() == [0.0, 1.0]
    assert test_scaled["Close"].tolist() == [2.0]
    assert "Close" in scalers

