from Board.board import Board


class StartGameCommand:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_players):
        coin_amount_by_player_numbers = {2: 4, 3: 5, 4: 7}
        number_of_nobles = number_of_players + 1
        gold_coin = 5
        self.game_repository.save(
            Board(numberOfNobles=number_of_nobles, gold=gold_coin, red=coin_amount_by_player_numbers[number_of_players], green=coin_amount_by_player_numbers[number_of_players], blue=coin_amount_by_player_numbers[number_of_players], black=coin_amount_by_player_numbers[number_of_players], white=coin_amount_by_player_numbers[number_of_players],
                  card_level_3=4, card_level_2=4, card_level_1=4))
