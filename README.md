# Monthly Excel Data Separator - Python Script

This repository contains a Python script that reads a large Excel file and separates the data into monthly segments, saving each month's data into a separate Excel file. This script is specifically designed to break down large datasets into manageable monthly segments for easier handling.

## Features

- Read and process Excel files.
- Convert 'date' column to `datetime` type and remove time information.
- Remove percentage signs from 'production_percentage' column and round the values to integers.
- Group data by month and save as separate Excel files for each month.

## Usage

1. Ensure the Pandas library is installed in your Python environment.
2. Download the `split_and_save_excel.py` file from the repository.
3. Run the script, specifying the path to the Excel file you wish to process.

```python
split_and_save_excel('your_path/your_excel_file.xlsx')
