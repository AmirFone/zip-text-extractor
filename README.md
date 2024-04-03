# Zip Text Extractor

A Python script to extract text from files within a zip archive and store the file paths and their corresponding text contents in a JSON format.

## Usage

1. Clone the repository:
   ```
   git clone [https://github.com/yourusername/zip-text-extractor.git](https://github.com/AmirFone/zip-text-extractor.git)
   ```

2. Navigate to the repository directory:
   ```
   cd zip-text-extractor
   ```

3. Run the script:
   ```
   python zip_text_extractor.py /path/to/your/zipfile.zip
   ```
   Replace `/path/to/your/zipfile.zip` with the actual path to your zip file.

4. The script will extract the text from all files within the zip archive, including those inside nested directories, and store the file paths and their corresponding text contents in a JSON file named `extracted_text.json` in the same directory as the script.

## Requirements

- Python 3.x

## Notes

- The script assumes that the text files within the zip archive are encoded in UTF-8. If a file cannot be decoded using UTF-8, it will be skipped, and a message will be printed indicating the skipped file.

- The resulting JSON file will have the file paths (including directory names) as keys and their corresponding text contents as values.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
