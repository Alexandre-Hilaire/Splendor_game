class PlayerRepositoryInMemory:


    def get_player(self):
        return self.player

    def save(self, player):
        self.player = player
