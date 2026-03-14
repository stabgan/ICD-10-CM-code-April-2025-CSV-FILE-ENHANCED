# ICD-10-CM April 2025 — Enhanced CSV Dataset

Ready-to-use CSV of every valid ICD-10-CM diagnosis code (April 2025 release) with parent-category context baked into each row.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## What's in the box

| File | Description |
|---|---|
| `icd10cm_data.csv` | **74,260 valid codes** with enhanced descriptions (~14 MB) |
| `icd10cm-order-April-2025.txt` | Raw CDC order file (source of truth) |
| `icd10_converter.py` | Python script that produced the CSV |
| `icd10-Order-Files-April-2025.pdf` | Official CDC file-format spec |

## How the data was enhanced

The raw CDC order file mixes header rows (category-level) and valid-code rows in a flat text format with fixed-width columns. The converter script:

1. Parses each line by character position per the CDC spec.
2. Tracks the most recent header (flag `0`) as context.
3. For every valid code (flag `1`), prepends the parent header code + description to the code's own long description.

This means each CSV row is **self-contained** — you don't need to look up the parent category separately.

## CSV schema

```
code,description
```

| Column | Type | Example |
|---|---|---|
| `code` | `string` | `A0100` |
| `description` | `string` | `Header: A010 - Typhoid fever \| Specific long description about this code: Typhoid fever, unspecified` |

The `description` field follows the pattern:

```
Header: <parent_code> - <parent_description> | Specific long description about this code: <code_description>
```

## Quick start

### Use the CSV directly

```python
import pandas as pd

df = pd.read_csv("icd10cm_data.csv")
print(df.shape)        # (74260, 2)
print(df.head())
```

### Regenerate from source

```bash
python icd10_converter.py
```

Requires Python 3.6+ and `pandas`. Reads `icd10cm-order-April-2025.txt` and writes `icd10cm_data.csv`.

## Data source

[CDC ICD-10-CM Order Files — April 2025 Update](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025-Update/)

## License

MIT — see [LICENSE](LICENSE).
