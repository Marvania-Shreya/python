"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://pypi.org/project/beautifulsoup4/"

def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    # print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
         # BONUS: remove "[edit]" if it appears in the header
        header_text = header_text.replace("[edit]", "").strip()
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)

    # Print total count and first 10 headers
    print(f"\n✅ Total H2 headers found: {len(headers)}")
    print("\n📘 First 10 section titles:")
    for i, title in enumerate(headers[:10], start=1):
        print(f"{i}. {title}")

    return headers   

get_h2_headers(URL)
