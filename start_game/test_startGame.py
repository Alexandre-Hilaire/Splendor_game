# import start_game.startGame as startGame
# from star
from start_game import gameRepository
from start_game import startGame


def test_should_start_game_for_two_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=2)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=3, yellow=5, red=4, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected


def test_should_start_game_for_three_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=3)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=4, yellow=5, red=5, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected


def test_should_start_game_for_four_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=4)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=5, yellow=5, red=7, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected
