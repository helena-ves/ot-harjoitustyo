import string
import pygame
from services import sudoku_matrix
from services import check_correctedness
from services import user

class UserInterface:
    """Creates the user interface and starts the game. Contains functions for the UI.
    """
    def __init__(self):
        """Initializes the game, creates placeholders for variables needed for the game.
        """
        pygame.init()
        self.matrix = None
        self.user = None
        self.clock = None
        self.start_time = None
        self.original_matrix = []
        self.level = ''
        self.window = pygame.display.set_mode((800, 1000))
        pygame.display.set_caption("Sudoku")
        self.prescreen = True
        self.grid = False
        self.results = False
        self.button1 = pygame.Rect(100, 500, 150, 80) #EASY
        self.button2 = pygame.Rect(300, 500, 150, 80) #MEDIUM
        self.button3 = pygame.Rect(500, 500, 150, 80) #HARD
        self.button4 = pygame.Rect(76, 800, 320, 80) #CHECK PROGRESS
        self.input_field = pygame.Rect(100, 230, 200, 80) # Name of the player
        self.input_field_active = False
        self.input_name = ' '
        self.matrix_buttons = []
        self.cell_coordinates = None
        self.cell_color = (0, 0, 0)
        self.cell_active = False
        self.cell_line = 1
        self.input_digit = None
        self.text = ''
        self.text2 = ''
        self.text3 = ''

    def create_user(self, name: str):
        """Creates a new player
        Args:
            name (str): name of the player
        """
        self.user = user.User(name)


    def set_level_and_matrix(self, level):
        """Downloads the matrix from SudokuMatrix and sets it to the placeholder.
           Copies the original matrix to differentiate between user input and pre-filled numbers.
        """
        self.level = level
        self.matrix = sudoku_matrix.SudokuMatrix(self.level)
        for row in self.matrix:
            copy = []
            for num in row:
                copy.append(num)
            self.original_matrix.append(copy)


    def set_starting_time_for_game(self):
        """Sets the starting time for clock to measure the time it takes to complete the game
        """
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()


    def draw_grid(self):
        """Draws the grid, cell content and buttons
        """
        border = 76
        self.matrix_buttons = []
        for y in range(9):
            row = []
            for x in range(9):
                # Draw lines
                if y % 3 == 0 and y != 0 and x != 0:
                    pygame.draw.line(self.window, (0, 0, 0),
                            (border, (((x//3)*210)+1)+border),
                            (630+border, (((x//3)*210)+1)+border), 5)
                if x % 3 == 0 and x != 0 and y != 0:
                    pygame.draw.line(self.window, (0, 0, 0),
                            ((((x//3)*210)+1+border), border),
                            ((((x//3)*210)+1+border), (630+border)), 5)
                # Draw cell content:
                font = pygame.font.SysFont("Arial", 32)
                text = font.render(" ", True, (0, 0, 0))
                if self.input_digit and self.cell_coordinates == (y, x):
                    if self.matrix[y][x] != -1 and self.original_matrix[y][x] != -1:
                        self.input_digit = None
                        self.cell_coordinates = None
                    else:
                        if self.input_digit != '-1':
                            text = font.render(self.input_digit, True, (0, 0, 0))
                        if self.input_digit == '-1':
                            text = font.render(" ", True, (0, 0, 0))
                        success = self.matrix.insert_number(int(self.input_digit),
                                                            self.cell_coordinates)
                        if success:
                            print('Matrix updated')
                        else:
                            print('Wrong coordinates.')
                        self.input_digit = None
                        self.cell_coordinates = None
                if self.matrix[y][x] != -1:
                    text = font.render(str(self.matrix[y][x]), True, (0, 0, 0))
                rect = pygame.Rect((x * 70 + border), (y * 70 + border), 70, 70)
                text_rect = text.get_rect()
                text_rect.topleft = (rect.x+20, rect.y+20)
                if self.cell_active and self.cell_coordinates == (y, x):
                    self.cell_color = (212, 81, 104)
                    self.cell_line = 3
                else:
                    self.cell_color = (0, 0, 0)
                    self.cell_line = 1
                pygame.draw.rect(self.window, self.cell_color, rect, self.cell_line)
                pygame.draw.rect(self.window, (170, 238, 187), text_rect, 1)
                self.window.blit(text, text_rect)
                row.append(rect)
            self.matrix_buttons.append(row)
        # Draw buttons:
        self.draw_text()
        self.draw_button((76, 800), "CHECK PROGRESS", self.button4)


    def draw_prescreen(self):
        """Draws prescreen content: Text fields, field to enter players name, 
            and buttons.
        """
        self.draw_button((100, 100), "WELCOME TO PLAY SUDOKU", None)
        self.draw_button((100, 150), "Name of the player: ", None)
        self.draw_button((100, 230), self.input_name, self.input_field)
        self.draw_button((100, 420), "CHOOSE LEVEL AND PLAY:", None)
        self.draw_button((100, 500), " EASY ", self.button1)
        self.draw_button((300, 500), "MEDIUM", self.button2)
        self.draw_button((500, 500), " HARD ", self.button3)

    def draw_button(self, position, text, button):
        """Helper function to draw buttons with text.
        Args:
            position tuple: position on gameboard as tuple containin topleft coordinates
            text str: text displayed on button
            button Rect: A rectangle that is not yet drawn to the screen.
        """
        font = pygame.font.SysFont("Arial", 32)
        text = font.render(text, True, (0, 0, 0))
        if button:
            pygame.draw.rect(self.window, (0, 0, 0), button, 2)
        rect = text.get_rect(topleft=(position[0]+10, position[1]+20))
        pygame.draw.rect(self.window, (170, 238, 187), rect, 0)
        self.window.blit(text, rect)

    def draw_text(self):
        """Helper function to draw text fields.
        """
        font = pygame.font.SysFont("Arial", 22)
        text = font.render(self.text, True, (0, 0, 0))
        text2 = font.render(self.text2, True, (0, 0, 0))
        text3 = font.render(self.text3, True, (0, 0, 0))
        rect = text.get_rect(topleft=(76, 750))
        rect2 = text2.get_rect(topleft=(76, 770))
        rect3 = text3.get_rect(topleft=(76, 790))
        self.window.blit(text, rect)
        self.window.blit(text2, rect2)
        self.window.blit(text3, rect3)

    def set_grid_settings(self):
        """Settings for grid-view.
        """
        self.set_starting_time_for_game()
        self.input_field_active = False
        self.create_user(self.input_name)
        self.input_name = ' '
        self.prescreen = False
        self.grid = True


    def check_events(self):
        """Checking events for the main loop. Contains keyboard events, as well as
            mousebutton events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.prescreen:
                    if self.input_field.collidepoint(event.pos):
                        self.input_field_active = True
                    if self.button1.collidepoint(event.pos):
                        self.set_level_and_matrix('easy')
                        self.set_grid_settings()
                    if self.button2.collidepoint(event.pos):
                        self.set_level_and_matrix('medium')
                        self.set_grid_settings()
                    if self.button3.collidepoint(event.pos):
                        self.set_level_and_matrix('hard')
                        self.set_grid_settings()
                if self.grid:
                    if self.button4.collidepoint(event.pos):
                        self.check_progress()
                    for i, row in enumerate(self.matrix_buttons):
                        for j, button in enumerate(row):
                            if button.collidepoint(event.pos):
                                self.cell_coordinates = (i, j)
                                self.cell_active = True
            if event.type == pygame.KEYDOWN:
                if self.prescreen:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_name = self.input_name[:-1]
                    else:
                        self.input_name += event.unicode
                if self.grid:
                    if event.unicode in string.digits:
                        self.input_digit = event.unicode
                    if event.unicode == ' ':
                        self.input_digit = '-1'


    def draw_window(self):
        """Draws the window depending on the setting: prescreen, grid or results.
        """
        self.window.fill((170, 238, 187))
        if self.prescreen:
            self.draw_prescreen()
        if self.results:
            self.draw_results()
        if self.grid:
            self.clock.tick(60)
            self.draw_grid()
        pygame.display.flip()


    def main(self):
        """Contains the main loop for the game. Checks the events and draws the window.
        """
        while True:
            self.check_events()
            self.draw_window()


    def check_progress(self):
        """Check the correctedness of input the player has entered.
        Args: 
            rows: tuple containing Boolean value and coordinates of a possible error
            columns: tuple containing Boolean value and coordinates of a possible error
            squares: tuple containing Boolean value and coordinates of a possible error
        """
        rows = check_correctedness.rows(self.matrix)
        columns = check_correctedness.columns(self.matrix)
        squares = check_correctedness.squares(self.matrix)
        if squares[0] is False:
            self.text = f'Errors found in square in coordinates {squares[1]}'
        else:
            self.text = ''
        if columns[0] is False:
            self.text2 = f'Errors found in column number {columns[1]}'
        else:
            self.text2 = ''
        if rows[0] is False:
            self.text3 = f'Errors found on row number {rows[1]}'
        else:
            self.text3 = ''
        if rows[0] is True:
            if columns[0] is True:
                if squares[0] is True:
                    self.text = 'All correct!'
                    self.text2 = ''
                    self.text3 = ''
                    if check_correctedness.all_filled(self.matrix):
                        self.text = 'Done!'
                        self.add_new_completed_game_for_user()


    def add_new_completed_game_for_user(self):
        """Saves the time it took to complete the game in seconds.
            Adds the game to the user.
        """
        seconds = (pygame.time.get_ticks()-self.start_time)/1000
        self.user.add_game(self.level, seconds)
        self.start_time = None
