from domain.board.board import Board
from domain.player.player import Player


class TakeThreeCoinsCommand:

    def __init__(self, board_repository, player_repository):
        self.board_repository = board_repository
        self.player_repository = player_repository

    def execute(self, player: Player, coins_color1: str, coins_color2: str, coins_color3: str, board: Board):

        self._move_coin_by_color(board, coins_color1, player)
        self._move_coin_by_color(board, coins_color2, player)
        self._move_coin_by_color(board, coins_color3, player)

        self.player_repository.save(player)
        self.board_repository.save(board)

    def _move_coin_by_color(self, board, color, player):
        # player.coins_by_color[color] += 1
        match color:
            case "green":
                board.green -= 1
                player.coins_by_color["green"] += 1
            case "red":
                board.red -= 1
                player.coins_by_color["red"] += 1
            case "blue":
                board.blue -= 1
                player.coins_by_color["blue"] += 1
            case "black":
                board.black -= 1
                player.coins_by_color["black"] += 1
            case "white":
                board.white -= 1
                player.coins_by_color["white"] += 1
