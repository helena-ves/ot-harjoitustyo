import sqlite3
import random

class DataService:
    def __init__(self):
        self.database = sqlite3.connect("src/resources/data.db")
        self.database.isolation_level = None

    def format(self, sudoku):
        i = 0
        characters = sudoku[0]
        matrix = []
        while i < 9:
            chars = characters[i].strip().split(",")
            numbers = []
            for c in chars:
                numbers.append(int(c))
            matrix.append(numbers)
            i += 1
        return matrix

    def create_matrix(self, level: str):
        if level == 'easy':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Easy WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        if level == 'medium':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Medium WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        if level == 'hard':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Hard WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        return matrix
