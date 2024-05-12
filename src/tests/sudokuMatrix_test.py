import unittest
import string
from services.sudoku_matrix import SudokuMatrix

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

    def test_if_insert_number_updates_the_matrix_if_cell_is_empty(self):
        easy = self.easy.get_row(0)[0]
        medium = self.medium.get_row(0)[0]
        hard = self.hard.get_row(0)[0]

        easy_updated = self.easy.insert_number(5, (0, 0))
        medium_updated = self.medium.insert_number(5, (0, 0))
        hard_updated = self.hard.insert_number(5, (0, 0))

        if easy == -1:
            self.assertEqual(True, easy_updated)
        else:
            self.assertEqual(False, easy_updated)
        if medium == -1:
            self.assertEqual(True, medium_updated)
        else:
            self.assertEqual(False, medium_updated)
        if hard == -1:
            self.assertEqual(True, hard_updated)
        else:
            self.assertEqual(False, hard_updated)

    def test_matrix_iteration(self):
        for row in self.easy:
            for num in row:
                print(num)
        for row in self.medium:
            for num in row:
                print(num)
        for row in self.hard:
            for num in row:
                print(num)

    def test_str(self):
        easystr = self.easy.__str__()
        mediumstr = self.medium.__str__()
        hardstr = self.hard.__str__()
        for char in easystr:
            self.assertTrue(char in string.printable)  

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