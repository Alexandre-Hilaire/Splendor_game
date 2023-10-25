import pytest

from domain.board.board import Board
from domain.game.game import Game
from domain.game.game_repository_memory import GameRepositoryInMemory
from domain.player.player import Player
from start_game import startGame

"""
given
    the game master want to start the game
when
    two players plays
then
    a game with two player and a board with 3 nobles, 5 gold coins, 4 coins per other color and 4 development card per 
    level is prepared
"""
def test_should_start_game_for_two_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=2)

    actual = game_repository.get_game()
    expected = Game(
        board=Board(hidden_development_cards=78, exposed_development_cards=12, number_of_nobles=3, gold=5, red=4, green=4, blue=4, black=4, white=4, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected


"""
given
    the game master want to start the game
when
    three players plays
then
    a game with two player and a board with 4 nobles, 5 gold coins, 5 coins per other color and 4 development card per 
    level is prepared
"""
def test_should_start_game_for_three_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=3)

    actual = game_repository.get_game()

    expected = Game(
        board=Board(hidden_development_cards=78, exposed_development_cards=12, number_of_nobles=4, gold=5, red=5, green=5, blue=5, black=5, white=5, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected


"""
given
    the game master want to start the game
when
    four players plays
then
    a game with two player and a board with 5 nobles, 5 gold coins, 7 coins per other color and 4 development card per 
    level is prepared
"""
def test_should_start_game_for_four_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=4)

    actual = game_repository.get_game()
    expected = Game(
        board=Board(hidden_development_cards=78, exposed_development_cards=12, number_of_nobles=5, gold=5, red=7, green=7, blue=7, black=7, white=7, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected
