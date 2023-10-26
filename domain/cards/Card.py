import dataclasses


@dataclasses.dataclass
class Card:
    price: dict[str]