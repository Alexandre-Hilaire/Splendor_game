from domain.board.board import Board


class BoardRepositoryInMemory:


    def get_board(self):
        return self.board

    def save(self, board: Board):
        self.board = board
