import uuid
from services import data_service


class User:
    """Class containing player information.
    """
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.games = []
        self.data_service = data_service.DataService()
        self.data_service.add_new_player(self.name, self.id)

    def add_game(self, level, time):
        """"Function to add completed game to the user.
            Sends the data to DataService.
        """
        gameplayed = (level, time)
        self.games.append(gameplayed)
        self.data_service.add_new_game(gameplayed, self.id)

    def get_games(self):
        """Getter for the games.
        Returns:
            list: the games user has completed
        """
        return self.games

    def get_name(self):
        """Getter for the name
        Returns:
            str: name of the player
        """
        return self.name

    def get_id(self):
        """Getter for the id.
        Returns:
            uuid: id of the player in uuid format.
        """
        return self.id
    