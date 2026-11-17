# diabetes-risk-classification

## Setup: installing the required libraries

This project uses **Python 3.13**. All packages (pandas, NumPy, scikit-learn, matplotlib, seaborn, PyTorch, JupyterLab, etc.) are pinned in `requirements.txt` so everyone runs the same versions.

From the root of the repository, create a virtual environment and install everything with **one** of the options below.

**Option A: standard `venv` + `pip` (no extra tools needed)**

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Option B: `uv` (faster, if you have it installed)**

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt
```

Then launch Jupyter with `jupyter lab` and pick the `.venv` kernel.

If you add a new package, install it into your environment and regenerate the file with `pip freeze > requirements.txt` (or `uv pip freeze > requirements.txt`), then let the group know.
