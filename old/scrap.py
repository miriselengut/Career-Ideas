import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.bls.gov/emp/tables/top-skills-by-detailed-occupation.htm"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.bls.gov/",
}

def soup_from_url(url: str, headers: dict | None = None) -> BeautifulSoup:
    h = DEFAULT_HEADERS.copy()

    if headers:
        h.update(headers)

    r = requests.get(url, headers=h, timeout=30)
    r.raise_for_status()

    return BeautifulSoup(r.text, "html.parser")


soup = soup_from_url(URL)
print(soup.prettify()[:1000])