from asyncio.windows_events import NULL
from codecs import getencoder


from enum import Enum
class Person:
    def __init__(self, gender, okWithOpposite, peoplePrefs):
        self.gender = gender
        self.okWithOpposite = okWithOpposite
        self.peoplePrefs = peoplePrefs
        

class Genders(Enum):
    MALE = 1
    FEMALE = 2
    ENBY = 3