import sudokuMatrix
import checkCorrectedness

class sudokuApp:
    def __init__(self, level: str):
        self.level = level
        self.sudoku = sudokuMatrix.SudokuMatrix(level)

    def checkProgress(self):
        if checkCorrectedness.rows(self.matrix) and checkCorrectedness.columns(self.matrix) and checkCorrectedness.squares(self.matrix):
            return True
        return False
    
    def start(self):
        print(self.sudoku)
        return "Sudoku is starting!"
    

app = sudokuApp("easy")
print(app.start())