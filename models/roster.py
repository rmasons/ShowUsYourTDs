from typing import List
from player import Player

class Roster:
    def __init__(self) -> None:
        self.roster_id: int = None
        self.starters: List[Player] = None
        self.bench: List[Player] = None
        self.reserve: List[Player] = None