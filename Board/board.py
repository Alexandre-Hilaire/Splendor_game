import dataclasses


@dataclasses.dataclass
class Board:
    number_of_nobles: int
    gold: int
    red: int
    green: int
    blue: int
    black: int
    white: int
    card_level_3: int
    card_level_2: int
    card_level_1: int
