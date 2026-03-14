"""
ICD-10-CM April 2025 Order File → CSV Converter

Parses the fixed-width CDC order file and produces a clean CSV
containing only valid diagnosis codes with enhanced descriptions.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import pandas as pd

# Minimum line length required by the CDC fixed-width format.
# Positions: 0-5 order, 6-12 code, 14 valid flag, 16-76 short desc, 77+ long desc
_MIN_LINE_LEN = 16


def parse_order_file(file_path: str | Path) -> pd.DataFrame:
    """
    Parse the ICD-10-CM order file and return *all* rows (headers + valid codes)
    as a DataFrame.  Useful for exploratory analysis.
    """
    file_path = Path(file_path)
    records: list[dict[str, object]] = []

    with file_path.open(encoding="utf-8") as fh:
        for line in fh:
            if len(line.strip()) < _MIN_LINE_LEN:
                continue  # skip empty / malformed lines

            code = line[6:13].strip()
            is_header = line[14] == "0"
            long_desc = line[77:].strip() if len(line) > 77 else line[16:76].strip()
            records.append(
                {
                    "code": code,
                    "is_header": is_header,
                    "description": long_desc,
                }
            )

    return pd.DataFrame(records)


def process_order_file(file_path: str | Path, output_csv_path: str | Path) -> int:
    """
    Process the ICD-10-CM order file and write valid codes to CSV
    with parent-header context baked into each description.

    Returns the number of valid-code rows written.
    """
    file_path = Path(file_path)
    output_csv_path = Path(output_csv_path)
    row_count = 0

    with (
        file_path.open(encoding="utf-8") as fh,
        output_csv_path.open("w", newline="", encoding="utf-8") as csv_file,
    ):
        writer = csv.writer(csv_file)
        writer.writerow(["code", "description"])

        last_header_code = ""
        last_header_long_desc = ""

        for line in fh:
            if len(line.strip()) < _MIN_LINE_LEN:
                continue  # skip empty / malformed lines

            code = line[6:13].strip()
            is_valid = line[14]
            long_description = (
                line[77:].strip() if len(line) > 77 else line[16:76].strip()
            )

            if is_valid == "0":
                last_header_code = code
                last_header_long_desc = long_description
                continue

            if is_valid == "1":
                enhanced_desc = (
                    f"Header: {last_header_code} - {last_header_long_desc} "
                    f"| Specific long description about this code: {long_description}"
                )
                writer.writerow([code, enhanced_desc])
                row_count += 1

    return row_count


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert CDC ICD-10-CM fixed-width order file to CSV.",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=None,
        help="Path to the order .txt file (default: icd10cm-order-April-2025.txt next to this script)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path for the output CSV (default: icd10cm_data.csv next to this script)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = _build_parser().parse_args(argv)

    script_dir = Path(__file__).resolve().parent
    order_file_path: Path = args.input or (script_dir / "icd10cm-order-April-2025.txt")
    output_path: Path = args.output or (script_dir / "icd10cm_data.csv")

    if not order_file_path.exists():
        print(f"Error: Order file not found at {order_file_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing order file: {order_file_path}")
    row_count = process_order_file(order_file_path, output_path)
    print(f"Conversion complete — {row_count:,} valid codes written to {output_path}")


if __name__ == "__main__":
    main()
