"""Run the published PBMC notebook on the 700-cell example with this Python environment."""
import os
from pathlib import Path

import matplotlib
from IPython.core.interactiveshell import InteractiveShell


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "notebooks" / "single_cell" / "pbmc68k.ipynb"
    data = root / "data" / "demo" / "pbmc700.h5ad"
    if not data.is_file():
        raise SystemExit(f"Missing demo input: {data}. Download the complete repository ZIP.")
    output = root / "results" / "runs" / "pbmc_demo"
    print(f"Running {source.name} on {data.name}...", flush=True)
    os.chdir(root)
    os.environ["SCAICME_PBMC_MODE"] = "demo"
    matplotlib.use("Agg")
    # Execute the notebook cells in order with the interpreter that launched this script.
    InteractiveShell.instance().safe_execfile_ipy(source, raise_exceptions=True)
    print(f"Finished. Open {output / 'predictions.csv'}")
    print(f"Annotated data: {output / 'annotated.h5ad'}")


if __name__ == "__main__":
    main()
