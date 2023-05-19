from model.Hero import Hero
from utils.csv_utils import *


class HeroesHelper:
    ATTR_GENDER = 'gender'
    ATTR_HEIGHT = 'height'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

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

    def __get_heroes_by_attr_key_and_value(self, attr_key, attr_value):
        return list(filter(lambda hero: hero[attr_key].capitalize() == attr_value.capitalize(), self.heroes))

    @staticmethod
    def __get_max_hero_by_attr(heroes, attr_key):
        return max(heroes, key=lambda hero: float(hero[attr_key]))

    @staticmethod
    def __get_min_hero_by_attr(heroes, attr_key):
        return min(heroes, key=lambda hero: float(hero[attr_key]))

    @staticmethod
    def __get_sum_by_hero_attr(heroes, attr_key):
        return sum([hero[attr_key] for hero in heroes])

    @staticmethod
    def __get_avergae_by_hero_attr(heroes, attr_key):
        return HeroesHelper.__get_sum_by_hero_attr(heroes, attr_key) / len(heroes)

    def __get_grouped_heroes_by_key(self, key):
        grouped_heroes = {}

        for hero in self.heroes:
            # find a way to make this more dinamic/generic
            if key == 'intelligence' and not hero['intelligence']:
                hero.intelligence = 'Does not have'

            if hero[key] in grouped_heroes.keys():
                grouped_heroes[hero[key]].append(
                    hero.get_name())  # TODO: Remove the 'get_name'
            else:
                grouped_heroes[hero[key]] = []
                grouped_heroes[hero[key]].append(
                    hero.get_name())  # TODO: Remove the 'get_name'

        return grouped_heroes

    def __get_grouped_quantity_of_heroes_by_key(self, key):
        grouped_heroes = self.__get_grouped_heroes_by_key(key)
        return {k: len(grouped_heroes[k]) for k in grouped_heroes}

    @staticmethod
    def __get_hero_head_csv():
        return ['Name', 'Identity', 'Company', 'Height', 'Weight', 'Gender',
                 'Eyes color', 'Hair color', 'Strength', 'Intelligence']
    
    @staticmethod
    def __get_hero_data_csv(hero, hide_identity):
        return [hero['name'], (hide_identity and 'secret' or hero['identity']), hero['company'], hero['height'], hero['weight'],
                 hero['gender'], hero['eyes_color'], hero['hair_color'], hero['strength'],
                 hero['intelligence']]
        #return [hero.name, (hide_identity and 'secret' or hero.identity), hero.company, hero.height, hero.weight,
        #         hero.gender, hero.eyes_color, hero.hair_color, hero.strength,
        #         hero.intelligence]

    @staticmethod
    def save_heroes_to_csv(file_name, heroes, hide_identity=True):
        data = [HeroesHelper.__get_hero_head_csv()]
        
        for hero in heroes:
            data.append(HeroesHelper.__get_hero_data_csv(hero, hide_identity))
        
        save_csv(file_name, data)
    
    @staticmethod
    def save_hero_to_csv(file_name, hero, hide_identity=True):
        data = [HeroesHelper.__get_hero_head_csv()]
        data.append(HeroesHelper.__get_hero_data_csv(hero, hide_identity))
        save_csv(file_name, data)
        
    @staticmethod
    def __save_to_csv(file_name, data):
        save_csv(file_name, data)

    @staticmethod
    def __save_to_csv_with_head(file_name, head, data):
        save_csv(file_name, [head] + [data])

    @staticmethod
    def __save_grouped_quantity_by_attr(elements, file_name, attr):
        head = [attr, 'quantity']
        data = []
        for key in list(elements.keys()):
            data.append([key, elements[key]])
        HeroesHelper.__save_to_csv(file_name, [head] + data)
    
    @staticmethod
    def __save_grouped_heroes_by_attr(grouped_heroes, file_name, attr):
        head = [attr, 'heroes']
        data = []
        for key in list(grouped_heroes.keys()):
            data.append([key, ' - '.join(grouped_heroes[key])])
        HeroesHelper.__save_to_csv(file_name, [head] + data)

    @staticmethod
    def __to_dict_heroes(heroes:list):
        return [h.to_dict() for h in heroes]

    @staticmethod
    def __sort_by_key(heroes:list, attr:str, ascending=True):
        return HeroesHelper.__to_dict_heroes(sorted(heroes, key = lambda h : h[attr], reverse=not ascending))

    @staticmethod
    def __filter_higher_or_less_by_attr(heroes:list, attr:str, value:float, higher:bool=True) -> list:
        return list(filter(lambda h : higher and h[attr] > value or h[attr] < value, heroes))

    # use cases
    # FIXME: Fijate que hay cosas que se repiten bastante, al re pedo

    def get_by_quantity(self, quantity):
        return [self.heroes[i] for i in range(quantity)]
    
    def sort_by_height(self, ascending=True):
        return HeroesHelper.__sort_by_key(self.heroes, 'height', ascending)
    
    def sort_by_strength(self, ascending=True):
        return HeroesHelper.__sort_by_key(self.heroes, 'strength', ascending)
    
    def get_height_average(self) -> float:
        return round(float(HeroesHelper.__get_avergae_by_hero_attr(self.heroes, 'height')), 2)
    
    def filter_height_by_average(self, average:float, higher:bool=True) -> list:
        return HeroesHelper.__filter_higher_or_less_by_attr(self.heroes, 'height', average, higher)
    
    def get_weight_average(self) -> float:
        return round(float(HeroesHelper.__get_avergae_by_hero_attr(self.heroes, 'weight')), 2)
    
    def filter_weight_by_average(self, average:float, higher:bool=True) -> list:
        return HeroesHelper.__filter_higher_or_less_by_attr(self.heroes, 'weight', average, higher)
    
    def get_strength_average(self) -> float:
        return round(float(HeroesHelper.__get_avergae_by_hero_attr(self.heroes, 'strength')), 2)
    
    def filter_strength_by_average(self, average:float, higher:bool=True) -> list:
        return HeroesHelper.__filter_higher_or_less_by_attr(self.heroes, 'strength', average, higher)
    
    def filter_by_intelligence(self, intelligence):
        return self.__get_heroes_by_attr_key_and_value('intelligence', intelligence)
    