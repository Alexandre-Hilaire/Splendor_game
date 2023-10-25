from domain.game.game import Game


class GameRepositoryInMemory:


    def get_game(self):
        return self.game

    def save(self, game: Game):
        self.game = game
