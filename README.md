# Zip Text Extractor

A Python script to extract text from files within a zip archive and store the file paths and their corresponding text contents in a JSON format.

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/AmirFone/zip-text-extractor.git
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
  ```
  ex:
      Skipping file: cs5435-hw3-master/app/api/__pycache__/__init__.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/admin.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/encr_decr.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/hash_table.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/login.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/pay.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/profile.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/api/__pycache__/static.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/models/__pycache__/__init__.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/models/__pycache__/base.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/models/__pycache__/session.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/models/__pycache__/user.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/scripts/__pycache__/__init__.cpython-35.pyc (non-UTF-8 encoding)
      Skipping file: cs5435-hw3-master/app/scripts/__pycache__/registration.cpython-35.pyc (non-UTF-8 encoding)
  ```

- The resulting JSON file will have the file paths (including directory names) as keys and their corresponding text contents as values.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
