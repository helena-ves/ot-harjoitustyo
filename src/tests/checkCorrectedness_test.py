import unittest
from sudoku_matrix import SudokuMatrix
from check_correctedness import rows, columns, squares

class testSudokuMatrix(unittest.TestCase):
    def setUp(self):
        self.easy = SudokuMatrix('easy')
        self.medium = SudokuMatrix('medium')
        self.hard = SudokuMatrix('hard')

    def test_if_correct_rows_pass(self):
        self.assertEqual(rows(self.easy), (True, -1))
        self.assertEqual(rows(self.medium), (True, -1))
        self.assertEqual(rows(self.hard), (True, -1))

    def test_if_correct_columns_pass(self):
        self.assertEqual(columns(self.easy), (True, -1))
        self.assertEqual(columns(self.medium), (True, -1))
        self.assertEqual(columns(self.hard), (True, -1))

    def test_if_correct_squares_pass(self):
        self.assertEqual(squares(self.easy), (True, -1))
        self.assertEqual(squares(self.medium), (True, -1))
        self.assertEqual(squares(self.hard), (True, -1))