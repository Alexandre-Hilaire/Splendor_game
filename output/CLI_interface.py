# from output.outputRepository import OutputRepository
from game_elements import Board


class CliInterface:

    # implementation
    def showBoard(self, board: Board):
        print(board)
        return board.__repr__()

