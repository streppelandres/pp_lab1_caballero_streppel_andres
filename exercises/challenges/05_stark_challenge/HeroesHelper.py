from model.Hero import Hero

class HeroesHelper:
    heroes : list

    def __init__(self, json_heroes):
        self.heroes = self.__heroes_adapter(json_heroes)


    def __heroes_adapter(self, json_heroes):
        return [hero.values() for hero in json_heroes]