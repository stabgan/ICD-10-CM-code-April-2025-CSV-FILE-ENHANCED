# ICD-10-CM/PCS Order Files Parser

This repository contains a Python script that processes the ICD-10-CM/PCS Order Files for FY2025. The script reads the order file, extracts valid codes along with their enhanced descriptions (by combining header and specific code details), and outputs a clean CSV file.

If you find this project helpful, please ⭐ star the repo!

---

## Overview

The ICD-10-CM/PCS order files are provided by the CDC and contain a unique order number for each code or header. The files include a flag that indicates whether a line represents a valid code or a header. This project uses the [ICD-10-CM/PCS Order Files for April 2025](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025-Update/) as its source.

### What the Script Does

- **Reads** the input order file (e.g., `icd10cm-order-April-2025.txt`).
- **Extracts**:
  - **Code**: From a specific position in each line.
  - **Header Information**: Stored from lines marked as headers.
  - **Long Description**: From the designated part of the line.
- **Processes** valid codes by combining the header details with their specific long descriptions.
- **Outputs** a CSV file (`icd10cm_data.csv`) containing only valid codes with optimized descriptions.

---

## Repository Structure

```
.
├── icd_10_cm_data
│   └── icd10cm-order-April-2025.txt  # Source order file from CDC
├── processed_data
│   └── icd10cm_data.csv              # Generated CSV with valid codes
├── icd10_converter.py                # Main Python script for processing
└── README.md                         # This file
```

---

## How It Works

1. **Input File**  
   The script reads an order file that includes ICD-10 codes, headers, and descriptions.  
   - **Header Lines**: Identified by a flag (`0`) and used to store common information.
   - **Valid Code Lines**: Identified by a flag (`1`), then enhanced by appending the relevant header's details.

2. **Processing Steps**  
   - Skips any malformed lines.
   - Extracts code and description using fixed character positions based on the file specification.
   - Combines header information with each valid code's specific long description.
   - Writes the processed data into a CSV file.

3. **Output File**  
   The output is a CSV file (`icd10cm_data.csv`) saved in the `processed_data/` directory, containing two columns: `code` and `description`.

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Dependencies (listed in `requirements.txt`, if applicable):
  - `pandas` (used in the unused `parse_order_file` function)

### Installation

1. **Clone the Repository:**

   ```
   git clone https://github.com/stabgan/ICD-10-CM-code-April-2025-CSV-FILE-ENHANCED.git
   cd your_repo
   ```

2. **Install Dependencies:**

   If you have a `requirements.txt`, run:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Place the downloaded ICD-10-CM order file (`icd10cm-order-April-2025.txt`) inside the `icd_10_cm_data/` folder.
2. Run the script:

   ```
   python your_script.py
   ```

3. The processed CSV file will be generated in the `processed_data/` directory.

---

## Source and Acknowledgments

- **Source Data:**  
  The ICD-10-CM/PCS Order Files for FY2025 were downloaded from the [CDC FTP site](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025-Update/).

- **Documentation:**  
  For detailed specifications of the file format, refer to the included [icd10-Order-Files-April-2025.pdf](icd10-Order-Files-April-2025.pdf).

---

## Contributing

Contributions are welcome! If you have ideas for improvements or bug fixes, please open an issue or submit a pull request.

---

## Star the Repo!

If you found this project helpful, please give it a star on GitHub. Your support is greatly appreciated!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
