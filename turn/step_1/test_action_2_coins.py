from player.Player import Player
from player import playerRepository
from start_game import gameRepository
from turn.step_1.action_take_2_coins_of_the_same_color import TakeTwoCoinsCommand


def test_take_2_green_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(game_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=0, green=0, blue=0, black=0, white=0)

    take_coins_command.execute(example_player, "green")

    actual = player_repository.get_player()
    expected = Player(gold=0, red=0, green=2, blue=0, black=0, white=0)

    assert actual == expected


def test_take_2_red_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(game_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=0, green=0, blue=2, black=1, white=0)

    take_coins_command.execute(example_player, "red")

    actual = player_repository.get_player()
    expected = Player(gold=0, red=2, green=0, blue=2, black=1, white=0)

    assert actual == expected


def test_take_2_white_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(game_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=5, green=3, blue=7, black=12, white=3)

    take_coins_command.execute(example_player, "white")

    actual = player_repository.get_player()
    expected = Player(gold=0, red=5, green=3, blue=7, black=12, white=5)

    assert actual == expected


def test_take_2_blue_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(game_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=2, red=5, green=3, blue=5, black=1, white=5)

    take_coins_command.execute(example_player, "blue")

    actual = player_repository.get_player()
    expected = Player(gold=2, red=5, green=3, blue=7, black=1, white=5)

    assert actual == expected


def test_take_2_black_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = gameRepository.GameRepositoryInMemory()

    take_coins_command = TakeTwoCoinsCommand(game_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=1, green=1, blue=2, black=1, white=1)

    take_coins_command.execute(example_player, "black")

    actual = player_repository.get_player()
    expected = Player(gold=0, red=1, green=1, blue=2, black=3, white=1)

    assert actual == expected


