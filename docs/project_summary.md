# Project Summary

This repository presents a SimpleRNN/LSTM forecasting experiment with a clearer engineering structure. The core experiment compares sequence models on Google and Occidental Petroleum stock-price series using 60-timestep windows.

## Strengths

- The notebook covers an end-to-end sequence-modelling workflow: data loading, cleaning, scaling, train/validation split, model training, prediction, inverse scaling, plotting, and metric reporting.
- The reusable `src/` package extracts the parts that can be validated quickly: data cleaning, train/test scaling, sequence construction, test-window handling, forecast metrics, and a persistence baseline.
- The project uses multiple metrics: RMSE for magnitude error, sMAPE for relative error, MASE for comparison against naive in-sample movement, and RMSLE for log-scale error.
- CI tests the reusable logic and regenerates a lightweight baseline output through a short command.

## Project Positioning

This project is best read as a workflow and evaluation exercise: preprocessing, sequence modelling, metric choice, baseline comparison, and clear limitations.

The persistence baseline in `results/baseline_metrics.csv` gives the neural-model outputs a simple previous-day-close benchmark for comparison.

## Known Limitations

- Historical close/open/high/low/volume features support a limited sequence-modelling exercise; a broader forecasting study would need additional market and business context.
- A short test window can make results look more stable than they are.
- Repeated-run variance and seed sensitivity matter for RNN/LSTM training.
- The project focuses on model workflow. Deployment topics such as transaction costs, slippage, investment risk, and live-market constraints are outside the experiment scope.
- Forecasts should be read as academic model outputs, not trading guidance.
