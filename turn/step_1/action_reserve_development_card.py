from domain.board.board import Board
from domain.player.player import Player


class ReserveDevelopmentCardCommand:
    def __init__(self, board_repository, player_repository):
        self.board_repository = board_repository
        self.player_repository = player_repository

    def execute(self, player: Player, card_type: str, board: Board):
        match card_type:
            case "hidden":
                player.reserved_development_cards += 1
                board.hidden_development_cards -= 1
            case "exposed":
                player.reserved_development_cards += 1
                board.exposed_development_cards -= 1

        self.player_repository.save(player)
        self.board_repository.save(board)


