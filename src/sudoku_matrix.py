import file_service

class SudokuMatrix:
    def __init__(self, level: str):
        self.level = level
        fromfile = file_service.FileService()
        self.matrix = fromfile.create_matrix(self.level)

    def get_row(self, number: int):
        return self.matrix[number]

    def get_rolumn(self, number: int):
        column = []
        for row in self.matrix:
            column.append(row[number])
        return column

    def insert_number(self, number: int, coordinates: tuple):
        if self.matrix[coordinates[0]][coordinates[1]] != -1:
            return 'False coordinates'
        self.matrix[coordinates[0]][coordinates[1]] = number
        return True

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

    def __getitem__(self, x: int):
        return self.matrix[x]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.matrix):
            row = self.matrix[self.n]
            self.n += 1
            return row
        raise StopIteration
