from Board.board import Board
from player.Player import Player
from turn.step_1.Error import NotEnoughCoinsError


class TakeTwoCoinsCommand:
    def __init__(self, board_repository, player_repository):
        self.board_repository = board_repository
        self.player_repository = player_repository

    def execute(self, player: Player, coins_color: str, board: Board):
        match coins_color:
            case "green":
                if board.green < 4:
                    raise NotEnoughCoinsError()
                player.green += 2
            case "red":
                if board.red < 4:
                    raise NotEnoughCoinsError()
                player.red += 2
            case "black":
                if board.black < 4:
                    raise NotEnoughCoinsError()
                player.black += 2
            case "blue":
                if board.blue < 4:
                    raise NotEnoughCoinsError()
                player.blue += 2
            case "white":
                if board.white < 4:
                    raise NotEnoughCoinsError()
                player.white += 2

        self.player_repository.save(player)


"""
    def execute(self, number_of_players):
        coin_amount_by_player_numbers = {2: 4, 3: 5, 4: 7}
        number_of_nobles = number_of_players + 1
        gold_coin = 5
        self.game_repository.save(
            Board(number_of_nobles=number_of_nobles, gold=gold_coin, red=coin_amount_by_player_numbers[number_of_players], green=coin_amount_by_player_numbers[number_of_players], blue=coin_amount_by_player_numbers[number_of_players], black=coin_amount_by_player_numbers[number_of_players], white=coin_amount_by_player_numbers[number_of_players],
                  card_level_3=4, card_level_2=4, card_level_1=4))
"""
