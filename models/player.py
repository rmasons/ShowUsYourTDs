class Player:
    def __init__(self, player_id: str) -> None:
        self.player_id: str = player_id
        self.first_name: str = None
        self.last_name: str = None
        self.years_exp: int = None