import pytest

from domain.board.board import Board
from domain.game.game import Game
from domain.game.game_repository_memory import GameRepositoryInMemory
from domain.player.player import Player
from start_game import startGame


def test_should_start_game_for_two_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=2)

    actual = game_repository.get_game()
    expected = Game(
        board=Board(number_of_nobles=3, gold=5, red=4, green=4, blue=4, black=4, white=4, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected


# @pytest.mark.skip
def test_should_start_game_for_three_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=3)

    actual = game_repository.get_game()

    expected = Game(
        board=Board(number_of_nobles=4, gold=5, red=5, green=5, blue=5, black=5, white=5, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected


def test_should_start_game_for_four_players():
    game_repository = GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=4)

    actual = game_repository.get_game()
    expected = Game(
        board=Board(number_of_nobles=5, gold=5, red=7, green=7, blue=7, black=7, white=7, card_level_3=4,
                    card_level_2=4, card_level_1=4),
        players=[
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0),
            Player(gold=0, red=0, green=0, blue=0, white=0, black=0)
        ])
    assert actual == expected
