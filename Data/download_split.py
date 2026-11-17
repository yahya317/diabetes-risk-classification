"""Download the Kaggle diabetes dataset and split it into working (80%) and reporting (20%) sets.

This script only downloads and splits; exploratory analysis lives in a separate notebook.
Run from anywhere: `python Data/download_split.py` or the editor's Run button.

- The full CSV is saved to Data/ for local use only (it is git-ignored).
- Each step is skipped if its output already exists, so nothing is re-downloaded
  needlessly and the reporting set is never overwritten once it has been created.
"""

# imports
import shutil
import sys
import time
from pathlib import Path

import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

# Build paths from this file's location, not the current working directory,
# so the CSVs always land in Data/ no matter where the script is run from.
DATA_DIR = Path(__file__).resolve().parent

DATASET = "alexteboul/diabetes-health-indicators-dataset"
CSV_NAME = "diabetes_012_health_indicators_BRFSS2015.csv"
TARGET = "Diabetes_012"
SEED = 42

FULL_PATH = DATA_DIR / CSV_NAME  # keep Kaggle's original file name so its source is obvious
WORK_PATH = DATA_DIR / "working_set.csv"
REPORT_PATH = DATA_DIR / "reporting_set.csv"


def download_full_csv() -> None:
    """Download the 012 CSV from Kaggle and save an untouched copy as FULL_PATH.

    Raises:
        RuntimeError: If the download or the copy fails.
    """
    # perf_counter is a high-resolution timer meant for measuring elapsed time
    start = time.perf_counter()
    try:
        cached_file = kagglehub.dataset_download(DATASET, path=CSV_NAME)
        # Copy the file as-is (rather than read + re-save with pandas) so the raw data stays byte-identical.
        shutil.copy2(cached_file, FULL_PATH)
    except Exception as e:
        # Re-raise so the script stops here with a clear message.
        raise RuntimeError(f"Could not download {CSV_NAME}: {e}") from e
    elapsed = time.perf_counter() - start

    # kagglehub caches the file, so repeat downloads take well under a second
    print(f"Downloaded {CSV_NAME} in {elapsed:.2f} s.")


def split_full_csv() -> None:
    """Split the full CSV into stratified working and reporting sets and save both."""
    df = pd.read_csv(FULL_PATH)

    # stratify keeps the class proportions the same in both sets
    work, report = train_test_split(
        df, test_size=0.20, stratify=df[TARGET], random_state=SEED
    )

    work.to_csv(WORK_PATH, index=False)
    report.to_csv(REPORT_PATH, index=False)

    print(f"Saved {WORK_PATH.name} ({len(work)} rows) and {REPORT_PATH.name} ({len(report)} rows).")


def main() -> None:
    """Download the full CSV and create the split, skipping any step that is already done."""
    if FULL_PATH.exists():
        print(f"{FULL_PATH.name} already exists, skipping download.")
    else:
        download_full_csv()

    if WORK_PATH.exists() and REPORT_PATH.exists():
        print("Working and reporting sets already exist, skipping split.")
    else:
        split_full_csv()


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)  # non-zero exit code signals failure to the terminal / Run button
