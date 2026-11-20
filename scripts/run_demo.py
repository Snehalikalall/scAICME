"""Run the published PBMC notebook on the 700-cell example with this Python environment."""
import os
from pathlib import Path

import nbformat
from jupyter_client import AsyncKernelManager
from jupyter_client.kernelspec import KernelSpecManager
from nbclient import NotebookClient


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "notebooks" / "single_cell" / "pbmc68k.ipynb"
    data = root / "data" / "demo" / "pbmc700.h5ad"
    if not data.is_file():
        raise SystemExit(f"Missing demo input: {data}. Download the complete repository ZIP.")
    output = root / "results" / "runs" / "pbmc_demo"
    print(f"Running {source.name} on {data.name} with a fresh kernel...", flush=True)
    notebook = nbformat.read(source, as_version=4)
    # Use the current Python installation, even if another user-level kernel is registered.
    manager = AsyncKernelManager(kernel_name="python3", kernel_spec_manager=KernelSpecManager(kernel_dirs=[]))
    client = NotebookClient(notebook, km=manager, timeout=900)
    client.execute(cwd=str(root), env={**os.environ, "SCAICME_PBMC_MODE": "demo"}, cleanup_kc=True)
    nbformat.write(notebook, output / "executed_demo.ipynb")
    print(f"Finished. Open {output / 'predictions.csv'}")
    print(f"Annotated data: {output / 'annotated.h5ad'}")
    print(f"Executed notebook: {output / 'executed_demo.ipynb'}")


if __name__ == "__main__":
    main()
