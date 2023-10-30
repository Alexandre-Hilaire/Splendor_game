import copy

from domain.player.player import Player


class PlayerRepositoryInMemory:

    def get_player(self):
        return copy.deepcopy(self.player)

    def save(self, player: Player):
        self.player = copy.deepcopy(player)

    def __repr__(self):
        if self.player == None:
            return ""
        else:
            return str(type(self.player))
