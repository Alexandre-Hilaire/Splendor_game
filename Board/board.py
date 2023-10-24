import dataclasses


@dataclasses.dataclass
class Board:
    numberOfNobles: int
    yellow: int
    red: int
    card_level_3: int
    card_level_2: int
    card_level_1: int
