
def rows(matrix: list):
    items = []
    for row in matrix:
        for num in row:
            if num not in items and num > 0:
                items.append(num)
    for item in items:
        if items.count(item) > 1:
            return False
    return True

def columns(matrix: list):
    column = 0
    while column < 9:
        numbers = []
        for row in matrix:
            if numbers.count(row[column]) > 0:
                return False
            if row[column] > 0:
                numbers.append(row[column])
        column += 1
    return True

def squares(matrix: list):
    if matrix:
        return True
