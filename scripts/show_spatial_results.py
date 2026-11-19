"""Print saved scAICME spatial measurements and check their manuscript transcription."""

import csv
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"


def read_csv(name):
    with (RESULTS / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    saved = [r for r in read_csv("spatial_notebook_outputs.csv") if r["method_in_notebook"] == "scAICME"]
    paper = {r["accession"]: r for r in read_csv("table2_spatial_reported.csv") if r["method_as_printed"] == "scAICME"}
    metrics = ("spatial_coherence", "spatial_inconsistency", "morans_i")
    if len(saved) != 4 or len(paper) != 4 or {r["accession"] for r in saved} != paper.keys():
        raise ValueError("Expected four matched scAICME spatial records.")
    print("Dataset        Accession    Graph spots  Coherence  Inconsistency   Moran's I")
    for row in sorted(saved, key=lambda r: r["dataset"]):
        ref = paper[row["accession"]]
        if any(row[k] != ref[k] for k in metrics):
            raise ValueError(f"Metric transcription differs for {row['accession']}.")
        print(f"{row['dataset']:<14} {row['accession']:<11} {int(row['spots_in_saved_comparison']):>10,}  "
              f"{row['spatial_coherence']:>9}  {row['spatial_inconsistency']:>13}  {row['morans_i']:>10}")


if __name__ == "__main__":
    main()
