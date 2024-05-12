import unittest
from services.sudoku_matrix import SudokuMatrix
from services.check_correctedness import rows, columns, squares

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

    def test_if_false_rows_are_found(self):
        false = [[1, 1, 6, 2, -1, 8, 9, -1, 4],
                [-1, -1, 2, -1, 4, -1, -1, 1, -1],
                [-1, 9, 4, 7, -1, -1, -1, 5, 6],
                [2, 8, 1, -1, -1, -1, -1, -1, 7],
                [-1, -1, 3, -1, -1, -1, 6, -1, -1],
                [4, -1, -1, -1, -1, -1, 3, 2, 5],
                [1, 4, -1, -1, -1, 2, 5, 6, -1],
                [-1, 2, -1, -1, 9, -1, 1, -1, -1],
                [3, -1, 9, 5, -1, 1, 8, -1, -1]]
        self.assertEqual(rows(false), (False, 0))
        self.assertEqual(columns(false), (False, 0))
        self.assertEqual(squares(false), (False, (0, 0)))