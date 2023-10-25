from domain.player.player import Player


class PlayerRepositoryInMemory:

    def get_player(self):
        return self.player

    def save(self, player: Player):
        self.player = player
