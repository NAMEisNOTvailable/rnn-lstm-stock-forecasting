# Results

This folder stores lightweight comparison outputs that can be regenerated quickly.

| File | Purpose |
| --- | --- |
| `baseline_metrics.csv` | One-step persistence baseline metrics for Google and OXY test periods. |
| `model_metrics.csv` | RNN and LSTM metrics copied from the executed notebook output. |
| `comparison_metrics.csv` | Combined RNN, LSTM, and persistence-baseline metrics. |
| `forecast_plots/` | Forecast and training-loss plots exported from the executed notebook. |

Regenerate the baseline metrics from the repository root:

```bash
python scripts/run_baseline.py
```

Export plots from the committed notebook output:

```bash
python scripts/export_notebook_plots.py
```

The baseline is a simple previous-day-close benchmark for comparison.
