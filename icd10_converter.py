import pandas as pd
import os
import csv
from pathlib import Path

def parse_order_file(file_path):
    """
    Parse the ICD-10-CM order file according to the specification.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            code = line[6:13].strip()
            long_desc = line[77:].strip()
            data.append({
                'code': code,
                'description': long_desc
            })
    return pd.DataFrame(data)

def process_order_file(file_path, output_csv_path):
    """
    Process the ICD-10-CM order file and write valid codes to CSV with header information.
    Output only code and optimized description.
    """
    with open(file_path, 'r', encoding='utf-8') as file, open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write simplified header row with only code and description
        csv_writer.writerow(['code', 'description'])
        
        last_header_code = ""    
        last_header_long_desc = ""
        
        for line in file:
            if len(line) < 78:
                continue  # Skip malformed lines
                
            code = line[6:13].strip()
            is_valid = line[14]
            long_description = line[77:].strip() if len(line) > 77 else line[16:76].strip()
            
            # If this is a header, update the last header info
            if is_valid == '0':
                last_header_code = code
                last_header_long_desc = long_description
                continue  # Skip writing header to output
            
            # For valid codes, format the description with header at beginning
            if is_valid == '1':
                enhanced_desc = f"Header: {last_header_code} - {last_header_long_desc} | Specific long description about this code: {long_description}"
                csv_writer.writerow([code, enhanced_desc])

def main():
    # Set file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'icd_10_cm_data')
    order_file_path = os.path.join(data_dir, 'icd10cm-order-April-2025.txt')
    output_path = os.path.join(script_dir, 'processed_data/icd10cm_data.csv')
    
    # Check if order file exists
    if not os.path.exists(order_file_path):
        print(f"Error: Order file not found at {order_file_path}")
        return
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Process and save file
    print(f"Processing order file: {order_file_path}")
    process_order_file(order_file_path, output_path)
    
    print(f"Conversion complete. Output saved to: {output_path}")
    print("Only valid codes with optimized descriptions are included in the output.")

if __name__ == "__main__":
    main()