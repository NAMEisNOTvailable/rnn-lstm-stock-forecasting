# Results

This folder stores lightweight comparison outputs that can be regenerated quickly.

| File | Purpose |
| --- | --- |
| `baseline_metrics.csv` | One-step persistence baseline metrics for Google and OXY test periods. |

Regenerate the baseline metrics from the repository root:

```bash
python scripts/run_baseline.py
```

The baseline is a simple previous-day-close benchmark for comparison.
