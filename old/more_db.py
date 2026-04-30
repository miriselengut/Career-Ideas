from playwright.sync_api import sync_playwright

URL = "https://www.bls.gov/emp/tables/top-skills-by-detailed-occupation.htm"

def scrape(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)
        html = page.content()

        browser.close()
        return html


if __name__ == "__main__":
    html = scrape(URL)
    print(html[:1000])  # just confirm it worked