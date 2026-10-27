# Data Dictionary — Pima Indians Diabetes Database

Source: `data/raw/diabetes.csv` (see `data/raw/SOURCE.md`). All patients are
female, age 21+, of Pima Indian heritage. n = 768.

| # | Column | Type | Unit / Range | Description | Data quality note |
|---|--------|------|---------------|--------------|--------------------|
| 1 | `Pregnancies` | int | 0–17 | Number of times pregnant | No missing/invalid values |
| 2 | `Glucose` | int | 0–199 | Plasma glucose concentration, 2-hour oral glucose tolerance test (mg/dL) | 5 records (0.7%) recorded as 0 — physiologically impossible, treated as missing |
| 3 | `BloodPressure` | int | 0–122 | Diastolic blood pressure (mm Hg) | 35 records (4.6%) recorded as 0 — treated as missing |
| 4 | `SkinThickness` | int | 0–99 | Triceps skinfold thickness (mm) | 227 records (29.6%) recorded as 0 — treated as missing; high missingness, use with caution |
| 5 | `Insulin` | int | 0–846 | 2-hour serum insulin (mu U/mL) | 374 records (48.7%) recorded as 0 — nearly half missing; treated as missing |
| 6 | `BMI` | float | 0–67.1 | Body mass index, weight in kg / (height in m)^2 | 11 records (1.4%) recorded as 0 — treated as missing |
| 7 | `DiabetesPedigreeFunction` | float | 0.078–2.42 | A function scoring likelihood of diabetes based on family history | No missing/invalid values |
| 8 | `Age` | int | 21–81 | Age in years | No missing/invalid values |
| 9 | `Outcome` | int (binary) | {0, 1} | Target variable: 1 = diabetes diagnosis, 0 = no diabetes | No missing values; class balance ~65% (0) / 35% (1) — see `reports/figures/target_balance.png` |
