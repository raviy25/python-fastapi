
from utils.const import Constansts
from utils.parsers.WebParser import WebParser
from models.games_model import Game


class MetaCriticWebParser(WebParser):

    def __init__(self):
        super().__init__(Constansts.METACRITIC_APP_URL)

    def parse( self ):
        return self.__get_top_ps4_games()

    def __get_top_ps4_games(self):
        web_page = self.scraper.scrape()
        games_container = web_page.select(".clamp-list tr .clamp-summary-wrap")
        return [

               Game(
                   game.find("h3").get_text(strip=True),
                   int(game.find("div", class_="clamp-score-wrap").find('a').get_text(strip=True)))
                # 'title': game.find("h3").get_text(strip=True),
                # 'score': int(game.find("div", class_="clamp-score-wrap").find('a').get_text(strip=True))
             for game in games_container
        ]
