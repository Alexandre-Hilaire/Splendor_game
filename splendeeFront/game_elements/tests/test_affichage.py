import pytest

from splendeeFront.game_elements.domain.board.board import Board
from output.CLI_interface import CliInterface

"""
given
    the board countains 3 nobles, 3 gold coins, 5 coins of other color, 4 development card per level 
when
    a player want to look at the game
then
    a line describing the board appear on screen detailing the board content
"""
@pytest.mark.skip
def test_printBoard():
    user_interface: CliInterface = CliInterface()
    exemple_board: Board = Board(hidden_development_cards=78, number_of_nobles=3, gold=3, red=5, blue=5, black=5, white=5, green=5, exposed_development_card_level_1=4,
                                 exposed_development_card_level_2=4, exposed_development_card_level_3=4)

    actual = user_interface.showBoard(exemple_board)
    expected = "Board(hidden_development_cards=78, number_of_nobles=3, gold=3, red=5, green=5, blue=5, black=5, white=5, exposed_development_card_level_3=4, exposed_development_card_level_2=4, exposed_development_card_level_1=4)"
    assert actual == expected


"""
given
    the board countains 3 nobles, 14 gold coins, 5 coins of other color, 6 development card per level 
when
    a player want to look at the game
then
    a line describing the board appear on screen detailing the board content
"""
@pytest.mark.skip
def test_printBoard2():
    user_interface: CliInterface = CliInterface()
    exemple_board: Board = Board(hidden_development_cards=78, number_of_nobles=3, gold=14, red=5, blue=5, black=5, white=5, green=5, exposed_development_card_level_1=6,
                                 exposed_development_card_level_2=6, exposed_development_card_level_3=6)

    actual = user_interface.showBoard(exemple_board)
    expected = "Board(hidden_development_cards=78, number_of_nobles=3, gold=14, red=5, green=5, blue=5, black=5, white=5, exposed_development_card_level_3=6, exposed_development_card_level_2=6, exposed_development_card_level_1=6)"
    assert actual == expected
