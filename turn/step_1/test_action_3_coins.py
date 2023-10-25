from domain.board.board import Board
from domain.player.player import Player
from turn.step_1.action_take_3_coins_differents_colors import TakeThreeCoinsCommand
import domain.player.player_repository_memory as playerRepository
import domain.board.board_repository_memory as board_repository


def test_take_3_different_color_coins():
    player_repository = playerRepository.PlayerRepositoryInMemory()
    game_repository = board_repository.BoardRepositoryInMemory()

    take_coins_command = TakeThreeCoinsCommand(board_repository=game_repository, player_repository=player_repository)

    example_player: Player = Player(gold=0, red=0, green=0, blue=0, black=0, white=0)
    example_board: Board = Board(blue=4, black=4, green=4, white=4, red=4, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)
    take_coins_command.execute(player=example_player, coins_color1="red", coins_color2="blue", coins_color3="black",
                               board=example_board)

    actual = (player_repository.get_player(), game_repository.get_board())
    expected = Player(blue=1, black=1, green=0, white=0, red=1, gold=0), Board(blue=3, black=3, green=4, white=4, red=3,
                                                                               gold=0, card_level_1=4, card_level_2=4,
                                                                               card_level_3=4, number_of_nobles=5)
    assert actual == expected
