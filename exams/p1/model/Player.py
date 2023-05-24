import PlayerStats


class Player:
    name: str
    position: str
    statistics: PlayerStats
    archivements: list(str)

    def __init__(self, name: str, position: str, statistics: PlayerStats, archivements: list(str)) -> None:
        self.name = name
        self.position = position
        self.statistics = statistics
        self.archivements = archivements
