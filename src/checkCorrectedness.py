
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
    return True

def squares(matrix: list):
    return True