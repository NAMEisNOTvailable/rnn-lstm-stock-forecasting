# RNN/LSTM Stock Forecasting with Baseline-Aware Evaluation

[![Smoke tests](https://github.com/NAMEisNOTvailable/rnn-lstm-stock-forecasting/actions/workflows/smoke.yml/badge.svg)](https://github.com/NAMEisNOTvailable/rnn-lstm-stock-forecasting/actions/workflows/smoke.yml)
![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-RNN%20%7C%20LSTM-ff6f00)
![License](https://img.shields.io/badge/License-MIT-green)

University of Adelaide Deep Learning coursework project comparing RNN and LSTM sequence models on Google and Occidental Petroleum stock-price data.

## Project Snapshot

| Area | Summary |
| --- | --- |
| Task | One-step stock-price forecasting from historical price features |
| Assets | Google and Occidental Petroleum |
| Sequence length | 60 timesteps |
| Features | Open, High, Low, Close, Volume |
| Models in notebook | SimpleRNN and LSTM with dropout, MSE loss, Adam optimizer |
| Evaluation metrics | RMSE, sMAPE, MASE, RMSLE |
| Validation checks | Unit-tested preprocessing, sequence construction, metrics, and persistence baseline |
| Main artefacts | [`notebooks`](notebooks), [`src/rnn_lstm_stock_forecasting`](src/rnn_lstm_stock_forecasting), [`results/comparison_metrics.csv`](results/comparison_metrics.csv), [`results/forecast_plots`](results/forecast_plots), [`docs/portfolio_summary.md`](docs/portfolio_summary.md) |

## What This Demonstrates

- Built RNN/LSTM forecasting pipelines for multivariate stock-price time series.
- Added tested helper modules for data cleaning, scaling, rolling-window sequence generation, and forecast metrics.
- Added a one-step persistence baseline so RNN/LSTM forecasts can be compared against a simple previous-day-close benchmark.
- Reported RMSE, sMAPE, MASE, and RMSLE to show absolute, relative, scaled, and log-scale error.
- Documented the limits of historical price-only forecasting and the coursework context for the experiment.

## Model Results

Metrics below come from the executed notebook output and the committed persistence-baseline run. Lower values are better for all four metrics.

| Asset | Model | RMSE | sMAPE | MASE | RMSLE |
| --- | --- | ---: | ---: | ---: | ---: |
| Google | RNN | 25.79 | 3.04 | 3.27 | 0.0325 |
| Google | LSTM | 15.87 | 1.69 | 1.84 | 0.0197 |
| Google | Persistence baseline | 8.32 | 0.77 | 0.84 | 0.0103 |
| OXY | RNN | 0.88 | 1.02 | 0.80 | 0.0125 |
| OXY | LSTM | 0.75 | 0.95 | 0.74 | 0.0107 |
| OXY | Persistence baseline | 0.60 | 0.72 | 0.56 | 0.0085 |

This result shows how difficult short-window stock forecasting can be: a simple previous-close baseline outperformed the RNN/LSTM models in this run.

Full metrics are stored in [`results/comparison_metrics.csv`](results/comparison_metrics.csv). Forecast plots are saved under [`results/forecast_plots`](results/forecast_plots).

## Baseline Reference

The repository includes a lightweight persistence baseline that predicts each test-period closing price from the most recent observed close. This gives the RNN/LSTM results a simple previous-day-close benchmark for comparison.

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
results/                      Comparison metrics and exported notebook plots
scripts/                      Command-line baseline runner
src/rnn_lstm_stock_forecasting/
                              Reusable preprocessing, sequence, metric, and baseline helpers
tests/                        Pytest coverage for the reusable project logic
```

## Environment

The notebook metadata records Python 3.11.9. For fast checks that skip TensorFlow training, install the package and test dependency:

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

## Project Notes

| What to inspect | Where |
| --- | --- |
| Notebook experiment and plots | [`notebooks/rnn_lstm_stock_forecasting.ipynb`](notebooks/rnn_lstm_stock_forecasting.ipynb) |
| Sequence construction and test-window handling | [`src/rnn_lstm_stock_forecasting/sequences.py`](src/rnn_lstm_stock_forecasting/sequences.py) |
| Forecast metrics | [`src/rnn_lstm_stock_forecasting/metrics.py`](src/rnn_lstm_stock_forecasting/metrics.py) |
| Baseline benchmark | [`src/rnn_lstm_stock_forecasting/baselines.py`](src/rnn_lstm_stock_forecasting/baselines.py), [`results/comparison_metrics.csv`](results/comparison_metrics.csv) |
| Forecast plots | [`results/forecast_plots`](results/forecast_plots) |
| CI and smoke checks | [`.github/workflows/smoke.yml`](.github/workflows/smoke.yml) |
| Portfolio positioning and caveats | [`docs/portfolio_summary.md`](docs/portfolio_summary.md) |

## Limitations

- The notebook uses historical price/volume features only; a broader forecasting study would add fundamentals, news, macro variables, market regime features, and transaction-cost assumptions.
- The neural models are useful for sequence-modelling practice, but stock forecasting is highly sensitive to splits, seeds, market periods, and leakage controls.
- The bundled stock data is third-party market data and remains under the original data-provider terms.
- This project was completed as a University of Adelaide Deep Learning coursework project.

## License and Data

Original source code, notebook code, tests, and documentation are licensed under the MIT License. Bundled stock-price data files remain under the original data-provider terms; see [Data Provenance](DATA_PROVENANCE.md) before reusing them.

## Status

Academic portfolio project. The repository is organised around the original RNN/LSTM notebook, a fast baseline check, and CI coverage for the reusable preprocessing and metric logic.
