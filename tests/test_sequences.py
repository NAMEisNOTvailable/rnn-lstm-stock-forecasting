import numpy as np
import pytest

from rnn_lstm_stock_forecasting.sequences import create_sequences, prepare_test_sequences


def test_create_sequences_builds_rolling_windows_and_close_targets():
    values = np.arange(20, dtype=float).reshape(5, 4)

    x_values, y_values = create_sequences(values, window_size=2, target_index=3)

    assert x_values.shape == (3, 2, 4)
    assert y_values.tolist() == [11.0, 15.0, 19.0]
    assert np.array_equal(x_values[0], values[0:2])


def test_prepare_test_sequences_uses_last_training_window():
    train = np.arange(24, dtype=float).reshape(6, 4)
    test = np.arange(24, 36, dtype=float).reshape(3, 4)

    windows = prepare_test_sequences(train, test, window_size=2)

    assert windows.shape == (3, 2, 4)
    assert np.array_equal(windows[0], train[-2:])
    assert np.array_equal(windows[1], np.vstack([train[-1], test[0]]))


def test_create_sequences_rejects_too_short_series():
    with pytest.raises(ValueError, match="Need more rows"):
        create_sequences(np.ones((3, 2)), window_size=3, target_index=1)

