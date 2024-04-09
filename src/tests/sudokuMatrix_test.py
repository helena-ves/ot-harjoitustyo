import unittest
from sudokuMatrix import SudokuMatrix
from fileService import FileService

class testSudokuMatrix(unittest.TestCase):
    def setUp(self):
        self.files = FileService('easysudoku.txt')
        self.matrix = self.files.createMatrix('easy')

    def test_if_matrix_exist(self):
        self.assertIsNotNone(self.matrix)

    def matrix_has_correct_amount_of_rows(self):
        amount = 0
        for row in self.matrix:
            if row:
                amount += 1
        self.assertEqual(amount, 9)
