# XML_to_CSV-XLSX_Converter

📌 Project Overview
This project is a Python script that converts XML-based Excel (.xls) files into structured CSV (.csv) and Excel (.xlsx) formats.

🚀 Features
✅ Parses and reads .xls files in XML format
✅ Extracts tabular data into a structured Pandas DataFrame
✅ Saves the extracted data as .csv and .xlsx
✅ Error handling for missing files and parsing failures

🛠 Prerequisites
Ensure you have Python 3.7+ installed. Install required dependencies:
pip install pandas openpyxl

📝 Usage
Run the script to convert an XML-based .xls file:
python script.py

🔹 Key Steps:
File Validation: Checks if the input .xls file exists
Parsing XML: Reads XML using ElementTree
Namespace Handling: Extracts data using correct Excel XML namespace
Data Extraction: Iterates through <Row> and <Cell> elements
Data Formatting: Cleans and structures into a Pandas DataFrame
Saving Output: Exports data as CSV and Excel (.xlsx)
