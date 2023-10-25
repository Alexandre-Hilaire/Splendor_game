import dataclasses


@dataclasses.dataclass
class Player:
    reserved_development_cards: int
    gold: int
    red: int
    green: int
    blue: int
    black: int
    white: int

