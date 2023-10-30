import copy

from domain.board.board import Board


class BoardRepositoryInMemory:


    def get_board(self):
        return copy.deepcopy(self.board)

    def save(self, board: Board):
        self.board = copy.deepcopy(board)
