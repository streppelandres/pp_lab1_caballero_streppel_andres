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
        return list(filter(lambda hero: hero[attr_key] == attr_value, self.heroes))

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

    def __get_grouped_amount_of_heroes_by_key(self, key):
        grouped_heroes = self.__get_grouped_heroes_by_key(key)
        return {k: len(grouped_heroes[k]) for k in grouped_heroes}

    @staticmethod
    def save_heroes_to_csv(file_name, heroes):
        data = [['Name', 'Identity', 'Company', 'Height', 'Weight', 'Gender',
                 'Eyes color', 'Hair color', 'Strength', 'Intelligence']]
        
        for hero in heroes:
            data.append([hero.name, hero.identity, hero.company, hero.height,
                         hero.weight, hero.gender, hero.eyes_color, hero.hair_color,
                         hero.strength, hero.intelligence])
        
        save_csv(file_name, data)


    # Use cases:

    def get_males_heroes(self):
        return self.__get_heroes_by_attr_key_and_value(self.ATTR_GENDER, self.GENDER_MALE)

    def get_females_heroes(self):
        return self.__get_heroes_by_attr_key_and_value(self.ATTR_GENDER, self.GENDER_FEMALE)

    def get_more_height_male(self):
        return HeroesHelper.__get_max_hero_by_attr(self.get_males_heroes(), self.ATTR_HEIGHT)

    def get_more_height_female(self):
        return HeroesHelper.__get_max_hero_by_attr(self.get_females_heroes(), self.ATTR_HEIGHT)

    def get_less_height_male(self):
        return HeroesHelper.__get_min_hero_by_attr(self.get_males_heroes(), self.ATTR_HEIGHT)

    def get_less_height_female(self):
        return HeroesHelper.__get_min_hero_by_attr(self.get_females_heroes(), self.ATTR_HEIGHT)

    def get_average_height_male(self):
        return HeroesHelper.__get_avergae_by_hero_attr(self.get_males_heroes(), self.ATTR_HEIGHT)

    def get_average_height_female(self):
        return HeroesHelper.__get_avergae_by_hero_attr(self.get_females_heroes(), self.ATTR_HEIGHT)

    def get_grouped_amount_by_eyes_color(self):
        return self.__get_grouped_amount_of_heroes_by_key('eyes_color')

    def get_grouped_amount_by_hair_color(self):
        return self.__get_grouped_amount_of_heroes_by_key('hair_color')

    def get_grouped_amount_by_intelligence(self):
        return self.__get_grouped_amount_of_heroes_by_key('intelligence')

    def get_grouped_by_eyes_color(self):
        return self.__get_grouped_heroes_by_key('eyes_color')

    def get_grouped_by_hair_color(self):
        return self.__get_grouped_heroes_by_key('hair_color')

    def get_grouped_by_intelligence(self):
        return self.__get_grouped_heroes_by_key('intelligence')
