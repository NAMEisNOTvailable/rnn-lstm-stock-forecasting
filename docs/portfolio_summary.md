# Portfolio Summary

This repository presents a financial time-series forecasting coursework project as a machine-learning portfolio artifact with a clearer engineering structure. The core experiment compares SimpleRNN and LSTM models on Google and Occidental Petroleum stock-price series using 60-timestep windows.

## Strengths

- The notebook covers an end-to-end sequence-modelling workflow: data loading, cleaning, scaling, train/validation split, model training, prediction, inverse scaling, plotting, and metric reporting.
- The reusable `src/` package extracts the parts that can be validated quickly: data cleaning, train/test scaling, sequence construction, test-window handling, forecast metrics, and a persistence baseline.
- The project uses multiple metrics: RMSE for magnitude error, sMAPE for relative error, MASE for comparison against naive in-sample movement, and RMSLE for log-scale error.
- CI now tests the reusable logic and regenerates a lightweight baseline output without rerunning long TensorFlow training.

## Reviewer Interpretation

The most valuable signal is not that a neural model can draw a plausible stock-price curve. The stronger signal is that the project handles sequence windows carefully, keeps evaluation caveats explicit, and compares outputs with metrics that expose different failure modes.

The persistence baseline in `results/baseline_metrics.csv` gives the neural-model outputs a simple previous-day-close benchmark for comparison.

## Known Limitations

- Historical close/open/high/low/volume features are not enough to make a robust financial forecasting system.
- A short test window can make results look more stable than they are.
- Repeated-run variance and seed sensitivity matter for RNN/LSTM training.
- This repository does not model transaction costs, slippage, portfolio risk, or live-market constraints.
- Forecasts are academic model outputs, not investment recommendations.

## Best Interview Framing

Use this project as evidence of ML workflow discipline: preprocessing, sequence modelling, metric choice, baseline comparison, and honest limitations. For security or AI safety roles, keep it as a supporting ML project behind the LLM/security repositories.
