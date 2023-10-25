from domain.board.board import Board
from domain.player.player import Player


class TakeThreeCoinsCommand:

    def __init__(self, board_repository, player_repository):
        self.board_repository = board_repository
        self.player_repository = player_repository

    def execute(self, player: Player, coins_color1: str, coins_color2: str, coins_color3: str, board: Board):
        match coins_color1:
            case "green":
                player.green += 1
                board.green -= 1
            case "red":
                player.red += 1
                board.red -= 1
            case "blue":
                player.blue += 1
                board.blue -= 1
            case "black":
                player.black += 1
                board.black -= 1
            case "white":
                player.white += 1
                board.white -= 1

        match coins_color2:
            case "green":
                player.green += 1
                board.green -= 1
            case "red":
                player.red += 1
                board.red -= 1
            case "blue":
                player.blue += 1
                board.blue -= 1
            case "black":
                player.black += 1
                board.black -= 1
            case "white":
                player.white += 1
                board.white -= 1

        match coins_color3:
            case "green":
                player.green += 1
                board.green -= 1
            case "red":
                player.red += 1
                board.red -= 1
            case "blue":
                player.blue += 1
                board.blue -= 1
            case "black":
                player.black += 1
                board.black -= 1
            case "white":
                player.white += 1
                board.white -= 1

        self.player_repository.save(player)
        self.board_repository.save(board)
