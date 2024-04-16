import sudoku_matrix
import check_correctedness

class SudokuApp:
    def __init__(self):
        self.sudoku = None
        self.level = ''

    def set_matrix(self):
        self.sudoku = sudoku_matrix.SudokuMatrix(self.level)

    def check_progress(self):
        if check_correctedness.rows(self.sudoku):
            if check_correctedness.columns(self.sudoku):
                if check_correctedness.squares(self.sudoku):
                    return True
        return False

    def start(self):
        while True:
            print('Welcome to play sudoku!')
            print('X - quit')
            print('L - choose level and play')
            print('C - check progress')
            print('I - insert new number')
            command = input(':')
            if command == 'X':
                break
            if command == 'L':
                self.level = input('Choose level - easy, medium, hard: ')
                self.set_matrix()
                print(self.sudoku)
            if command == 'C':
                result = self.check_progress()
                if result:
                    print('All correct!')
                if not result:
                    print('Errors found!')
            if command == 'I':
                row = int(input('Number of row: '))
                column = int(input('Number of column: '))
                number = int(input('Number to insert: '))
                result = self.sudoku.insert_number(number, (row, column))
                if result == 'False coordinates':
                    print('False coordinates')
                if result:
                    print(self.sudoku)


app = SudokuApp()
app.start()
