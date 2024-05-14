class Owner:
    def __init__(self, owner_id: str) -> None:
        self.owner_id: str = owner_id
        self.username: str = None
        self.display_name: str = None
        self.team_name: str = None
        self.roster_id: int = None
        self.wins: int = None
        self.losses: int = None
        self.ties: int = None
        self.pts_for: float = None
        self.pts_against: float = None