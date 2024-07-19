import requests
import zipfile
import os

# Define constants for the GitHub repository and asset
GITHUB_REPO = 'SCR-ATOmatic/ATOmatic'
ASSET_NAME = 'ATOmatic.zip'
DOWNLOAD_URL_TEMPLATE = f'https://github.com/{GITHUB_REPO}/releases/latest/download/{ASSET_NAME}'
TEMP_FILE = 'temp_update.zip'  # Temporary file name for the downloaded zip
TARGET_DIR = 'ATOmatic'  # Directory to extract files into

# Function to download a file from a URL
def download_file(url, local_filename):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check for HTTP errors
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

# Function to extract a zip file to a specified directory
def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Main function to handle the download and extraction process
def main():
    # Create the target directory if it doesn't exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Download the latest release
    print('Downloading latest release...')
    download_file(DOWNLOAD_URL_TEMPLATE, TEMP_FILE)
    print('Download complete.')

    # Extract the downloaded zip file
    print('Extracting files...')
    extract_zip(TEMP_FILE, TARGET_DIR)
    print('Extraction complete.')

    # Clean up temporary file
    os.remove(TEMP_FILE)
    print('Temporary file cleaned up.')

# Entry point for the script
if __name__ == '__main__':
    main()

# Wait for user input before exiting
input("Press Enter to exit...")
