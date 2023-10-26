import pytest

from domain.cards.Card import Card
from domain.player.player import Player
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from turn.step_1.Error import NotEnoughCoin
from turn.step_1.buy_card_command import BuyCardCommand


def test_buy_card():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = create_player_with_owned_development_card(0,
                                                                       {"gold": 0, "red": 0, "green": 3, "blue": 0,
                                                                        "black": 0,
                                                                        "white": 0})
    example_card: Card = Card(price={"green": 2})

    buy_card_command.execute(example_player, example_card)

    actual = create_player_with_owned_development_card(1, {"gold": 0, "red": 0, "green": 1, "blue": 0, "black": 0,
                                                           "white": 0})
    expected = player_repository.get_player()

    assert actual == expected


def test_buy_card2():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = create_player_with_owned_development_card(1, {"gold": 0, "red": 3, "green": 2, "blue": 1,
                                                                           "black": 5,
                                                                           "white": 0})
    example_card: Card = Card(price={"green": 1, "red": 1, "black": 1, "blue": 1})

    buy_card_command.execute(example_player, example_card)

    actual = create_player_with_owned_development_card(2, {"gold": 0, "red": 2, "green": 1, "blue": 0,
                                                           "black": 4,
                                                           "white": 0})
    expected = player_repository.get_player()

    assert actual == expected


def test_buy_card_failed():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = create_player_with_owned_development_card(0, {"gold": 0, "red": 0, "green": 0, "blue": 0,
                                                                           "black": 0,
                                                                           "white": 0})
    example_card: Card = Card(price={"green": 1, "red": 2})

    has_error_not_enough_coin = False

    try:
        buy_card_command.execute(example_player, example_card)
    except NotEnoughCoin:
        has_error_not_enough_coin = True
    assert has_error_not_enough_coin


@pytest.mark.skip
def test_buy_card_with_gold():
    player_repository = PlayerRepositoryInMemory()
    buy_card_command = BuyCardCommand(player_repository)

    example_player: Player = create_player_with_owned_development_card(0, {"gold": 0, "red": 0, "green": 0, "blue": 0,
                                                                           "black": 0,
                                                                           "white": 0})
    example_card: Card = Card(price={"red": 1, "blue": 1})

    buy_card_command.execute(example_player, example_card)

    actual = player_repository.get_player()
    expected = create_player_with_owned_development_card(1, {"gold": 0, "red": 0, "green": 0, "blue": 0, "black": 0,
                                                             "white": 0})
    assert actual == expected


def create_player_with_owned_development_card(number_owned_card, coins_content):
    return Player(coins_by_color=coins_content,
                  reserved_development_cards=0,
                  owned_development_card=number_owned_card)
