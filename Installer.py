import os
import zipfile
import sys
import requests

# Welcome message
print("Welcome to the SCR-ATOmatic installer for Windows.")
print("This script will:\n- Download the ATOmatic latest files\n- Download the Updater")

# Prompt user for confirmation to proceed
proceed = input("\nDo you wish to proceed? (Y/n) ")
if proceed.lower() == "n":
    print("Canceled.")
    exit()

# Install the 'requests' module
print("Getting requests module...")
os.system("py -m pip install requests")

# Define the function to download a file from a URL
def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for errors in the request
    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

# Wait for user input to continue
input("Press Enter to continue...")

# Download the ATOmatic repository
print("Downloading ATOmatic repository...")
GITHUB_REPO = 'SCR-ATOmatic/ATOmatic'  # GitHub repository path
ASSET_NAME = 'ATOmatic.zip'  # Asset name in the repository
DOWNLOAD_URL = f'https://github.com/{GITHUB_REPO}/releases/latest/download/{ASSET_NAME}'  # Construct download URL
TEMP_FILE = 'temp_update.zip'  # Temporary file name for the downloaded zip
TARGET_DIR = 'ATOmatic'  # Directory to extract files into

# Download the ATOmatic zip file
print(f"Downloading from {DOWNLOAD_URL}...")
download_file(DOWNLOAD_URL, TEMP_FILE)
print("Download complete.")

# Extract the downloaded zip file
print("Extracting files...")
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)  # Create target directory if it doesn't exist
with zipfile.ZipFile(TEMP_FILE, 'r') as zip_ref:
    zip_ref.extractall(TARGET_DIR)
print("Extraction complete.")

# Clean up temporary file
os.remove(TEMP_FILE)
print("Temporary file cleaned up.")

# Wait for user input to continue
input("Press Enter to continue...")

# Download the Updater script
print("Downloading Updater...")
UPDATER_URL = 'https://raw.githubusercontent.com/SCR-ATOmatic/ATOmatic-Installer/main/Updater.py'  # Updater script URL
UPDATER_TEMP_FILE = 'Updater.py'  # Temporary file name for the Updater script

print(f"Downloading from {UPDATER_URL}...")
download_file(UPDATER_URL, UPDATER_TEMP_FILE)
print("Download complete.")

# Final completion message
print("Installation complete!")

# Wait for user input before exiting
input("Press Enter to exit...")

# Attempt to delete the installer script
try:
    script_path = sys.argv[0]
    print("Deleting installer script...")
    os.remove(script_path)
    print("Installer script deleted.")
except Exception as e:
    print(f"Failed to delete the installer script: {e}")
