# scAICME

**Adaptive Marker-Guided Semi-Supervised Framework for Single-Cell RNA-seq and Spatial Transcriptomics Data Analysis**

Snehalika Lall and Adityarup Laha (equal contribution), Jayant Jha, Sanghamitra Bandyopadhyay and Raghunath Chatterjee · Indian Statistical Institute, Kolkata.

[Run the PBMC demo](#run-the-pbmc-demo) · [Project page](https://snehalikalall.github.io/scAICME/) · [Data and accessions](data/README.md) · [Analysis notebooks](notebooks/README.md) · [Results and provenance](results/README.md)

scAICME uses expression of tissue-specific markers to select seed labels, then trains classifiers on the seeds and records their agreement for each cell or spatial spot. In a Visium section, the label describes the predominant expression signal in a spot that can contain multiple cells.

![Tissue histology and scAICME consensus labels in psoriatic skin](docs/assets/skin-spatial.webp)

*Psoriatic skin, GSE225475. The manuscript pairs the tissue image with the spatial distribution of consensus labels. The [full-resolution figure](results/figures/Skin_original_vs_label_consensus.png) is available with the other results.*

## Run the PBMC demo

Annotate **700 real peripheral blood mononuclear cells across 765 genes** with the same five-method workflow used in the PBMC notebook. The repository includes a 452 KiB AnnData file and runs on a CPU. [Download pbmc700.h5ad](https://raw.githubusercontent.com/Snehalikalall/scAICME/main/data/demo/pbmc700.h5ad) · [Dataset source and preparation](data/README.md#pbmc-demo)

1. [Download the repository ZIP](https://github.com/Snehalikalall/scAICME/archive/refs/heads/main.zip), extract it, and open a terminal in the folder containing `requirements.txt`. Alternatively, run `git clone https://github.com/Snehalikalall/scAICME.git` and then `cd scAICME`.
2. Create the environment and run the example. The first three commands are the one-time setup. Use the last command to repeat the analysis.

   ```bash
   conda create -n scaicme-demo python=3.13 pip -y
   conda activate scaicme-demo
   python -m pip install -r requirements.txt
   python scripts/run_demo.py
   ```

3. Open `results/runs/pbmc_demo/predictions.csv`. It contains **700 rows**, one per cell barcode. `label_consensus` is the winning cell label and `consensus_agree_frac` is the fraction of all five methods voting for it. For example, a value of **0.8** means **four of five** methods voted for that label. The same directory contains `annotated.h5ad` with the expression matrix and predictions, plus a marker dot plot and heatmap as PNG files.

**To run interactively**, use the same environment and enter `python -m jupyterlab notebooks/single_cell/pbmc68k.ipynb`. Choose **Run → Run All Cells**. A fresh checkout selects the demo automatically. The command-line runner always selects the demo, including when the full study data are present. [Open the notebook on GitHub](notebooks/single_cell/pbmc68k.ipynb)

The first two cells in a test run with Python 3.13.9, Scanpy 1.12.2 and scikit-learn 1.7.2 illustrate how to read the output. The second cell shows why agreement between methods and agreement with the reference are different quantities.

| Cell barcode | Source reference | Predicted consensus | Agreement |
| --- | --- | --- | ---: |
| `AAAGCCTGGCTAAC-1` | CD14+ Monocyte | CD14+ Monocyte | 4/5 |
| `AAATTCGATGCACA-1` | Dendritic | CD14+ Monocyte | 5/5 |

## Run the study analyses

To inspect the saved spatial results, run this command from the repository root with Python 3. It reads the included CSVs and requires only the standard library.

```bash
python scripts/show_spatial_results.py
```

To run a full study analysis, prepare the inputs for one tissue. The data guide gives the archive accession, expected local layout and required reference files for each notebook. You can reuse the environment above or create a separate one.

```bash
conda create -n scaicme-notebooks python=3.11 pip -y
conda activate scaicme-notebooks
python -m pip install -r requirements.txt
python -m jupyter lab
```

Open one of the notebooks below and run the cells in order from a fresh kernel. Each notebook writes to its own directory under `results/runs/`. Optional comparison cells have a switch in the first code cell and use additional packages listed in the [notebook guide](notebooks/README.md).

| Dataset | Single-cell RNA-seq | Spatial transcriptomics |
| --- | --- | --- |
| PBMC 68K | [10x PBMC 68K](notebooks/single_cell/pbmc68k.ipynb) | — |
| Breast | [GSE161529](notebooks/single_cell/breast_gse161529.ipynb) | [GSE243022](notebooks/spatial/breast_gse243022.ipynb) |
| Lung | [GSE127465](notebooks/single_cell/lung_gse127465.ipynb) | [GSE292299](notebooks/spatial/lung_gse292299.ipynb) |
| Oral | [GSE215403](notebooks/single_cell/oral_gse215403.ipynb) | [GSE208253](notebooks/spatial/oral_gse208253.ipynb) |
| Skin | [Study record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173706) | [GSE225475](notebooks/spatial/skin_gse225475.ipynb) |

The manuscript also describes PBMC CITE-seq, bone marrow and retina. The [dataset manifest](data/datasets.tsv) covers all twelve study datasets and identifies the eight with supplied notebooks.

## Interpreting this release

These eight notebooks implement the authors’ tissue-specific analyses. They contain an earlier consensus implementation. For example, the PBMC notebook takes a plurality over five classifier outputs and records agreement. The manuscript describes a six-classifier, two-thirds agreement rule and a lineage-then-subtype procedure. The code for that later benchmark was outside the supplied files.

The [results guide](results/README.md) distinguishes notebook output from manuscript transcriptions. The four scAICME spatial metric rows agree across those sources. Some comparator values and two spot counts differ. The guide records the differences alongside the original figures. Local reruns and their outputs belong under `results/runs/`.

## Citation

Lall S, Laha A, Jha J, Bandyopadhyay S, Chatterjee R. *scAICME: Adaptive Marker-Guided Semi-Supervised Framework for Single-Cell RNA-seq and Spatial Transcriptomics Data Analysis*. Manuscript. The repository citation is also available in [CITATION.cff](CITATION.cff).
