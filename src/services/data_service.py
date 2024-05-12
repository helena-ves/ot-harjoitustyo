import sqlite3
import random
import uuid

class DataService:
    """Class taking care of drawing data from database, updating it and saving it.
    """
    def __init__(self):
        self.database = sqlite3.connect("src/resources/data.db")
        self.database.isolation_level = None

    def format(self, sudoku):
        """A helper function to format matrix.
        """
        i = 0
        characters = sudoku[0]
        matrix = []
        while i < 9:
            chars = characters[i].strip().split(",")
            numbers = []
            for c in chars:
                numbers.append(int(c))
            matrix.append(numbers)
            i += 1
        return matrix

    def create_matrix(self, level: str):
        """Function that draws a random matrix from database.
            Args: level str: difficulty level of the matrix
            Returns: a list inside of list, containing numbers.
        """
        if level == 'easy':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Easy WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        if level == 'medium':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Medium WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        if level == 'hard':
            number = random.randint(1, 3)
            sudoku = self.database.execute("""
                        SELECT row0, row1, row2, row3, row4, row5, row6, row7, row8
                        FROM Hard WHERE id = ?
                        """, [number]).fetchall()
            matrix = self.format(sudoku)
            return matrix
        return matrix

    def add_new_player(self, name: str, id: uuid):
        """Adds new player to the database.
        """
        playerid = str(id)
        self.database.execute("""
                        INSERT INTO User (id, name, game_id) VALUES (?, ?, NULL)
                              """, [playerid, name])

    def add_new_game(self, gameplayed: tuple, player_id):
        """Adds new game to the database and updates the player info.
        """
        level = str(gameplayed[0])
        time = int(gameplayed[1])
        id = str(uuid.uuid4())
        player_id = str(player_id)
        self.database.execute("""
                        INSERT INTO Game (id, level, time) VALUES (?, ?, ?)
                              """, [id, level, time])
        self.database.execute("""
                        UPDATE User Set game_id = ? WHERE id = ?
                              """, [id, player_id])


    def get_player(self, name: str):
        """Draws player info from database and returns it.
        """
        player = self.database.execute("""
                SELECT *
                FROM User WHERE name = ?
                """, [name]).fetchall()
        return player
