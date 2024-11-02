class Owner:
    def __init__(self, owner_id: str) -> None:
        self.sleeper_user_id: str = owner_id
        self.sleeper_display_name: str = None
        self.team_name: str = None
        self.roster_id: int = None
        self.team_name: str = None
        self.owner_first_name: str = None
        self.owner_last_name: str = None
        self.owner_avatar: str = None
        self.league_start_year: int = None
        self.owner_bio: str = None