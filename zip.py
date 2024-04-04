import zipfile
import os
import json
import io
import PyPDF2
from pptx import Presentation

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

def extract_text_from_pptx(file):
    prs = Presentation(file)
    text = ""
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, 'text'):
                text += shape.text + "\n"
    return text

def extract_text_from_zip(zip_file, file_path):
    result = {}

    for file_info in zip_file.infolist():
        if file_info.filename.startswith(file_path):
            relative_path = file_info.filename[len(file_path):]
            if relative_path and not relative_path.endswith('/'):
                # If it's a file, extract its text content
                with zip_file.open(file_info) as file:
                    try:
                        if file_info.filename.lower().endswith('.pdf'):
                            file_content = extract_text_from_pdf(io.BytesIO(file.read()))
                        elif file_info.filename.lower().endswith('.pptx'):
                            file_content = extract_text_from_pptx(io.BytesIO(file.read()))
                        else:
                            file_content = file.read().decode('utf-8')
                        result[relative_path] = file_content
                    except (PyPDF2._utils.PdfStreamError, ValueError, KeyError, UnicodeDecodeError, AttributeError):
                        print(f"Skipping file: {relative_path} (unsupported format or error occurred)")

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
