import fileService

class SudokuMatrix:
    def __init__(self, level: str):
        self.level = level
        fromfile = fileService.FileService("easysudoku.txt")
        self.matrix = fromfile.createMatrix(self.level)

    def getRow(self, number: int):
        return self.matrix[number]
    
    def getColumn(self, number: int):
        column = []
        for row in self.matrix:
            column.append(row[number])
        return column
    
    def __str__(self):
        sudokustring = ""
        for row in self.matrix:
            for c in row:
                if c < 0:
                    sudokustring += str(c) + " "
                else:
                    sudokustring += " " + str(c) + " "
            sudokustring += "\n"
        return sudokustring