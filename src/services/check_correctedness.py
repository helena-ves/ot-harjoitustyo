
def rows(matrix: list):
    """Checks the correctedness of rows in the matrix
    Args:
        matrix (list): the current state of the matrix
    Returns:
        _tuple: contains Boolean value and index number of possible error
    """
    for index, row in enumerate(matrix):
        for num in row:
            if num > 0:
                if row.count(num) > 1:
                    return (False, index)
    return (True, -1)

def columns(matrix: list):
    """Checks the correctedness of columns in the matrix
    Args:
        matrix (list): the current state of the matrix
    Returns:
        tuple: contains Boolean value and index of possible error
    """
    column = 0
    while column < 9:
        numbers = []
        for row in matrix:
            if numbers.count(row[column]) > 0:
                return (False, column)
            if row[column] > 0:
                numbers.append(row[column])
        column += 1
    return (True, -1)

def squares(matrix: list):
    """Checks the correctedness of squares in the matrix
    Args:
        matrix (list): the current state of the matrix
    Returns:
        tuple: contains Boolean value and index of possible error
    """
    starting_points = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    numbers_in_squares = []
    for point in starting_points:
        i = 0
        numbers = []
        point_x = point[0]
        point_y = point[1]
        while i < 3:
            j = 0
            while j < 3:
                numbers.append(matrix[point_x + i][point_y + j])
                j += 1
            i += 1
        numbers_in_squares.append(numbers)
    for index, square in enumerate(numbers_in_squares):
        for n in square:
            if square.count(n) > 1 and n!= -1:
                return (False, starting_points[index])
    return (True, -1)
