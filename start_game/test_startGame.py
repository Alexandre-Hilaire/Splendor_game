# import start_game.startGame as startGame
# from star
from start_game import gameRepository
from start_game import startGame


def test_should_start_game_for_two_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=2)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=3, gold=5, red=4, green=4, blue=4, black=4, white=4, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected


def test_should_start_game_for_three_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=3)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=4, gold=5, red=5, green=5, blue=5, black=5, white=5, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected


def test_should_start_game_for_four_players():
    game_repository = gameRepository.GameRepositoryInMemory()

    start_game_command = startGame.StartGameCommand(game_repository=game_repository)
    start_game_command.execute(number_of_players=4)

    actual = game_repository.get_game()
    expected = startGame.Board(numberOfNobles=5, gold=5, red=7, green=7, blue=7, black=7, white=7, card_level_3=4, card_level_2=4, card_level_1=4)
    assert actual == expected
