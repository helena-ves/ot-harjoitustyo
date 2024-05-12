import unittest
from services.user import User
from services.data_service import DataService
from resources.createdb import initialize_db

class testUser(unittest.TestCase):
    def setUp(self):
        initialize_db()
        self.user = User('tester')

    def test__user_get_name(self):
        self.assertEqual(self.user.get_name(), 'tester')

    def test_user_get_id(self):
        self.assertIsNotNone(self.user.get_id())

    def test_add_game_to_user(self):
        self.user.add_game('easy', 600)
        games = self.user.get_games()
        self.assertGreater(len(games), 0)
        self.assertIsNotNone(games[0])
        self.assertEqual(games[0], ('easy', 600))
