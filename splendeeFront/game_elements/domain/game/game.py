import dataclasses

from splendeeFront.game_elements.domain.board.board import Board
from splendeeFront.game_elements.domain.player.player import Player


@dataclasses.dataclass
class Game:
    board: Board
    players: list[Player]
