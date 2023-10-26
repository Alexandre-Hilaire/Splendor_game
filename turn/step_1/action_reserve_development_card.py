from domain.board.board import Board
from domain.player.player import Player
from turn.step_1.Error import AlreadyThreeReservedCard


class ReserveDevelopmentCardCommand:
    def __init__(self, board_repository, player_repository):
        self.board_repository = board_repository
        self.player_repository = player_repository

    def execute(self, player: Player, board: Board, card_type: str, level_card: int):
        if player.reserved_development_cards == 3:
            raise AlreadyThreeReservedCard()

        match card_type:
            case "hidden":
                player.reserved_development_cards += 1
                board.hidden_development_cards_by_level[level_card] -= 1

            case "exposed":
                board.exposed_development_cards_by_level[level_card] -= 1
                player.reserved_development_cards += 1
                board.hidden_development_cards_by_level[level_card] -= 1
                board.exposed_development_cards_by_level[level_card] += 1

        if board.gold > 0:
            player.gold += 1
            board.gold -= 1

        self.player_repository.save(player)
        self.board_repository.save(board)
