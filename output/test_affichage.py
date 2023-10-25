from domain.board.board import Board
from output.CLI_interface import CliInterface


# class testCLIInterface:
#     pass


def test_printBoard():
    user_interface: CliInterface = CliInterface()
    exemple_board: Board = Board(number_of_nobles=3, gold=3, red=5, blue=5, black=5, white=5, green=5, card_level_1=3,
                                 card_level_2=6, card_level_3=5)

    actual = user_interface.showBoard(exemple_board)
    expected = "Board(number_of_nobles=3, gold=3, red=5, green=5, blue=5, black=5, white=5, card_level_3=5, card_level_2=6, card_level_1=3)"
    assert actual == expected

def test_printBoard2():
    user_interface: CliInterface = CliInterface()
    exemple_board: Board = Board(number_of_nobles=3, gold=14, red=5, blue=5, black=5, white=5, green=5, card_level_1=3,
                                 card_level_2=6, card_level_3=5)

    actual = user_interface.showBoard(exemple_board)
    expected = "Board(number_of_nobles=3, gold=14, red=5, green=5, blue=5, black=5, white=5, card_level_3=5, card_level_2=6, card_level_1=3)"
    assert actual == expected