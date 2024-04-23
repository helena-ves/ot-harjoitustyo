import sudoku_matrix
import check_correctedness

class SudokuApp:
    def __init__(self):
        self.sudoku = None
        self.level = ''

    def set_matrix(self):
        self.sudoku = sudoku_matrix.SudokuMatrix(self.level)

    def check_progress(self):
        rows = check_correctedness.rows(self.sudoku)
        columns = check_correctedness.columns(self.sudoku)
        squares = check_correctedness.squares(self.sudoku)
        if rows[0] is True:
            if columns[0] is True:
                if squares[0] is True:
                    print('All correct!')
        if squares[0] is False:
            print(f'Errors found in square in coordinates {squares[1]} ')
        if columns[0] is False:
            print(f'Errors found in column number {columns[1]}')
        if rows[0] is False:
            print(f'Errors found on row number {rows[1]}')
        print()

    def start(self):
        print('Welcome to play sudoku!')
        while True:
            print('X - quit')
            print('L - choose level and play')
            print('C - check progress')
            print('I - insert new number')
            command = input(':')
            if command == 'X':
                break
            if command == 'L':
                self.level = input('Choose level - easy, medium, hard: ').lower().strip()
                self.set_matrix()
                print(self.sudoku)
            if command == 'C':
                self.check_progress()
            if command == 'I':
                row = int(input('Number of row: '))
                column = int(input('Number of column: '))
                number = int(input('Number to insert: '))
                if number > 9 or number < 1:
                    print()
                    print('Number to insert must be from 1 to 9.')
                    print()
                if row > 8 or row < 0:
                    print()
                    print('Number of row must be from 0 to 8.')
                    print()
                if column > 8 or column < 0:
                    print()
                    print('Number of column must be from 0 to 8.')
                    print()
                else:
                    result = self.sudoku.insert_number(number, (row, column))
                    if result == 'False coordinates':
                        print('False coordinates: slot was not empty')
                    if result:
                        print(self.sudoku)


app = SudokuApp()
app.start()
