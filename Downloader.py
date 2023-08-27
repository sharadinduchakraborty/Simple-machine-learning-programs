# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:23:51 2023

@author: shara
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website containing the files
base_url = "https://example.com/files/"

# Directory to save downloaded files
download_directory = "downloaded_files"

# Create the download directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Send an HTTP request to the website
response = requests.get(base_url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all links on the page
links = soup.find_all("a")

# Loop through the links
for link in links:
    file_url = urljoin(base_url, link.get("href"))

    # Check if the link leads to a file (you can add more checks here)
    if file_url.endswith(".pdf") or file_url.endswith(".zip"):
        # Get the filename from the URL
        filename = os.path.join(download_directory, os.path.basename(file_url))
        
        # Download the file
        with open(filename, "wb") as file:
            file_response = requests.get(file_url)
            file.write(file_response.content)

        print(f"Downloaded: {filename}")

print("Download process completed.")
