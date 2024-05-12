from services import user_interface

class SudokuApp:
    """Class for starting the user interface of the app
    """
    def __init__(self):
        """Creates the user interface
        """
        self.ui = user_interface.UserInterface()

    def start(self):
        """Starts the GUI of the game
        """
        self.ui.main()

app = SudokuApp()
app.start()
