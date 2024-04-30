import services.sudoku_matrix as sudoku_matrix
import services.check_correctedness as check_correctedness

class SudokuApp:
    """Class containing the user interface of the app
        Attributes:
        sudoku: contains the sudoku matrix
        level: level of difficulty chosen by the player
    """
    def __init__(self):
        """Creates a placeholder for sudoku matrix and level of difficulty
        """
        self.sudoku = None
        self.level = ''

    def set_matrix(self):
        """Downloads the matrix from SudokuMatrix and sets it to the placeholder
        """
        self.sudoku = sudoku_matrix.SudokuMatrix(self.level)

    def check_progress(self):
        """Check the correctedness of input the player has entered.
            Args: 
            rows: tuple containing Boolean value and coordinates of a possible error
            columns: tuple containing Boolean value and coordinates of a possible error
            squares: tuple containins Boolean value and coordinates of a possible error
        """
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
        """Starts the user interface of the game and prints out output for the user
        Args:
        command: str input by the user
        """
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
