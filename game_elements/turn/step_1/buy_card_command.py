from game_elements.domain.cards.Card import Card
from game_elements.domain.player.player import Player
from game_elements.domain.player.player_repository_memory import PlayerRepositoryInMemory
from game_elements.turn.step_1.Error import NotEnoughCoin


class BuyCardCommand:
    def __init__(self, player_repository: PlayerRepositoryInMemory):
        self.player_repository = player_repository

    def execute(self, player: Player, card: Card):

        for coin_color in card.price:
            coin_cost = card.price[coin_color]

            if coin_cost > (player.coins_by_color[coin_color] + player.coins_by_color["gold"]):
                raise NotEnoughCoin
            while player.coins_by_color[coin_color] > 0 and coin_cost > 0:
                player.coins_by_color[coin_color] -= 1
                coin_cost -= 1
            while coin_cost > 0:
                player.coins_by_color["gold"] -= 1
                coin_cost -= 1

        player.owned_development_card += 1
        self.player_repository.save(player)
