import dataclasses

from domain.board.board import Board
from domain.player.player import Player


@dataclasses.dataclass
class Game:
    board: Board
    players: list[Player]
