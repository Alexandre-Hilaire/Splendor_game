import dataclasses


@dataclasses.dataclass
class Board:
    hidden_development_cards_by_level: dict[int]
    number_of_nobles: int
    gold: int
    red: int
    green: int
    blue: int
    black: int
    white: int
    exposed_development_cards_by_level: dict[int]

    def exposed_development_cards(self):
        return self.exposed_development_cards_by_level[1] + self.exposed_development_cards_by_level[2] + \
            self.exposed_development_cards_by_level[3]

    def hidden_development_cards(self):
        return self.hidden_development_cards_by_level[1] + self.hidden_development_cards_by_level[2] + \
            self.hidden_development_cards_by_level[3]


