import pytest

from Board.board import Board
from player.Player import Player
from player import playerRepository
from start_game import gameRepository
from turn.step_1.Error import NotEnoughCoinsError
from turn.step_1.action_take_2_coins_of_the_same_color import TakeTwoCoinsCommand


# @pytest.mark.skip("test raise exception")
def test_take_2_green_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=0, green=0, blue=0, black=0, white=0)
    example_board: Board = Board(blue=4, black=0, green=4, white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)
    take_coins_command.execute(example_player, "green", example_board)

    actual = (player_repository.get_player(), game_repository.get_game())
    expected = Player(gold=0, red=0, green=2, blue=0, black=0, white=0), Board(blue=4, black=0, green=2, white=1, red=0,
                                                                               gold=0, card_level_1=4, card_level_2=4,
                                                                               card_level_3=4, number_of_nobles=5)

    assert actual == expected


# @pytest.mark.skip
def test_take_2_red_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=0, green=0, blue=2, black=1, white=0)
    example_board: Board = Board(blue=4, black=0, green=4, white=1, red=5, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)

    take_coins_command.execute(example_player, "red", example_board)

    actual = (player_repository.get_player(), game_repository.get_game())
    expected = Player(gold=0, red=2, green=0, blue=2, black=1, white=0), Board(blue=4, black=0, green=4, white=1, red=3,
                                                                               gold=0, card_level_1=4, card_level_2=4,
                                                                               card_level_3=4, number_of_nobles=5)

    assert actual == expected


# @pytest.mark.skip
def test_take_2_white_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=5, green=3, blue=7, black=12, white=3)
    example_board: Board = Board(blue=4, black=0, green=4, white=5, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)

    take_coins_command.execute(example_player, "white", example_board)

    actual = player_repository.get_player(), game_repository.get_game()
    expected = Player(gold=0, red=5, green=3, blue=7, black=12, white=5), Board(blue=4, black=0, green=4, white=3,
                                                                                red=0, gold=0, card_level_1=4,
                                                                                card_level_2=4,
                                                                                card_level_3=4, number_of_nobles=5)

    assert actual == expected


# @pytest.mark.skip
def test_take_2_blue_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=2, red=5, green=3, blue=5, black=1, white=5)
    example_board: Board = Board(blue=5, black=0, green=4, white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)

    take_coins_command.execute(example_player, "blue", example_board)

    actual = player_repository.get_player(), game_repository.get_game()
    expected = Player(gold=2, red=5, green=3, blue=7, black=1, white=5), Board(blue=3, black=0, green=4, white=1, red=0,
                                                                               gold=0, card_level_1=4, card_level_2=4,
                                                                               card_level_3=4, number_of_nobles=5)

    assert actual == expected


# @pytest.mark.skip
def test_take_2_black_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=1, green=1, blue=2, black=1, white=1)
    example_board: Board = Board(blue=4, black=4, green=4, white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)

    take_coins_command.execute(example_player, "black", example_board)

    actual = player_repository.get_player(), game_repository.get_game()
    expected = Player(gold=0, red=1, green=1, blue=2, black=3, white=1), Board(blue=4, black=2, green=4, white=1, red=0,
                                                                               gold=0, card_level_1=4, card_level_2=4,
                                                                               card_level_3=4, number_of_nobles=5)

    assert actual == expected


def test_4_or_more_tokens_when_take_two():
    game_repository = gameRepository.GameRepositoryInMemory()
    player_repository = playerRepository.PlayerRepositoryInMemory()

    example_player: Player = Player(gold=0, red=1, green=1, blue=2, black=1, white=0)
    example_board: Board = Board(blue=4, black=0, green=3, white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)
    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    has_not_enough_coin_error = False
    try:
        take_coins_command.execute(example_player, "green", example_board)
    except NotEnoughCoinsError:
        has_not_enough_coin_error = True

    assert has_not_enough_coin_error


def test_4_or_more_tokens_when_take_two_bis():
    game_repository = gameRepository.GameRepositoryInMemory()
    player_repository = playerRepository.PlayerRepositoryInMemory()

    example_player: Player = Player(gold=0, red=1, green=1, blue=2, black=1, white=0)
    example_board: Board = Board(blue=4, black=0, green=3, white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)
    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    has_not_enough_coin_error = False
    try:
        take_coins_command.execute(example_player, "white", example_board)
    except NotEnoughCoinsError:
        has_not_enough_coin_error = True

    assert has_not_enough_coin_error
