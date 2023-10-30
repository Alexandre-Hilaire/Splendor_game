import copy

from splendeeFront.game_elements.domain.player.player import Player


class PlayerRepositoryInMemory:

    def get_player(self):
        return copy.deepcopy(self.player)

    def save(self, player: Player):
        self.player = copy.deepcopy(player)
