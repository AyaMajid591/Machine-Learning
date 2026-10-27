"""
load_data.py
Loads the raw Pima Indians Diabetes CSV, applies column names, and flags
biologically impossible zero values as missing (NaN) for the columns where
zero cannot be a true measurement. Does NOT impute — imputation is a modeling
decision left for later in the semester.

Usage:
    from src.load_data import load_raw, load_flagged
    df_raw = load_raw()
    df = load_flagged()
"""

from pathlib import Path
import pandas as pd

RAW_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "diabetes.csv"

COLUMN_NAMES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome",
]

ZERO_AS_MISSING_COLUMNS = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
]


def load_raw() -> pd.DataFrame:
    df = pd.read_csv(RAW_PATH, header=None, names=COLUMN_NAMES)
    return df


def load_flagged() -> pd.DataFrame:
    df = load_raw()
    for col in ZERO_AS_MISSING_COLUMNS:
        df[col] = df[col].replace(0, pd.NA)
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


if __name__ == "__main__":
    df = load_raw()
    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head())
