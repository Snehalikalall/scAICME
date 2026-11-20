# Data and marker panels

[Study manifest](datasets.tsv) · [Marker panels used by the notebooks](notebook_markers.tsv) · [Curated manuscript panels](manuscript_markers.tsv)

Download expression data from each study’s source record. Use the **Supplementary files** section on GEO for processed matrices and tissue-position files. Large expression matrices and histology archives belong in the local folders described below. Raw study data are distributed by the original data providers.

## PBMC demo

[Download pbmc700.h5ad](https://raw.githubusercontent.com/Snehalikalall/scAICME/main/data/demo/pbmc700.h5ad) · [Run the example](../README.md#run-the-pbmc-demo)

This teaching file contains 700 real PBMCs and 765 genes from **10x Genomics, Fresh 68k PBMCs (Donor A)**, as processed and distributed by Scanpy. The original dataset is available under CC BY 4.0. [10x Genomics dataset](https://www.10xgenomics.com/datasets/fresh-68-k-pbm-cs-donor-a-1-standard-1-1-0) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · [Scanpy preparation](https://scanpy.readthedocs.io/en/stable/api/generated/scanpy.datasets.pbmc68k_reduced.html)

The file retains the cell order, barcodes and gene symbols of Scanpy 1.12.2's reduced example. Its sparse `X` matrix is copied from the source object's `raw.X` and holds unscaled, **log-normalized expression**. The demo reads it on that scale. `obs["reference_label"]` contains the original `bulk_labels` for comparison after fitting. The input contains no predicted labels or precomputed embeddings.

The small run uses a minimum of 10 cells for a qualifying mixture cluster and for a retained seed label. The full-study run uses its original minimum of 100 for both. The example demonstrates how to run the workflow and inspect its outputs. The paper's cohort results are in the [results guide](../results/README.md).

## Single-cell inputs

| Notebook | Expected input relative to the repository root | Preparation |
| --- | --- | --- |
| PBMC 68K | `data/raw/pbmc68k_10x/filtered_matrices_mex/hg19/` | Extract the filtered 10x matrix, with `matrix.mtx`, `genes.tsv` and `barcodes.tsv`. Add `pbmc_annot.csv` with a `pbmcannot` column and preferably a unique `barcode` column. The authors’ CSV is a separate input. [10x dataset](https://www.10xgenomics.com/datasets/fresh-68-k-pbm-cs-donor-a-1-standard-1-1-0) · [Reference analysis](https://github.com/10XGenomics/single-cell-3prime-paper/tree/master/pbmc68k_analysis) |
| Breast | `data/prepared/GSE161529_combined.h5ad` | A combined, count-scale AnnData with gene symbols and a `sample` column for stratified downsampling. The study’s reference labels come from the authors’ Seurat objects. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161529) · [Figshare 17058077](https://doi.org/10.6084/m9.figshare.17058077) |
| Lung | `data/prepared/GSE127465_human_processed.h5ad` | A human, count-scale AnnData with gene symbols. Retain `Major cell type` for comparisons that use reference labels. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE127465) |
| Oral | `data/prepared/GSE215403_combined.h5ad` | A combined, count-scale AnnData with gene symbols. The notebook writes the QC-filtered object under its own run directory. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE215403) |

The supplied single-cell tumour notebooks start at processed AnnData objects. The exact H5AD files and the original conversion scripts were outside the supplied materials. For an exact reproduction, obtain the authors’ inputs; for a new analysis, document the conversion from the accession and retain the matrix, feature and sample identifiers. Keep counts on the input scale expected by the preprocessing cell.

## Spatial inputs

| Tissue | Folder below `data/raw/` | Sections and expected layout |
| --- | --- | --- |
| Skin | `GSE225475_RAW_extracted/` | Six sections, NS1, NS2 and PP1–PP4. Each section directory contains the Space Ranger count H5 and `spatial/`. The notebook expects paths such as `GSM7049137_PP4.tar/PP4/` after extraction. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE225475) |
| Oral SCC | `GSE208253_RAW/` | S1–S12 (file names use lowercase `s`), GSM6339631–GSM6339642. Keep the accession-prefixed H5 and positions CSV side by side. Include the sample-matched histology and scale factors for overlays. Extract the hires PNG for the plotting cell. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE208253) |
| Breast | `GSE243022_RAW/` | A1, B1, C1 and D1, GSM7777520–GSM7777523. The reader expects `<GSM>_<sample>_filtered_feature_bc_matrix.h5` and `<GSM>_<sample>_spatial/spatial/`. Decompress H5 and spatial archives before use. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243022) |
| Lung NSCLC | `GSE292299_SELECTED/` | P1, P2, P4 and P5, GSM8855703, GSM8855704, GSM8855706 and GSM8855707. Extract each section’s H5 and Space Ranger spatial files, keeping the GSM or sample identifiers in the paths for discovery. [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292299) |

A spatial section pairs barcodes with tissue coordinates. Retain the original barcode, section identifier, hires or lowres tissue image and scale-factor JSON together. Spatial neighbourhoods are built within sections.

## Marker sources

`notebook_markers.tsv` lists the 548 marker memberships in the eight dataset-specific panels used by the notebooks. `manuscript_markers.tsv` transcribes the 613 rows in the five curated supplementary panels. The manuscript’s `use_as_printed` and source-key fields are preserved. An empty use field means the corresponding table cell was empty. The two files document different stages of the study. Use [marker_source_keys.tsv](marker_source_keys.tsv) to look up each source key in [the bibliography](marker_references.bib). [marker_sources.tex](marker_sources.tex) gives the supporting location within each publication.
