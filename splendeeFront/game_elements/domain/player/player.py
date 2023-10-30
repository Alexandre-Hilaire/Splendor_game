import dataclasses


@dataclasses.dataclass
class Player:
    reserved_development_cards: int
    owned_development_card: int
    coins_by_color: dict[str]

