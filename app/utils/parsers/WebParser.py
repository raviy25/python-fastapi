from abc import ABC,abstractmethod
from services.scrape_service import WebScraper

class WebParser(ABC):

    def __init__(self, url):
        self.url = url
        self.scraper = WebScraper(url)

    @abstractmethod
    def parse(self):
        pass
