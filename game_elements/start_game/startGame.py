from game_elements.domain.board.board import Board
from game_elements.domain.game.game import Game
from game_elements.domain.player.player import Player


class StartGameCommand:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_players):
        number_card_exposed_per_level = 4
        coin_amount_by_player_numbers = {2: 4, 3: 5, 4: 7}
        number_of_nobles = number_of_players + 1
        gold_coin = 5

        board = Board(hidden_development_cards_by_level={1: 40 - number_card_exposed_per_level,
                                                         2: 30 - number_card_exposed_per_level,
                                                         3: 20 - number_card_exposed_per_level},
                      number_of_nobles=number_of_nobles, gold=gold_coin,
                      red=coin_amount_by_player_numbers[number_of_players],
                      green=coin_amount_by_player_numbers[number_of_players],
                      blue=coin_amount_by_player_numbers[number_of_players],
                      black=coin_amount_by_player_numbers[number_of_players],
                      white=coin_amount_by_player_numbers[number_of_players],
                      exposed_development_cards_by_level={1: number_card_exposed_per_level,
                                                          2: number_card_exposed_per_level,
                                                          3: number_card_exposed_per_level})
        players = [
            Player(reserved_development_cards=0,
                   coins_by_color={"gold": 0, "red": 0, "green": 0, "blue": 0, "black": 0, "white": 0},
                   owned_development_card=0) for _ in
            range(number_of_players)
        ]
        self.game_repository.save(
            Game(board, players))
