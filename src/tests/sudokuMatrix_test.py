import unittest
from sudoku_matrix import SudokuMatrix

class testSudokuMatrix(unittest.TestCase):
    def setUp(self):
        self.easy = SudokuMatrix('easy')
        self.medium = SudokuMatrix('medium')
        self.hard = SudokuMatrix('hard')

    def test_if_matrix_exist(self):
        self.assertIsNotNone(self.easy)
        self.assertIsNotNone(self.medium)
        self.assertIsNotNone(self.hard)

    def test_if_matrix_has_correct_amount_of_rows(self):
        self.assertEqual(helper_count_rows(self.easy), 9)
        self.assertEqual(helper_count_rows(self.medium), 9)   
        self.assertEqual(helper_count_rows(self.hard), 9)  
    
    def test_if_matrix_has_correct_length_of_rows(self):
        for num in helper_count_lengths(self.easy):
            self.assertEqual(num, 9)
        for num in helper_count_lengths(self.medium):
            self.assertEqual(num, 9)
        for num in helper_count_lengths(self.hard):
            self.assertEqual(num, 9)

    def test_if_row_contains_same_numbers(self):
        for row in self.easy:
            self.assertEqual(helper_row_contains_same_numbers(row), False)
        for row in self.medium:
            self.assertEqual(helper_row_contains_same_numbers(row), False)
        for row in self.hard:
            self.assertEqual(helper_row_contains_same_numbers(row), False)

    def test_if_insert_number_updates_the_matrix(self):
        easy_updated = SudokuMatrix('easy').insert_number(5, (0, 0))
        medium_updated = SudokuMatrix('medium').insert_number(5, (0, 0))
        hard_updated = SudokuMatrix('hard').insert_number(5, (0, 0))
        



def helper_row_contains_same_numbers(row):
    sameNumbers = False
    numbers = set([])
    for number in row:
        if number > 0:
            if number in numbers:
                sameNumbers = True
            if number not in numbers:
                numbers.add(number)
    return sameNumbers

def helper_count_lengths(matrix):
    lengths = []
    for row in matrix:
        lengths.append(len(row))
    return lengths

def helper_count_rows(matrix):
    amount = 0
    for row in matrix:
        if row:
            amount += 1
    return amount