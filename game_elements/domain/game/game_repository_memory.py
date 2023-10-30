import copy

from domain.game.game import Game


class GameRepositoryInMemory:


    def get_game(self):
        return copy.deepcopy(self.game)

    def save(self, game: Game):
        self.game = copy.deepcopy(game)
