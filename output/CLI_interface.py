# from output.outputRepository import OutputRepository
from domain.board.board import Board


class CliInterface:

    # implementation
    def showBoard(self, board: Board):
        print(board)
        return board.__repr__()

