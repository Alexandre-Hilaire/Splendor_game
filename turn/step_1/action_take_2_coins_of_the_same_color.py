from domain.board.board import Board
from domain.player.player import Player
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
                board.green -= 2
            case "red":
                if board.red < 4:
                    raise NotEnoughCoinsError()
                player.red += 2
                board.red -= 2
            case "black":
                if board.black < 4:
                    raise NotEnoughCoinsError()
                player.black += 2
                board.black -= 2
            case "blue":
                if board.blue < 4:
                    raise NotEnoughCoinsError()
                player.blue += 2
                board.blue -= 2
            case "white":
                if board.white < 4:
                    raise NotEnoughCoinsError()
                player.white += 2
                board.white -= 2

        self.player_repository.save(player)
        self.board_repository.save(board)


