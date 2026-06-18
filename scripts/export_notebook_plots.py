import base64
import json
from pathlib import Path


PLOT_NAMES = {
    (11, 0): "google_rnn_loss.png",
    (11, 1): "google_lstm_loss.png",
    (11, 2): "oxy_rnn_loss.png",
    (11, 3): "oxy_lstm_loss.png",
    (16, 0): "google_forecast.png",
    (17, 0): "oxy_forecast.png",
}


def main() -> int:
    notebook_path = Path("notebooks/rnn_lstm_stock_forecasting.ipynb")
    output_dir = Path("results/forecast_plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    exported = []
    for cell_index, cell in enumerate(notebook.get("cells", [])):
        image_output_index = 0
        for output in cell.get("outputs", []):
            image_data = output.get("data", {}).get("image/png")
            if image_data is None:
                continue

            name = PLOT_NAMES.get((cell_index, image_output_index), f"cell_{cell_index}_plot_{image_output_index}.png")
            image_bytes = base64.b64decode("".join(image_data))
            path = output_dir / name
            path.write_bytes(image_bytes)
            exported.append(path)
            image_output_index += 1

    for path in exported:
        print(f"Exported {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

