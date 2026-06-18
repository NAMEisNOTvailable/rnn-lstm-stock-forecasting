# Notebooks

This folder contains the original RNN/LSTM stock-price forecasting notebook.

Open `rnn_lstm_stock_forecasting.ipynb` from this folder after installing the dependencies from the repository root:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/rnn_lstm_stock_forecasting.ipynb
```

For fast checks that do not rerun TensorFlow training, use the package tests and baseline command from the repository root:

```bash
pip install -e ".[dev]"
pytest
python scripts/run_baseline.py
```
