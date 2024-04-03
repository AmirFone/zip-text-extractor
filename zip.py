import zipfile
import os
import json

def extract_text_from_zip(zip_file, file_path):
    result = {}

    for file_info in zip_file.infolist():
        if file_info.filename.startswith(file_path):
            relative_path = file_info.filename[len(file_path):]
            if relative_path and not relative_path.endswith('/'):
                # If it's a file, extract its text content
                with zip_file.open(file_info) as file:
                    try:
                        file_content = file.read().decode('utf-8')
                        result[relative_path] = file_content
                    except UnicodeDecodeError:
                        print(f"Skipping file: {relative_path} (non-UTF-8 encoding)")

    return result

# Specify the path to your zip file
zip_file_path = '/Users/amirhossain/Desktop/Cornell/Angel/cs5435-hw3-master.zip'

# Extract text from the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
    text_data = extract_text_from_zip(zip_file, '')

# Save the extracted text data as a JSON file
output_file = 'extracted_text.json'
with open(output_file, 'w') as json_file:
    json.dump(text_data, json_file, indent=4)

print(f"Text extraction completed. Results saved to {output_file}.")