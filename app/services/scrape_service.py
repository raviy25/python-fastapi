import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url: str):
        self.url = url

    def scrape(self) -> BeautifulSoup:
        try:
            with requests.Session() as session:
                session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2)'
                response = session.get(self.url)

            return BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Error occured while scraping {e}")
            return None

