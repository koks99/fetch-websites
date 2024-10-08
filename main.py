import argparse
import requests

from utils.util import write_html, print_metadata, mirror_website_assets

# Main Script Driver Method
def fetch_website(url, fetch_metadata=False, mirror=False):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        write_html(url, content)
        if fetch_metadata:
            print_metadata(url, content)

        if mirror:
            mirror_website_assets(url)

    except Exception as e:
        m = "Error fetching"
        if mirror:
            m = "Error fetching mirror for"
        print(f"{m} {url}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch website content and optionally metadata or mirror the website.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='One or more website URLs to fetch')
    parser.add_argument('--metadata', action='store_true', help='Fetch metadata (number of links and images)')
    parser.add_argument('--mirror', action='store_true', help='Mirror the website (default is no mirroring)')

    args = parser.parse_args()

    for url in args.urls:
        fetch_website(url, args.metadata, mirror=args.mirror)
