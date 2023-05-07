from dataclasses import dataclass


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

    def __init__(self, name, identity, company, height, weight, gender, eyes_color, hair_color, strength, intelligence):
        self.name = name
        self.identity = identity
        self.company = company
        self.height = float(height)
        self.weight = float(weight)
        self.gender = gender
        self.eyes_color = eyes_color
        self.hair_color = hair_color
        self.strength = int(strength)
        self.intelligence = intelligence

    def __str__(self, hide_identity=True):
        return (f'Name: {self.name}, identity: {hide_identity and "secret" or self.identity}, '
                f'company: {self.company}, height: {self.height}cm, weight: {self.weight}kg, '
                f'gender: {self.gender}, eyes color: {self.eyes_color}, hair color: {self.hair_color}, '
                f'strength: {self.strength}, intelligence: {self.intelligence}')

    def __getitem__(self, key):
        return getattr(self, key)

    def get_name(self, hide_identity=True):
        return f'{self.name} {("" if hide_identity else ("| " + self.identity))}'

    def get_name_and_attr(self, attr, hide_identity=True):
        return f'{self.get_name(hide_identity)}| {attr}: {self[attr]}'
