# RNN and LSTM - Financial Time-Series Forecasting

[![Smoke tests](https://github.com/NAMEisNOTvailable/rnn-lstm-stock-forecasting/actions/workflows/smoke.yml/badge.svg)](https://github.com/NAMEisNOTvailable/rnn-lstm-stock-forecasting/actions/workflows/smoke.yml)
![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-RNN%20%7C%20LSTM-ff6f00)
![License](https://img.shields.io/badge/License-MIT-green)

Financial time-series forecasting portfolio project comparing RNN and LSTM sequence models on Google and Occidental Petroleum stock-price data. The project is framed as a sequence-modelling experiment, not as a trading recommendation system.

## Project Snapshot

| Area | Summary |
| --- | --- |
| Task | One-step stock-price forecasting from historical price features |
| Assets | Google and Occidental Petroleum |
| Sequence length | 60 timesteps |
| Features | Open, High, Low, Close, Volume |
| Models in notebook | SimpleRNN and LSTM with dropout, MSE loss, Adam optimizer |
| Evaluation metrics | RMSE, sMAPE, MASE, RMSLE |
| Reviewer checks | Unit-tested preprocessing, sequence construction, metrics, and persistence baseline |
| Main artefacts | [`notebooks`](notebooks), [`src/rnn_lstm_stock_forecasting`](src/rnn_lstm_stock_forecasting), [`results`](results), [`docs/portfolio_summary.md`](docs/portfolio_summary.md) |

## What This Demonstrates

- Built RNN/LSTM forecasting pipelines for multivariate stock-price time series.
- Converted notebook logic into reusable, unit-tested helpers for cleaning, scaling, rolling-window sequence generation, and forecast metrics.
- Added a one-step persistence baseline so RNN/LSTM forecasts can be compared against a simple previous-day-close benchmark.
- Reported RMSE, sMAPE, MASE, and RMSLE to show absolute, relative, scaled, and log-scale error.
- Documented why historical price-only forecasting is fragile and should not be interpreted as investment advice.

## Baseline Reference

The repository includes a lightweight persistence baseline that forecasts each test close with the most recent observed close. It is not intended to beat the neural models; it gives reviewers a sanity-check comparator.

Run:

```bash
python scripts/run_baseline.py
```

The committed baseline output is stored in [`results/baseline_metrics.csv`](results/baseline_metrics.csv). Regenerate it after dependency installation if the source data changes.

## Repository Structure

```text
data/                         Stock-price CSV/XLSX files used by the notebook
docs/                         Portfolio summary and modelling caveats
notebooks/                    Original RNN/LSTM forecasting notebook
results/                      Lightweight baseline metrics for reviewer comparison
scripts/                      Command-line baseline runner
src/rnn_lstm_stock_forecasting/
                              Reusable preprocessing, sequence, metric, and baseline helpers
tests/                        Pytest coverage for the reusable project logic
```

## Environment

The notebook metadata records Python 3.11.9. For reviewer checks without TensorFlow training, install the package and test dependency:

```bash
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -e ".[dev]"
```

Run tests and the baseline check:

```bash
pytest
python scripts/run_baseline.py
```

For the full notebook environment, including TensorFlow and Jupyter:

```bash
.\.venv\Scripts\python -m pip install -r requirements.txt
jupyter notebook notebooks/rnn_lstm_stock_forecasting.ipynb
```

On Linux/macOS, replace `.\.venv\Scripts\python` with `. .venv/bin/activate` or call `.venv/bin/python`.

## Reviewer Notes

| What to inspect | Where |
| --- | --- |
| Notebook experiment and plots | [`notebooks/rnn_lstm_stock_forecasting.ipynb`](notebooks/rnn_lstm_stock_forecasting.ipynb) |
| Sequence construction and test-window handling | [`src/rnn_lstm_stock_forecasting/sequences.py`](src/rnn_lstm_stock_forecasting/sequences.py) |
| Forecast metrics | [`src/rnn_lstm_stock_forecasting/metrics.py`](src/rnn_lstm_stock_forecasting/metrics.py) |
| Baseline comparator | [`src/rnn_lstm_stock_forecasting/baselines.py`](src/rnn_lstm_stock_forecasting/baselines.py), [`results/baseline_metrics.csv`](results/baseline_metrics.csv) |
| CI and smoke checks | [`.github/workflows/smoke.yml`](.github/workflows/smoke.yml) |
| Portfolio positioning and caveats | [`docs/portfolio_summary.md`](docs/portfolio_summary.md) |

## Limitations

- The notebook uses historical price/volume features only; it does not include fundamentals, news, macro variables, market regime features, or transaction costs.
- The neural models are useful for sequence-modelling practice, but stock forecasting is highly sensitive to splits, seeds, market periods, and leakage controls.
- The bundled stock data is third-party market data and is not relicensed by this repository.
- This project is academic portfolio work, not financial advice or a deployable trading system.

## License and Data

Original source code, notebook code, tests, and documentation are licensed under the MIT License. Bundled stock-price data files are not relicensed by this repository; see [Data Provenance](DATA_PROVENANCE.md) before reusing them.

## Status

Academic portfolio project. The repository is organised so reviewers can inspect the original RNN/LSTM notebook, run a fast baseline check, and verify the reusable preprocessing and metric logic through CI.
