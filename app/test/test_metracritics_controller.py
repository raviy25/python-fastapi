from unittest import TestCase

from controller.metacritics_controller import GamesController
from test.FakeWebParser import FakeWebParser, Test_Data


class GamesControllerTests(TestCase):

    def setUp(self):
        self.sut = GamesController(FakeWebParser())

    def test_when_all_games_return_data_success( self ):
        # Act
        result = self.sut.get_all_games()

        # Assert
        self.assertListEqual(result, Test_Data)
        self.assertListEqual(self.sut.all_games, Test_Data)
        self.assertIsInstance(self.sut.web_parser, FakeWebParser)

    def test_game_by_title( self ):
        result = self.sut.get_game_by_title("Title1")

        # Assert
        self.assertEqual(result, Test_Data[0])

    def test_game_by_title_when_title_is_not_present( self ):
        result = self.sut.get_game_by_title("blahblah")

        # Assert
        self.assertEqual(result, {})

    def test_game_by_title_when_all_games_cache_is_empty( self ):
        # Arrange
        self.sut.all_games = []

        # Act
        result = self.sut.get_game_by_title("Title2")

        # Assert
        self.assertEqual(result, Test_Data[1])
