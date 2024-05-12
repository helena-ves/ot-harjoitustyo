import unittest
import uuid
from resources.createdb import initialize_db
from services.data_service import DataService

class DataServiceTest(unittest.TestCase):
    def setUp(self):
        self.data_service = DataService()
        initialize_db()

    def test_if_create_matrix_fetches_the_sudoku_grid(self):
        easy = self.data_service.create_matrix('easy')
        medium = self.data_service.create_matrix('medium')
        hard = self.data_service.create_matrix('hard')
        self.assertIsNotNone(easy)
        self.assertIsNotNone(medium)
        self.assertIsNotNone(hard)
        self.assertEqual(len(easy), 9)
        self.assertEqual(len(medium), 9)
        self.assertEqual(len(hard), 9)

    def test_add_new_player(self):
        id = str(uuid.uuid4())
        name = 'tester'
        self.data_service.add_new_player(name, id)
        player = self.data_service.get_player(name)[0]
        self.assertIsNotNone(player)
        self.assertEqual(player[1], 'tester')
        self.assertEqual(player[0], id)
        self.assertEqual(player[2], None)

    def test_add_game_to_the_player(self):
        id = str(uuid.uuid4())
        name = 'tester'
        self.data_service.add_new_player(name, id)
        player = self.data_service.get_player(name)[0]
        gameplayed = ('easy', 600)
        self.data_service.add_new_game(gameplayed, player[0])
        player = self.data_service.get_player(name)[0]
        self.assertIsNotNone(player[2])