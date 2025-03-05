# To Read .xls file (Which is in XML format) and save into .CSV or .XLSX file
import pandas as pd
import xml.etree.ElementTree as ET

file_path = r"C:\Users\MYSystem\Downloads\Dump_March_2025.xls"

# Parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

# Find the namespace (Excel XML files use multiple namespaces)
namespace = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

# Extract rows from the XML
rows = root.findall(".//ss:Table/ss:Row", namespace)

data = []
for row in rows:
    values = [cell.text if cell.text else "" for cell in row.findall("ss:Cell/ss:Data", namespace)]
    data.append(values)

# Convert to DataFrame
df = pd.DataFrame(data)
df = df.dropna(how="all")  # Remove empty rows

# Fix: Reset index properly
df.columns = df.iloc[0].values  # Set first row as column names
df = df[1:].reset_index(drop=True)  # Remove first row and reset index

# Display the DataFrame
print(df.head())

# Save as CSV or `.xlsx`
df.to_csv("converted_file.csv", index=False)
df.to_excel("converted_file.xlsx", index=False)
