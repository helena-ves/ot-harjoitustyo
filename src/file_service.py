
class FileService:
    def __init__(self):
        self.easy = "easysudoku.txt"
        self.medium = "mediumsudoku.txt"
        self.hard = "hardsudoku.txt"
        self.path = "src/resources/"

    def create_matrix(self, level: str):
        matrix = []
        if level == 'easy':
            with open(self.path + self.easy, encoding="utf-8") as new_file:
                for row in new_file:
                    characters = row.strip().split(",")
                    numbers = []
                    for c in characters:
                        numbers.append(int(c))
                    matrix.append(numbers)
            return matrix
        if level == 'medium':
            with open(self.path + self.medium, encoding="utf-8") as new_file:
                for row in new_file:
                    characters = row.strip().split(",")
                    numbers = []
                    for c in characters:
                        numbers.append(int(c))
                    matrix.append(numbers)
            return matrix
        if level == 'hard':
            with open(self.path + self.hard, encoding="utf-8") as new_file:
                for row in new_file:
                    characters = row.strip().split(",")
                    numbers = []
                    for c in characters:
                        numbers.append(int(c))
                    matrix.append(numbers)
            return matrix
        return matrix
