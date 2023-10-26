import pytest

from domain.cards.Card import Card
from domain.player.player import Player
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from turn.step_1.Error import NotEnoughCoin
from turn.step_1.buy_card_command import BuyCardCommand


def test_buy_card():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = Player(green=2, gold=0, red=0, black=0, blue=0, white=0, reserved_development_cards=0,
                                    owned_development_card=0)
    example_card: Card = Card(price={"green": 2, "red": 0, "black": 0, "blue": 0, "white": 0})

    buy_card_command.execute(example_player, example_card)

    actual = Player(green=0, gold=0, red=0, black=0, blue=0, white=0, reserved_development_cards=0,
                    owned_development_card=1)
    expected = player_repository.get_player()

    assert actual == expected


def test_buy_card2():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = Player(green=1, gold=0, red=1, black=1, blue=2, white=0, reserved_development_cards=0,
                                    owned_development_card=0)
    example_card: Card = Card(price={"green": 1, "red": 1, "black": 1, "blue": 1, "white": 0})

    buy_card_command.execute(example_player, example_card)

    actual = Player(green=0, gold=0, red=0, black=0, blue=1, white=0, reserved_development_cards=0,
                    owned_development_card=1)
    expected = player_repository.get_player()

    assert actual == expected


def test_buy_card_failed():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = Player(green=1, gold=0, red=1, black=0, blue=1, white=0, reserved_development_cards=0,
                                    owned_development_card=0)
    example_card: Card = Card(price={"green": 1, "red": 2, "black": 0, "blue": 0, "white": 0})

    has_error_not_enough_coin = False

    try:
        buy_card_command.execute(example_player, example_card)
    except NotEnoughCoin:
        has_error_not_enough_coin = True
    assert has_error_not_enough_coin
