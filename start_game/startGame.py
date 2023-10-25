from domain.board.board import Board
from domain.game.game import Game
from domain.player.player import Player


class StartGameCommand:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def execute(self, number_of_players):
        coin_amount_by_player_numbers = {2: 4, 3: 5, 4: 7}
        number_of_nobles = number_of_players + 1
        hidden_development_cards = 78
        exposed_development_cards = 12
        gold_coin = 5

        board = Board(hidden_development_cards=hidden_development_cards,
                      exposed_development_cards=exposed_development_cards,
                      number_of_nobles=number_of_nobles, gold=gold_coin,
                      red=coin_amount_by_player_numbers[number_of_players],
                      green=coin_amount_by_player_numbers[number_of_players],
                      blue=coin_amount_by_player_numbers[number_of_players],
                      black=coin_amount_by_player_numbers[number_of_players],
                      white=coin_amount_by_player_numbers[number_of_players],
                      card_level_3=4, card_level_2=4, card_level_1=4)
        players = [
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, black=0, white=0) for _ in range(number_of_players)
        ]
        self.game_repository.save(
            Game(board, players))
