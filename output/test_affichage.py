from Board.board import Board
from output.CLI_interface import CliInterface


# class testCLIInterface:
#     pass


def test_printBoard():
    board_repository: CliInterface = CliInterface()
    exemple_board: Board = Board(numberOfNobles=3, gold=3, red=5, blue=5, black=5, white=5, green=5, card_level_1=3,
                                card_level_2=6, card_level_3=5)

    text_printed = board_repository.showBoard(exemple_board)
    assert text_printed == "Board(numberOfNobles=3, gold=3, red=5, green=5, blue=5, black=5, white=5, card_level_3=5, card_level_2=6, card_level_1=3)"