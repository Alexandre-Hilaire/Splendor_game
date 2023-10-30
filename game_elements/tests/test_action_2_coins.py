from game_elements.domain.board.board import Board
from game_elements.domain.player.player import Player
import game_elements.domain.player.player_repository_memory as playerRepository
import game_elements.domain.board.board_repository_memory as boardRepository
from game_elements.turn.step_1.Error import NotEnoughCoinsError
from game_elements.turn.step_1.action_take_2_coins_of_the_same_color import TakeTwoCoinsCommand

"""
given
    the board contains 5 nobles, 4 blue and green coins, 1 white coin, 0 coin for other colors, 4 development card per level
    the player owns no coins at all
when
    the player takes two green coins
then
    the player has now 2 green coins and the player 2 green coins
    the board has now 2 green coins instead of 4
"""


def test_take_2_green_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    board_repository = boardRepository.BoardRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=board_repository, player_repository=player_repository)

    # given
    example_player: Player = create_player({"gold": 0, "red": 0, "green": 0, "blue": 0, "black": 0, "white": 0})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=4,
                                 white=1, red=0, gold=0,
                                 exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5)
    # when
    take_coins_command.execute(example_player, "green", example_board)

    # then
    actual = (player_repository.get_player(), board_repository.get_board())
    expected = (create_player({"gold": 0, "red": 0, "green": 2, "blue": 0, "black": 0, "white": 0}),
                Board(
                    hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=2, white=1, red=0,
                    gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5))

    assert actual == expected


"""
given
    the board contains 5 nobles, 5 red coins, 4 blue and green coins, 1 white coin, 0 coin for other colors, 4 development card per level
    the player owns 2 blue coins and 1 black coin
when
    the player takes two red coins
then
    the board has now 3 red coins
    the player has 2 red coins
"""


def test_take_2_red_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = boardRepository.BoardRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = create_player({"gold": 0, "red": 0, "green": 0, "blue": 2, "black": 1, "white": 0})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=4,
                                 white=1, red=5, gold=0,
                                 exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5)

    take_coins_command.execute(example_player, "red", example_board)

    actual = player_repository.get_player(), game_repository.get_board()
    expected = (
        create_player({"gold": 0, "red": 2, "green": 0, "blue": 2, "black": 1, "white": 0}),
        Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=4, white=1, red=3,
              gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5))

    assert actual == expected


def test_take_2_white_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = boardRepository.BoardRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = create_player({"gold": 0, "red": 5, "green": 3, "blue": 7, "black": 12, "white": 3})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=4,
                                 white=5, red=0, gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4},
                                 number_of_nobles=5)

    take_coins_command.execute(example_player, "white", example_board)

    actual = player_repository.get_player(), game_repository.get_board()
    expected = (create_player({"gold": 0, "red": 5, "green": 3, "blue": 7, "black": 12, "white": 5}),
                Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=4, white=3, red=0,
                      gold=0,
                      exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5))

    assert actual == expected


def test_take_2_blue_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = boardRepository.BoardRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = create_player({"gold": 2, "red": 5, "green": 3, "blue": 5, "black": 1, "white": 5})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=5, black=0, green=4,
                                 white=1, red=0, gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4},
                                 number_of_nobles=5)

    take_coins_command.execute(example_player, "blue", example_board)

    actual = player_repository.get_player(), game_repository.get_board()
    expected = (create_player({"gold": 2, "red": 5, "green": 3, "blue": 7, "black": 1, "white": 5}),
                Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=3, black=0, green=4, white=1, red=0,
                      gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5))

    assert actual == expected


def test_take_2_black_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = boardRepository.BoardRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = create_player({"gold": 0, "red": 1, "green": 1, "blue": 2, "black": 1, "white": 1})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=4, green=4,
                                 white=1, red=0, gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4},
                                 number_of_nobles=5)

    take_coins_command.execute(example_player, "black", example_board)

    actual = player_repository.get_player(), game_repository.get_board()
    expected = (create_player({"gold": 0, "red": 1, "green": 1, "blue": 2, "black": 3, "white": 1}),
                Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=2, green=4, white=1, red=0,
                      gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4}, number_of_nobles=5))

    assert actual == expected


def test_4_or_more_tokens_when_take_two():
    game_repository = boardRepository.BoardRepositoryInMemory()
    player_repository = playerRepository.PlayerRepositoryInMemory()

    example_player: Player = create_player({"gold": 0, "red": 1, "green": 1, "blue": 2, "black": 1, "white": 0})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=3,
                                 white=1, red=0, gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4},
                                 number_of_nobles=5)
    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    has_not_enough_coin_error = False
    try:
        take_coins_command.execute(example_player, "green", example_board)
    except NotEnoughCoinsError:
        has_not_enough_coin_error = True

    assert has_not_enough_coin_error


def test_4_or_more_tokens_when_take_two_bis():
    game_repository = boardRepository.BoardRepositoryInMemory()
    player_repository = playerRepository.PlayerRepositoryInMemory()

    example_player: Player = create_player({"gold": 0, "red": 1, "green": 1, "blue": 2, "black": 1, "white": 0})
    example_board: Board = Board(hidden_development_cards_by_level={1: 36, 2: 26, 3: 16}, blue=4, black=0, green=3,
                                 white=1, red=0, gold=0, exposed_development_cards_by_level={1: 4, 2: 4, 3: 4},
                                 number_of_nobles=5)
    take_coins_command = TakeTwoCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    has_not_enough_coin_error = False
    try:
        take_coins_command.execute(example_player, "white", example_board)
    except NotEnoughCoinsError:
        has_not_enough_coin_error = True

    assert has_not_enough_coin_error


def create_player(coins_content):
    return Player(reserved_development_cards=0, coins_by_color=coins_content,
                  owned_development_card=0)
