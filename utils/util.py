import os

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from pywebcopy import save_webpage
from datetime import datetime, timezone

# Check if "www." is in the URL
def ensure_www(url):
    if not url.startswith("http"):
        url = "http://" + url
    parsed_url = urlparse(url)
    if not parsed_url.netloc.startswith("www."):
        new_url = f"{parsed_url.scheme}://www.{parsed_url.netloc}{parsed_url.path}"
        new_url += (f"?{parsed_url.query}" if parsed_url.query else "")
        new_url += (f"#{parsed_url.fragment}" if parsed_url.fragment else "")
        return new_url
    return url

# Save content to a file named after the website
def write_html(url, content):
    filename = url.split("//")[-1].replace("/", "_") + ".html"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Website content saved to '{filename}'")

# Fetch and print metadata
def print_metadata(url, content):
    soup = BeautifulSoup(content, 'html.parser')
    # Count all <a> and <img> tags
    num_links = len(soup.find_all('a'))
    num_images = len(soup.find_all('img'))

    now = datetime.now(timezone.utc)
    print(f"Metadata for {url}:")
    print(f"-> Number of links: {num_links}")
    print(f"-> Number of images: {num_images}")
    print(f"-> Last Fetched Time: {now.strftime('%a %b %d %Y %H:%M UTC')}")

# Mirror the website using pywebcopy package
def mirror_website_assets(url):
    mirror_path = url.split("//")[-1].replace("/", "_")
    os.makedirs(mirror_path, exist_ok=True)
    save_webpage(ensure_www(url), project_folder="/usr/src/app/" + mirror_path, bypass_robots=True)
    print(f"Website mirrored to '{mirror_path}'")