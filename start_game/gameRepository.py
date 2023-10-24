class GameRepositoryInMemory:
    def get_game(self):
        return self.game

    def save(self, game):
        self.game = game
