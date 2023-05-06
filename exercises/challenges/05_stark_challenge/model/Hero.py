from dataclasses import dataclass

@dataclass
class Hero:
    name: str
    identity: str
    company: str
    height: float
    weight: float
    gender: str
    eyes_color: str
    hair_color: str
    strength: int
    intelligence: str