import requests
import zipfile
import os

GITHUB_REPO = 'SCR-ATOmatic/ATOmatic'
ASSET_NAME = 'ATOmatic.zip'
DOWNLOAD_URL_TEMPLATE = f'https://github.com/{GITHUB_REPO}/releases/latest/download/{ASSET_NAME}'
TEMP_FILE = 'temp_update.zip'
TARGET_DIR = 'ATOmatic'

def download_file(url, local_filename):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    print('Downloading latest release...')
    download_file(DOWNLOAD_URL_TEMPLATE, TEMP_FILE)
    print('Download complete.')

    print('Extracting files...')
    extract_zip(TEMP_FILE, TARGET_DIR)
    print('Extraction complete.')

    os.remove(TEMP_FILE)
    print('Temporary file cleaned up.')

if __name__ == '__main__':
    main()

input("Press Enter to exit...")