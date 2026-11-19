# Results and provenance

| File | Contents and source |
| --- | --- |
| [table1_single_cell.csv](table1_single_cell.csv) | All 32 rows of main Table 1, transcribed from the supplied `v3.tex`. The authors flagged this table for regeneration. Values are preserved at the printed precision. |
| [table2_spatial_reported.csv](table2_spatial_reported.csv) | The 16 non-placeholder rows of main Table 2. Spot counts and method names are as printed. Four BANKSY rows are explicitly described as hypothetical in the manuscript and are excluded. |
| [spatial_notebook_outputs.csv](spatial_notebook_outputs.csv) | All 16 rows displayed by the four uploaded spatial notebooks, with the number of spots in the final comparison graph. These are saved outputs from earlier runs. |
| [spatial_crosscheck.csv](spatial_crosscheck.csv) | Side-by-side spot counts, method names and categorical Moran’s I. The Seurat row is placed beside the notebook’s Leiden row solely to expose the naming discrepancy. |
| [figure_index.tsv](figure_index.tsv) | All 28 original PNGs in the Overleaf ZIP. The index identifies assets referenced by the main source, by the supplement, or present as additional figures, and includes a SHA-256 digest for each. |
| [figures](figures/) | Original-resolution figure assets plus the two TikZ sources for the method diagram. Additional figures include earlier and alternative panels. |

## Spatial results recorded in both sources

| Tissue | GEO accession | Spots in saved graph | scAICME coherence | scAICME inconsistency | scAICME Moran’s I |
| --- | --- | ---: | ---: | ---: | ---: |
| Skin | GSE225475 | 7,184 | 0.834363 | 0.165637 | 0.443570 |
| Oral SCC | GSE208253 | 24,921 | 0.751890 | 0.248110 | 0.262611 |
| Breast | GSE243022 | 3,216 | 0.766428 | 0.233572 | 0.382354 |
| Lung NSCLC | GSE292299 | 28,531 | 0.727955 | 0.272045 | 0.289200 |

Main Table 2 gives 7,570 skin and 3,581 breast spots. The notebook QC logs give 7,184 and 3,216, respectively, and the dimensions of the final comparison graphs confirm those post-QC counts. For oral and lung the two sources agree on counts. All four scAICME metric triples agree across sources. The twelve comparison-method Moran’s I values differ, and the manuscript labels the second method Seurat while the notebook calls Scanpy Leiden. Use the crosscheck to trace these differences. A method ranking from these mixed sources would require the original comparison runs.

## Figure guide

The workflow is provided as [Phase I](figures/workflow_phase1.tex) and [Phase II](figures/workflow_phase2.tex). The paper also shows the [PBMC comparison](figures/pbmc_compareall_journal_style.png), [multi-tissue marker heatmaps](figures/heatmap_alldata.png), [skin spatial overlay](figures/Skin_original_vs_label_consensus.png) and [skin marker heatmap](figures/GSE245475_Skin_marker_heatmap.png). The last asset has a typo in the original filename; the skin dataset is GSE225475.

The supplement includes spatial panels for [oral](figures/Oral_OSCC_original_vs_scAICME_consensus.png), [breast](figures/BreastCancer_original_vs_scAICME_consensus_A1.png) and [lung](figures/GSE292299_Lung_original_vs_scAICME_consensus.png). Its source identifies these as earlier, tissue-specific analyses. Figures and transcription tables document the supplied manuscript snapshot. They have not been re-estimated from the underlying expression matrices for this release.
