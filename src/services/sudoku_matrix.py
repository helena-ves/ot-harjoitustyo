import services.data_service as data_service

class SudokuMatrix:
    """Class that creates the matrix for the game according to the difficulty level chosen by the player.
        Contains functions to handle the matrix more easily.
        Attributes:
        level: level of difficulty of the matrix
        matrix: matrix derived from the DataService
    """
    def __init__(self, level: str):
        """Initializes the matrix

        Args:
            level (str): level of difficulty
            matrix: the sudoku matrix
        """
        self.level = level
        fromfile = data_service.DataService()
        self.matrix = fromfile.create_matrix(self.level)

    def get_row(self, number: int):
        """Returns the row in question
        Args:
            number (int): the row wanted, from 0 to 8 starting from top
        Returns:
            array: the row of numbers from the matrix
        """
        return self.matrix[number]

    def get_rolumn(self, number: int):
        """Return the column in question
        Args:
            number (int): the column wanted, from 0 to 8 starting from left
        Returns:
            array: the column of numbers from the matrix
        """
        column = []
        for row in self.matrix:
            column.append(row[number])
        return column

    def insert_number(self, number: int, coordinates: tuple):
        """Inserts the number given to the coordinates given
        Args:
            number (int): the number to insert
            coordinates (tuple): the x, y coordinates of the insertion counting from 0 to 8, from left to right and from top to down
        Returns:
            Boolean: whether the insertion was successful
        """
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
