import requests
from bs4 import BeautifulSoup
import pandas as pd

#set up scraoing
url = "https://www.payscale.com/data-packages/most-and-least-meaningful-jobs/full-list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("div", class_="hidden-sm hidden-xs")
lines = table.find_all("tr")

def get_data():
    data = []
    # put data from URL into data list
    for line in lines:
        cols = line.find_all("td")
        data.append({
            "job_name": cols[0].get_text(),
            "salary": cols[1].get_text(), 
            "job_satisfaction": cols[2].get_text(), 
            "job_meaning": cols[3].get_text()
        })
    return data 
