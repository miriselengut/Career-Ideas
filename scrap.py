import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.bls.gov/emp/tables.htm",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0", 
    "Accept-Encoding": "gzip, deflate, br",
    "Host":"www.bls.gov", 
    "Sec-Ch-Ua":'"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":'"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

def scrape(url):
    try:
        html = requests.get(url,headers=DEFAULT_HEADERS,timeout=20)
        html.raise_for_status()
        soup = BeautifulSoup(html.text, 'html.parser')
        table = soup.find("tbody")
        lines = table.find_all("tr")
        return lines
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

def get_data(lines):
    data = []
    # put data from URL into data list
    for line in lines:
        cols = line.find_all("td")
        names = line.find("p")
        "job_name" = names.get_text()
        data.append({
            "job_name": "".join(c for c in names.get_text() if not (c.isdigit() or c in "[]")),
            "matrix_code": cols[0].get_text(), 
            "self_employed": cols[5].get_text(), 
            "openings": cols[6].get_text(), 
            "salary": cols[7].get_text(),
            "education_needed": cols[8].get_text(),
            "skill_one": cols[9].get_text(),
            "skill_two": cols[10].get_text(),
            "skill_three": cols[11].get_text(),
        })
    return data

def return_data():
    lines = scrape("https://www.bls.gov/emp/tables/top-skills-by-detailed-occupation.htm")
    data = get_data(lines)
    return data
