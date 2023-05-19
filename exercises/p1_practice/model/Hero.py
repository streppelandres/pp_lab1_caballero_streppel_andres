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
        self.name = name.capitalize()
        self.identity = identity.capitalize()
        self.company = company.capitalize()
        self.height = float(height)
        self.weight = float(weight)
        self.gender = gender.capitalize()
        self.eyes_color = eyes_color.capitalize()
        self.hair_color = hair_color.capitalize()
        self.strength = int(strength)
        self.intelligence = intelligence.capitalize()

    def __str__(self, hide_identity=True):
        return (f'Name: {self.name}, identity: {hide_identity and "secret" or self.identity}, '
                f'company: {self.company}, height: {self.height}cm, weight: {self.weight}kg, '
                f'gender: {self.gender}, eyes color: {self.eyes_color}, hair color: {self.hair_color}, '
                f'strength: {self.strength}, intelligence: {self.intelligence}')

    def __getitem__(self, key):
        return getattr(self, key)

    def to_dict(self):
        return {
            'name': self.name,
            'identity': self.identity,
            'company': self.company,
            'height': self.height,
            'weight': self.weight,
            'gender': self.gender,
            'eyes_color': self.eyes_color,
            'hair_color': self.hair_color,
            'strength': self.strength,
            'intelligence': self.intelligence
        }

    def get_name(self, hide_identity=True):
        return f'{self.name} {("" if hide_identity else ("| " + self.identity))}'

    def get_name_and_attr(self, attr, hide_identity=True):
        return f'{self.get_name(hide_identity)}| {attr}: {self[attr]}'
