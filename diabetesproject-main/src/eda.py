"""
eda.py
Primary exploratory analysis for the Pima Indians Diabetes dataset.
Produces:
  - reports/summary_statistics.csv
  - reports/missingness_report.csv
  - reports/figures/target_balance.png
  - reports/figures/feature_histograms.png
  - reports/figures/correlation_heatmap.png
  - data/processed/diabetes_flagged.csv  (zeros -> NaN, not imputed)
"""

from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.load_data import load_raw, load_flagged, ZERO_AS_MISSING_COLUMNS

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
FIGS = REPORTS / "figures"
PROCESSED = ROOT / "data" / "processed"


def main():
    df_raw = load_raw()
    df = load_flagged()

    print(f"Shape: {df_raw.shape}")
    print(df_raw.dtypes)

    summary = df.describe(include="all").T
    summary["missing_count"] = df.isna().sum()
    summary["missing_pct"] = (df.isna().mean() * 100).round(1)
    summary.to_csv(REPORTS / "summary_statistics.csv")

    missing = pd.DataFrame({
        "column": ZERO_AS_MISSING_COLUMNS,
        "zero_count_raw": [(df_raw[c] == 0).sum() for c in ZERO_AS_MISSING_COLUMNS],
        "zero_pct_raw": [round((df_raw[c] == 0).mean() * 100, 1) for c in ZERO_AS_MISSING_COLUMNS],
    })
    missing.to_csv(REPORTS / "missingness_report.csv", index=False)
    print(missing)

    plt.figure(figsize=(4, 4))
    df_raw["Outcome"].value_counts().sort_index().plot(
        kind="bar", color=["#4C72B0", "#DD8452"]
    )
    plt.xticks([0, 1], ["No diabetes (0)", "Diabetes (1)"], rotation=0)
    plt.ylabel("Count")
    plt.title("Target class balance")
    plt.tight_layout()
    plt.savefig(FIGS / "target_balance.png", dpi=150)
    plt.close()

    feature_cols = [c for c in df.columns if c != "Outcome"]
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    for ax, col in zip(axes.flat, feature_cols):
        df[col].dropna().hist(ax=ax, bins=25, color="#4C72B0")
        ax.set_title(col)
    plt.tight_layout()
    plt.savefig(FIGS / "feature_histograms.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Feature correlation matrix")
    plt.tight_layout()
    plt.savefig(FIGS / "correlation_heatmap.png", dpi=150)
    plt.close()

    df.to_csv(PROCESSED / "diabetes_flagged.csv", index=False)

    print("EDA complete. Outputs written to reports/ and data/processed/")


if __name__ == "__main__":
    main()
