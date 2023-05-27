from dataclasses import dataclass
from player import PlayerStats


@dataclass
class Player:
    name: str
    position: str
    statistics: PlayerStats
    archivements: list
