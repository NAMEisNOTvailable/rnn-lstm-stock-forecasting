# RNN and LSTM - Financial Time-Series Forecasting

Deep learning coursework project for financial time-series forecasting using recurrent neural networks.

## Portfolio Summary

This project builds RNN/LSTM forecasting pipelines for stock-price time series and evaluates prediction quality with multiple error metrics. It is framed as an experiment in sequence modelling rather than a trading recommendation system.

Key work:

- Built recurrent forecasting pipelines for **Google** and **Occidental Petroleum** stock-price data.
- Used **60-timestep sequences** for supervised time-series modelling.
- Applied MinMax scaling and MSE/Adam-based model training.
- Compared RNN and LSTM behaviour across repeated runs.
- Evaluated forecasts with **RMSE**, **sMAPE**, **MASE**, and **RMSLE**.
- Documented seed sensitivity and the limitations of stock-price prediction with historical price-only models.

## Skills Demonstrated

- Time-series preprocessing
- RNN and LSTM sequence modelling
- Financial data analysis
- Forecast evaluation metrics
- Experiment tracking and reproducibility awareness
- Critical interpretation of model limitations

## Why This Matters

Financial forecasting can easily look stronger than it is if evaluation is too narrow. This project highlights uncertainty, seed sensitivity, and the limits of price-only sequence models, which is important for responsible analytical work.

## Repository Structure

```text
notebooks/   Main RNN/LSTM forecasting notebook
data/        Local stock-price CSV/XLSX files used by the notebook
README.md    Portfolio overview and reviewer guide
```

## Environment

The notebook metadata records Python 3.11.9. The reproducible environment is captured in [`requirements.txt`](requirements.txt), covering TensorFlow/Keras, pandas, NumPy, Matplotlib, scikit-learn, openpyxl for Excel inputs, Jupyter, and ipykernel.

```bash
pip install -r requirements.txt
jupyter notebook notebooks/rnn_lstm_stock_forecasting.ipynb
```

## License and Data

Original notebook code and documentation are licensed under the MIT License. Bundled stock-price data files are not relicensed by this repository; see [Data Provenance](DATA_PROVENANCE.md) before reusing data files.

## Status

Academic portfolio project. README added to make the repository easier for recruiters and reviewers to understand quickly.
