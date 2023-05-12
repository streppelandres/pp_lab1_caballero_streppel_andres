from functools import partial
from model.Hero import Hero


class HeroesHelper:
    heroes: list

    def __init__(self, json_heroes):
        self.heroes = self.__heroes_adapter(json_heroes)

    def __heroes_adapter(self, json_heroes):
        adapted_heroes = []
        for h in json_heroes:
            adapted_heroes.append(Hero(
                h['name'], h['identity'], h['company'], h['height'], h['weight'], h['gender'],
                h['eyes_color'], h['hair_color'], h['strength'], h['intelligence']
            ))
        return adapted_heroes
    
    @staticmethod
    def __to_dict_heroes(heroes:list):
        return [h.to_dict() for h in heroes]

    @staticmethod
    def __sort_by_key(heroes:list, attr:str, ascending=True):
        return HeroesHelper.__to_dict_heroes(sorted(heroes, key = lambda h : h[attr], reverse=not ascending))

    # Use cases:
    def sort_by_height(self):
        return HeroesHelper.__sort_by_key(self.heroes, 'height')

    def sort_by_weight(self):
        return HeroesHelper.__sort_by_key(self.heroes, 'weight', False)

    def sort_by_name(self):
        return HeroesHelper.__sort_by_key(self.heroes, 'name')

    def sort_by_name_length(self):
        # Try to not repeat code, similar to __sort_by_key
        return HeroesHelper.__to_dict_heroes(sorted(self.heroes, key = lambda h : len(h['name'])))