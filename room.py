class Room:
    def __init__(self) -> None:
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def getRoomScore(self):
        score = 0
        for person in self.people:
            score += person.calculateMatch(self)