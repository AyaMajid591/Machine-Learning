# Semester Project — Diabetes Risk Analysis (Pima Indians Diabetes Database)

## 1. Environment setup (reproducible)

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

All library versions are pinned in `requirements.txt` (generated against the
exact versions used to build this repo: pandas 3.0.2, numpy 2.4.4,
matplotlib 3.10.8, seaborn 0.13.2, scikit-learn 1.8.0). This guarantees the
analysis reproduces identically regardless of when or where it's re-run.

## 2. Dataset and why it was chosen

**Pima Indians Diabetes Database** — 768 patient records, 8 diagnostic
measurements + binary diabetes outcome. Source and license details in
`data/raw/SOURCE.md`; full column descriptions in `docs/data_dictionary.md`.

**Why this dataset fits a health/medicine/biology semester project:**
- It's a genuine clinical/diagnostic dataset (real measurements: glucose,
  blood pressure, BMI, insulin, family-history score) rather than a toy or
  synthetic one — the kind of tabular clinical data commonly analyzed in
  applied biomedical statistics and ML coursework.
- It has a clear, clinically meaningful binary target (diabetes diagnosis),
  which supports the full semester arc: EDA now → feature engineering →
  classification modeling → evaluation → possibly fairness/bias discussion
  later (the cohort is a single ethnic group, which itself raises questions
  worth discussing in a health-data context).
- It has *realistic data quality problems* (roughly 0.7%–48.7% disguised
  missing values across five columns, see `docs/data_dictionary.md`) —
  useful for demonstrating real data-cleaning decisions rather than working
  with an already-pristine dataset.
- It's small enough (768 rows) to iterate on quickly all semester, but rich
  enough (9 columns, mixed distributions, class imbalance ~65/35) to support
  non-trivial analysis.
- It's hosted on a stable, freely-accessible mirror with no authentication
  or API key required, so the pipeline in this repo runs unattended anywhere.

## 3. Repository structure

```
project/
├── README.md                    <- you are here
├── requirements.txt              <- pinned dependencies
├── data/
│   ├── raw/                      <- original, untouched data (never edit these files)
│   │   ├── diabetes.csv
│   │   └── SOURCE.md             <- provenance, license, retrieval date
│   └── processed/                <- cleaned/derived data, regenerable by scripts
│       └── diabetes_flagged.csv  <- raw data with implausible zeros -> NaN
├── src/                           <- reusable Python modules (import, don't copy-paste)
│   ├── load_data.py               <- single source of truth for loading the data
│   └── eda.py                     <- primary exploratory analysis script
├── notebooks/                     <- exploratory/scratch notebooks (one per topic/week)
├── reports/                       <- generated outputs (tables), regenerable, can be committed
│   ├── summary_statistics.csv
│   ├── missingness_report.csv
│   └── figures/                   <- generated plots
│       ├── target_balance.png
│       ├── feature_histograms.png
│       └── correlation_heatmap.png
└── docs/
    └── data_dictionary.md         <- feature-by-feature description
```

**Design principles for reuse through the semester:**
- `data/raw/` is read-only in practice — nothing in `src/` ever writes there.
  This means the analysis can always be regenerated from a known starting point.
- `data/processed/` and `reports/` hold *generated* artifacts. They're
  reproducible by re-running `src/eda.py`, so if the cleaning logic changes,
  just re-run the script rather than hand-editing outputs.
- `src/load_data.py` centralizes data loading and the zero-as-missing
  cleaning logic, so every future notebook or script imports from here
  instead of re-implementing loading/cleaning inconsistently.
- `notebooks/` is for exploration only — anything that becomes a stable,
  reusable step (a cleaning function, a metric, a plotting helper) should
  graduate into `src/`.
- New modeling work later in the semester can add `src/model.py`,
  `src/features.py`, etc., following the same pattern.

## 4. Running the analysis

```bash
python3 src/eda.py
```

This regenerates everything under `reports/` and `data/processed/` from
`data/raw/diabetes.csv`.

## 5. Key initial findings

- 768 patients, 8 numeric features, binary target `Outcome`
  (~65% no diabetes / ~35% diabetes — see `reports/figures/target_balance.png`).
- Five columns contain disguised missing values encoded as `0`
  (`Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`); missingness
  ranges from 0.7% (`Glucose`) to 48.7% (`Insulin`) — see
  `reports/missingness_report.csv`.
- See `reports/figures/correlation_heatmap.png` for feature relationships
  (e.g. `Glucose` and `BMI` show the strongest association with `Outcome`)
  and `reports/figures/feature_histograms.png` for individual distributions.
