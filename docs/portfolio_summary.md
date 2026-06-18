# Portfolio Summary

This repository presents a University of Adelaide Deep Learning coursework project as a machine-learning portfolio artifact with a clearer engineering structure. The core experiment compares SimpleRNN and LSTM models on Google and Occidental Petroleum stock-price series using 60-timestep windows.

## Strengths

- The notebook covers an end-to-end sequence-modelling workflow: data loading, cleaning, scaling, train/validation split, model training, prediction, inverse scaling, plotting, and metric reporting.
- The reusable `src/` package extracts the parts that can be validated quickly: data cleaning, train/test scaling, sequence construction, test-window handling, forecast metrics, and a persistence baseline.
- The project uses multiple metrics: RMSE for magnitude error, sMAPE for relative error, MASE for comparison against naive in-sample movement, and RMSLE for log-scale error.
- CI tests the reusable logic and regenerates a lightweight baseline output through a short command.

## Project Interpretation

The strongest project signal is the workflow discipline around sequence windows, evaluation caveats, and metrics that expose different failure modes.

The persistence baseline in `results/baseline_metrics.csv` gives the neural-model outputs a simple previous-day-close benchmark for comparison.

## Known Limitations

- Historical close/open/high/low/volume features support a limited sequence-modelling exercise; a broader forecasting study would need additional market and business context.
- A short test window can make results look more stable than they are.
- Repeated-run variance and seed sensitivity matter for RNN/LSTM training.
- The project focuses on model workflow. Deployment topics such as transaction costs, slippage, portfolio risk, and live-market constraints are outside the coursework scope.
- Forecasts should be read as academic model outputs from a coursework setting.

## Best Interview Framing

Use this project as evidence of ML workflow discipline: preprocessing, sequence modelling, metric choice, baseline comparison, and honest limitations. For security or AI safety roles, keep it as a supporting ML project behind the LLM/security repositories.
