from enum import Enum
class Person:
    def __init__(self, gender, okWithOpposite, peoplePrefs):
        self.gender = gender
        self.okWithOpposite = okWithOpposite
        self.peoplePrefs = peoplePrefs

    def calculateMatch(self, room):
        pass

class Genders(Enum):
    MALE = 1
    FEMALE = 2
    ENBY = 3