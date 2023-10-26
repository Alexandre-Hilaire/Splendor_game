from domain.cards.Card import Card
from domain.player.player import Player
from domain.player.player_repository_memory import PlayerRepositoryInMemory
from turn.step_1.Error import NotEnoughCoin


class BuyCardCommand:
    def __init__(self, player_repository: PlayerRepositoryInMemory):
        self.player_repository = player_repository

    def execute(self, player: Player, card: Card):

        for coin_color in card.price:
            coin_cost = card.price[coin_color]
            match coin_color:
                case "red":
                    if coin_cost > player.red:
                        raise NotEnoughCoin
                    player.red -= coin_cost
                case "green":
                    if coin_cost > player.green:
                        raise NotEnoughCoin
                    player.green -= coin_cost
                case "blue":
                    if coin_cost > player.blue:
                        raise NotEnoughCoin
                    player.blue -= coin_cost
                case "black":
                    if coin_cost > player.black:
                        raise NotEnoughCoin
                    player.black -= coin_cost
                case "white":
                    if coin_cost > player.white:
                        raise NotEnoughCoin
                    player.white -= coin_cost
        player.owned_development_card += 1
        self.player_repository.save(player)
