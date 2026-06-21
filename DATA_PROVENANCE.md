# Data Provenance

This repository contains original code and documentation for an academic RNN/LSTM forecasting exercise. The MIT license in `LICENSE` applies to the original code, tests, scripts, and documentation.

The raw stock-price files were used as project input data. The original provider URL and license file are unavailable in this repository, so those market-data files are documented here as external input data and kept outside the MIT licensing boundary.

## Data Inventory

| Path | Role in this repository | Reuse note |
| --- | --- | --- |
| `data/Google_Stock_Price_Train.csv` | Historical Google stock-price training data used in the notebook. | External input data; original market-data provider terms apply. |
| `data/Google_Stock_Price_Test.csv` | Historical Google stock-price test data used in the notebook. | External input data; original market-data provider terms apply. |
| `data/OXY_Stock_Price_Train.xlsx` | Historical Occidental Petroleum stock-price training data used in the notebook. | External input data; original market-data provider terms apply. |
| `data/OXY_Stock_Price_Test.xlsx` | Historical Occidental Petroleum stock-price test data used in the notebook. | External input data; original market-data provider terms apply. |
| `results/baseline_metrics.csv` | Derived persistence-baseline metrics generated from the bundled train/test files. | Analysis output; source data reuse still depends on the original data provider terms. |
| `results/model_metrics.csv` | RNN and LSTM metric values copied from the executed notebook output. | Analysis output derived from the forecasting experiment. |
| `results/comparison_metrics.csv` | Combined RNN, LSTM, and persistence-baseline metrics. | Analysis output derived from the forecasting experiment and baseline script. |
| `results/forecast_plots/` | PNG plots saved by the notebook plotting cells. | Analysis output derived from the forecasting experiment. |

## Licensing Boundary

- Original notebook code and documentation: MIT license, see `LICENSE`.
- Reusable source code, tests, scripts, and derived metric-generation code: MIT license, see `LICENSE`.
- Bundled stock-price data files: external input data; original market-data provider terms apply.
- Reuse of the raw data should follow the original provider terms and any applicable market-data restrictions.

## Responsible-Use Note

Forecast outputs should be interpreted as academic sequence-modelling results, not as trading guidance.
