from domain.board.board import Board
from domain.board.board_repository_memory import BoardRepositoryInMemory
from domain.player.player import Player
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from turn.step_1.action_reserve_development_card import ReserveDevelopmentCardCommand


def test_should_player_reserve_development_card():
    # given
    board_repository = BoardRepositoryInMemory()
    player_repository = PlayerRepositoryInMemory()

    reserve_exposed_development_card = ReserveDevelopmentCardCommand(board_repository=board_repository,
                                                                     player_repository=player_repository)

    example_player: Player = Player(reserved_development_cards=0, gold=0, red=0, green=0, blue=0, black=0, white=0)
    example_board: Board = Board(hidden_development_cards=78, exposed_development_cards=12, blue=4, black=0, green=4,
                                 white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)

    # when
    reserve_exposed_development_card.execute(example_player, "exposed", example_board)

    # then
    actual = (player_repository.get_player(), board_repository.get_board())
    expected = Player(reserved_development_cards=1, gold=0, red=0, green=0, blue=0, black=0, white=0), Board(hidden_development_cards=78, exposed_development_cards=11, blue=4, black=0, green=4,
                                 white=1, red=0, gold=0, card_level_1=4, card_level_2=4,
                                 card_level_3=4, number_of_nobles=5)
    assert actual == expected
