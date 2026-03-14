# ICD-10-CM April 2025 — Enhanced CSV Dataset

Ready-to-use CSV of every valid ICD-10-CM diagnosis code from the April 2025 release, with parent-category context baked into each row.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What It Does

The CDC publishes ICD-10-CM codes as a fixed-width text file that mixes header rows and billable codes. This project parses that file and produces a single, clean CSV where every row is a valid diagnosis code with its parent category already included in the description — no extra lookups needed.

## Dataset

| Property | Value |
|---|---|
| File | `icd10cm_data.csv` |
| Rows | **74,260** valid diagnosis codes |
| Columns | `code`, `description` |
| Release | April 2025 |

### Column Reference

| Column | Type | Example |
|---|---|---|
| `code` | `string` | `A0100` |
| `description` | `string` | `Header: A010 - Typhoid fever \| Specific long description about this code: Typhoid fever, unspecified` |

The `description` field follows the pattern:

```
Header: <parent_code> - <parent_description> | Specific long description about this code: <code_description>
```

## How to Use

### Load the CSV directly

```python
import pandas as pd

df = pd.read_csv("icd10cm_data.csv")
print(df.shape)   # (74260, 2)
print(df.head())
```

### Regenerate from source

```bash
# default paths (reads/writes next to the script)
python icd10_converter.py

# custom paths
python icd10_converter.py -i /path/to/order.txt -o /path/to/output.csv
```

### CLI Options

```
usage: icd10_converter.py [-h] [-i INPUT] [-o OUTPUT]

  -i, --input   Path to the order .txt file (default: icd10cm-order-April-2025.txt)
  -o, --output  Path for the output CSV      (default: icd10cm_data.csv)
```

## Repository Contents

| File | Description |
|---|---|
| `icd10cm_data.csv` | Enhanced CSV with 74,260 valid codes |
| `icd10cm-order-April-2025.txt` | Raw CDC fixed-width order file |
| `icd10_converter.py` | Python converter script |
| `icd10-Order-Files-April-2025.pdf` | Official CDC file-format specification |
| `requirements.txt` | Python dependencies |

## Source

[CDC ICD-10-CM Order Files — April 2025 Update](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025-Update/)

## 🛠 Tech Stack

| | Tool | Purpose |
|---|---|---|
| 🐍 | Python 3.10+ | Script runtime |
| 🐼 | pandas ≥ 2.0 | DataFrame utilities in `parse_order_file()` |
| 📄 | csv (stdlib) | CSV writing |
| 🗂️ | pathlib (stdlib) | Cross-platform path handling |
| ⌨️ | argparse (stdlib) | CLI argument parsing |

## Installation

```bash
pip install -r requirements.txt
```

## ⚠️ Known Issues

- The converter assumes the CDC fixed-width format documented in `icd10-Order-Files-April-2025.pdf`. Future CDC releases may change column positions.

## License

MIT — see [LICENSE](LICENSE).
