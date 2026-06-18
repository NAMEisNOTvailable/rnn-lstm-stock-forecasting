import csv
from pathlib import Path


EXPECTED_PLOTS = (
    "google_forecast.png",
    "google_lstm_loss.png",
    "google_rnn_loss.png",
    "oxy_forecast.png",
    "oxy_lstm_loss.png",
    "oxy_rnn_loss.png",
)


def check_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"Missing required artifact: {path}")
    if path.stat().st_size == 0:
        raise SystemExit(f"Artifact is empty: {path}")


def check_comparison_metrics(path: Path) -> None:
    check_file(path)
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    expected_columns = [
        "asset",
        "model",
        "test_rows",
        "rmse",
        "smape",
        "mase",
        "rmsle",
        "comparison_to_persistence",
    ]
    if rows and list(rows[0].keys()) != expected_columns:
        raise SystemExit(f"Unexpected comparison_metrics.csv columns: {list(rows[0].keys())}")
    if len(rows) != 6:
        raise SystemExit(f"Expected 6 comparison rows, found {len(rows)}")

    comparisons = {row["comparison_to_persistence"] for row in rows}
    if comparisons != {"worse", "reference"}:
        raise SystemExit(f"Unexpected comparison labels: {comparisons}")


def main() -> int:
    check_comparison_metrics(Path("results/comparison_metrics.csv"))
    check_file(Path("results/model_metrics.csv"))
    check_file(Path("results/baseline_metrics.csv"))

    plot_dir = Path("results/forecast_plots")
    for filename in EXPECTED_PLOTS:
        check_file(plot_dir / filename)

    print("Result artifacts are present and non-empty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

