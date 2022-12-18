import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

# Prompt the user for a website URL
url = input("Enter the website URL: ")

# Send a request to the website and get the HTML content
html = requests.get(url).text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the image tags in the HTML
img_tags = soup.find_all('img')

# Create a folder to save the images
if not os.path.exists('images'):
    os.makedirs('images')

# Iterate over the image tags and save the images
for i, img_tag in enumerate(tqdm(img_tags)):
    # Get the image URL
    img_url = img_tag['src']

    # Check if the URL is absolute or relative
    if not img_url.startswith('http'):
        # If it's relative, prepend the website URL
        img_url = url + img_url

    # Split the URL into parts
    parts = img_url.split('/')

    # Get the file name from the last part of the URL
    file_name = parts[-1]

    # Send a request to download the image
    img_data = requests.get(img_url).content

    # Save the image to the folder
    with open(f'images/{file_name}', 'wb') as f:
        f.write(img_data)

print("Done!")