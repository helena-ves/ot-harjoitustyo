import unittest
from sudoku_matrix import SudokuMatrix
from check_correctedness import rows, columns, squares

class testSudokuMatrix(unittest.TestCase):
    def setUp(self):
        self.easy = SudokuMatrix('easy')
        self.medium = SudokuMatrix('medium')
        self.hard = SudokuMatrix('hard')

    def test_if_correct_rows_pass(self):
        self.assertEqual(rows(self.easy), True)
        self.assertEqual(rows(self.medium), True)
        self.assertEqual(rows(self.hard), True)

    def test_if_correct_columns_pass(self):
        self.assertEqual(columns(self.easy), True)
        self.assertEqual(columns(self.medium), True)
        self.assertEqual(columns(self.hard), True)
