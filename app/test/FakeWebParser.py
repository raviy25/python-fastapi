from abc import ABC

from models.games_model import Game
from utils.parsers.WebParser import WebParser

DUMMY_URL = "http://test"

Test_Data = [
    Game("Title1", 92),
    Game("Title2", 62),
    Game("Title3", 84),
]

class FakeWebParser(WebParser):

    def __init__(self):
        super().__init__(DUMMY_URL)

    def parse( self ):
        return Test_Data
