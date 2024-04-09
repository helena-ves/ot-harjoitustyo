
class FileService:
    def __init__(self, file):
        self.file = file

    def createMatrix(self, level: str):
        print('level: ', level)
        path = f"src/{self.file}"
        matrix = []
        if level == 'easy':
            with open(path) as newFile:
                for row in newFile:
                    characters = row.strip().split(",")
                    numbers = []
                    for c in characters:
                        numbers.append(int(c))
                    matrix.append(numbers)
            return matrix
        
        # todo:
        # if level == 'medium':
        #     return matrix
        # if level == 'hard':
        #     return matrix