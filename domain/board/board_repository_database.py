import copy

from domain.board.board import Board as DTO_Board
from splendor_game.models import Game


class BoardRepositoryInMemory:

    def get_board(self):
        board = Game.objects.all()[0]  # extraction d'un jeu de la base de donnée / erreur s'il n'en existe pas
        board = DTO_Board(hidden_development_cards_by_level={1: 25, 2: 25, 3: 25}, number_of_nobles=board.visible_noble,
                          gold=board.gold_coins, red=board.red_coins, green=board.green_coins, blue=board.blue_coins,
                          black=board.black_coins, white=board.white_coins,
                          exposed_development_cards_by_level={1: board.visible_development_card_lvl_1,
                                                              2: board.visible_development_card_lvl_2,
                                                              3: board.visible_development_card_lvl_3})
        return board

    def save(self, dto_board: DTO_Board):
        if Game.objects.count() == 0:
            # create a new board
            board = Game()
        else:
            board = Game.objects.all()[0]

        board.visible_development_card_lvl_1 = dto_board.exposed_development_cards_by_level[1]
        board.visible_development_card_lvl_2 = dto_board.exposed_development_cards_by_level[2]
        board.visible_development_card_lvl_3 = dto_board.exposed_development_cards_by_level[3]
        board.visible_noble = dto_board.number_of_nobles
        board.gold_coins, board.red_coins, board.green_coins, board.blue_coins, board.black_coins, board.white_coins = \
            dto_board.gold, dto_board.red, dto_board.green, dto_board.blue, dto_board.black, dto_board.white
        board.save()
