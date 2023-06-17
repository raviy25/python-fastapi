from typing import List

from models.games_model import Game
from utils.parsers.meta_critic_web_parser import WebParser
from utils.parsers.factory import WebParserFactory
from utils.const import Constansts

class GamesController:

    def __init__(self, web_parser: WebParser):
        self.web_parser = web_parser
        self.all_games: List[Game] = []

    def get_all_games(self):
        self.all_games = self.web_parser.parse()

        return self.all_games

    def get_game_by_title(self, title: str):
        result_game = self.__filter_game_by_title(title)
        if not result_game:
            self.all_games = self.get_all_games()
            result_game = self.__filter_game_by_title(title)
        return result_game

    def __filter_game_by_title(self, title: str):
        filtered_games = list(filter(lambda g: g.title == title, self.all_games))
        return filtered_games[0] if filtered_games else {}


games_controller = GamesController(WebParserFactory[Constansts.METACRITIC_APP_URL])
