from Board.board import Board


class StartGameCommand:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_players):
        if number_of_players == 2:
            number_of_nobles = 3
            red = 4
        elif number_of_players == 3:
            number_of_nobles = 4
            red = 5
        elif number_of_players == 4:
            number_of_nobles = 5
            red = 7
        else:
            number_of_nobles = 0
            red = 0
        self.game_repository.save(
            Board(numberOfNobles=number_of_nobles, yellow=5, red=red, card_level_3=4, card_level_2=4, card_level_1=4))


