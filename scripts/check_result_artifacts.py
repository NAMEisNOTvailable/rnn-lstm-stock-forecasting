import csv
from pathlib import Path


BASE_COLUMNS = (
    "asset",
    "model",
    "test_rows",
    "rmse",
    "smape",
    "mase",
    "rmsle",
)
COMPARISON_COLUMNS = (*BASE_COLUMNS, "comparison_to_persistence")
METRIC_COLUMNS = ("rmse", "smape", "mase", "rmsle")
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


def read_csv(path: Path) -> list[dict[str, str]]:
    check_file(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def require_columns(path: Path, rows: list[dict[str, str]], expected_columns: tuple[str, ...]) -> None:
    if not rows:
        raise SystemExit(f"{path} has no data rows")
    columns = tuple(rows[0].keys())
    if columns != expected_columns:
        raise SystemExit(f"Unexpected {path} columns: {columns}")


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return row["asset"], row["model"]


def require_unique_keys(path: Path, rows: list[dict[str, str]]) -> None:
    keys = [row_key(row) for row in rows]
    duplicates = sorted(key for key in set(keys) if keys.count(key) > 1)
    if duplicates:
        raise SystemExit(f"{path} contains duplicate rows for: {duplicates}")


def base_row(row: dict[str, str]) -> dict[str, str]:
    return {column: row[column] for column in BASE_COLUMNS}


def compare_to_persistence(row: dict[str, str], baseline_row: dict[str, str]) -> str:
    metric_deltas = [float(row[column]) - float(baseline_row[column]) for column in METRIC_COLUMNS]
    if all(delta > 0 for delta in metric_deltas):
        return "worse"
    if all(delta < 0 for delta in metric_deltas):
        return "better"
    return "mixed"


def check_comparison_metrics(path: Path) -> None:
    rows = read_csv(path)
    require_columns(path, rows, COMPARISON_COLUMNS)
    require_unique_keys(path, rows)
    if len(rows) != 6:
        raise SystemExit(f"Expected 6 comparison rows, found {len(rows)}")

    by_key = {row_key(row): row for row in rows}
    baseline_by_asset = {
        row["asset"]: row
        for row in rows
        if row["model"] == "persistence_baseline"
    }

    for asset in ("Google", "OXY"):
        if asset not in baseline_by_asset:
            raise SystemExit(f"Missing persistence baseline row for {asset}")

    for row in rows:
        if row["model"] == "persistence_baseline":
            expected = "reference"
        else:
            expected = compare_to_persistence(row, baseline_by_asset[row["asset"]])
        if row["comparison_to_persistence"] != expected:
            raise SystemExit(
                "Unexpected comparison label for "
                f"{row['asset']} {row['model']}: {row['comparison_to_persistence']} != {expected}"
            )

    model_rows = read_csv(Path("results/model_metrics.csv"))
    baseline_rows = read_csv(Path("results/baseline_metrics.csv"))
    require_columns(Path("results/model_metrics.csv"), model_rows, BASE_COLUMNS)
    require_columns(Path("results/baseline_metrics.csv"), baseline_rows, BASE_COLUMNS)
    require_unique_keys(Path("results/model_metrics.csv"), model_rows)
    require_unique_keys(Path("results/baseline_metrics.csv"), baseline_rows)

    source_rows = {row_key(row): row for row in model_rows + baseline_rows}
    if set(source_rows) != set(by_key):
        raise SystemExit("comparison_metrics.csv rows do not match model and baseline metric rows")

    for key, source_row in source_rows.items():
        if base_row(by_key[key]) != source_row:
            raise SystemExit(f"comparison_metrics.csv does not match source metrics for {key}")


def main() -> int:
    check_comparison_metrics(Path("results/comparison_metrics.csv"))

    plot_dir = Path("results/forecast_plots")
    for filename in EXPECTED_PLOTS:
        check_file(plot_dir / filename)

    print("Result artifacts are present and non-empty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
