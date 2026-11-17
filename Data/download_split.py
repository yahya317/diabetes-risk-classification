"""Download the Kaggle diabetes dataset and split it into working (80%) and reporting (20%) sets.

This script only downloads and splits; exploratory analysis lives in a separate notebook.
Run from anywhere: `python Data/download_split.py` or the editor's Run button.
If both CSVs already exist, nothing is re-downloaded or overwritten, so the
reporting set stays fixed once it has been created.
"""

# imports
import sys
import time
from pathlib import Path

import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

# Build paths from this file's location, not the current working directory,
# so the CSVs always land in Data/ no matter where the script is run from.
DATA_DIR = Path(__file__).resolve().parent
WORK_PATH = DATA_DIR / "working_set.csv"
REPORT_PATH = DATA_DIR / "reporting_set.csv"

DATASET = "alexteboul/diabetes-health-indicators-dataset"
CSV_NAME = "diabetes_012_health_indicators_BRFSS2015.csv"
TARGET = "Diabetes_012"
SEED = 42


def download_data() -> pd.DataFrame:
    """Download the 012 CSV from Kaggle (kagglehub caches it) and load it.

    Returns:
        The full dataset as a DataFrame.

    Raises:
        RuntimeError: If the download or the read fails.
    """
    # perf_counter is a high-resolution timer meant for measuring elapsed time
    start = time.perf_counter()
    try:
        csv_file = kagglehub.dataset_download(DATASET, path=CSV_NAME)
        df = pd.read_csv(csv_file)
    except Exception as e:
        # Re-raise so the script stops here instead of crashing later on an undefined `df`.
        raise RuntimeError(f"Could not download or read {CSV_NAME}: {e}") from e
    elapsed = time.perf_counter() - start

    # kagglehub caches the file, so repeat runs take well under a second
    print(f"CSV file downloaded and read successfully in {elapsed:.2f} s.")
    return df


def main() -> None:
    """Create the working/reporting split if it doesn't already exist."""
    if WORK_PATH.exists() and REPORT_PATH.exists():
        print(f"Split already exists in {DATA_DIR}, skipping.")
        return

    df = download_data()

    # stratify keeps the class proportions the same in both sets
    work, report = train_test_split(
        df, test_size=0.20, stratify=df[TARGET], random_state=SEED
    )

    work.to_csv(WORK_PATH, index=False)
    report.to_csv(REPORT_PATH, index=False)

    print(f"Saved {WORK_PATH.name} ({len(work)} rows) and {REPORT_PATH.name} ({len(report)} rows).")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)  # non-zero exit code signals failure to the terminal / Run button
