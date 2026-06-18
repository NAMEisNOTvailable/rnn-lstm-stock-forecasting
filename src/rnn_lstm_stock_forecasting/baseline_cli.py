from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

from .baselines import evaluate_persistence_baseline
from .data import clean_price_frame, read_price_frame

ASSET_FILES = {
    "Google": ("Google_Stock_Price_Train.csv", "Google_Stock_Price_Test.csv"),
    "OXY": ("OXY_Stock_Price_Train.xlsx", "OXY_Stock_Price_Test.xlsx"),
}


def run_baselines(data_dir: Path) -> list[dict[str, float | str | int]]:
    rows = []
    for asset, (train_name, test_name) in ASSET_FILES.items():
        train_df = clean_price_frame(read_price_frame(data_dir / train_name))
        test_df = clean_price_frame(read_price_frame(data_dir / test_name))
        rows.append(evaluate_persistence_baseline(asset, train_df, test_df))
    return rows


def write_rows(rows: Iterable[dict[str, float | str | int]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["asset", "model", "test_rows", "rmse", "smape", "mase", "rmsle"]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row[name] for name in fieldnames})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a one-step persistence baseline on the bundled stock data.")
    parser.add_argument("--data-dir", type=Path, default=Path("data"), help="Directory containing the stock data files.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/baseline_metrics.csv"),
        help="CSV file to write baseline metrics.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rows = run_baselines(args.data_dir)
    write_rows(rows, args.output)
    for row in rows:
        print(
            f"{row['asset']} persistence baseline: "
            f"RMSE={row['rmse']:.4f}, sMAPE={row['smape']:.4f}, "
            f"MASE={row['mase']:.4f}, RMSLE={row['rmsle']:.4f}"
        )
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

