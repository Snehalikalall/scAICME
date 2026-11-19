# Analysis notebooks

Run each notebook with its own fresh Python kernel. The first code cell locates the repository, configures input paths and creates a tissue-specific output directory. Standard preprocessing, seed assignment, classification and the available annotation plots run with the core requirements. Set `RUN_COMPARISONS = True` only when the input data and optional environment for those cells are ready.

| Analysis | Main output | Optional methods |
| --- | --- | --- |
| PBMC 68K | Per-cell consensus and agreement, marker plots and clustering metrics | scANVI via `scvi-tools`; reference-label evaluation needs the authors’ annotation CSV. |
| Breast, lung and oral single-cell | Seed labels, individual classifier outputs, consensus and clustering metrics | scANVI via `scvi-tools` and CellTypist via `celltypist`. |
| Skin, oral, breast and lung spatial | Per-spot consensus labels with sample and barcode, spatial overlay and marker plot | SpaGCN and stLearn are optional dependencies. Their original calls are retained in the comparison cells. |

The notebooks include a mixture seeder and graph-based alternatives. Several cells write to the same seed column, so changing their sequence changes the run. Examine the seed column and classifier outputs when comparing variants. The final analysis objects are in memory as `adata`. The principal outputs are `adata.obs["label_consensus"]` and `adata.obs["consensus_agree_frac"]`.

## Differences from the uploaded working files

The [source index](source_files.tsv) maps all eight original names to their release paths. Local machine paths were replaced with repository paths, stored notebook output was cleared, and spatial CSV readers were matched to their upstream writers. The lung spatial file was renamed for GSE292299. The skin SpaGCN export uses the raw barcode column for joins. The three tumour spatial notebooks use their own marker panels for the optional graph seeder where the source referred to the skin panel and an undefined object. The PBMC mixture call resolves to the no-PCA function actually defined in that notebook.

PBMC reference labels should be joined by barcode. A legacy single-column annotation file can be used if its row order matches the original matrix. Importing an external scANVI prediction file and applying the source notebook’s manual label substitution are separate, opt-in steps. The latter maps `CD4+ T Helper2` to `CD34+` and needs author confirmation before a biological interpretation.

These edits address portability and fresh-kernel execution. The archived comparison values are the values stored in the authors’ notebooks before these edits. The later hierarchical benchmark and the full comparison environment described in the paper require their separate implementation, data splits and software versions.
