from dataparser import parse

def main():
    people = parse()
    print("How many rooms? ")
    rooms = input()
    while True:
        print("Minimum people per room: ")
        minPeoplePer = input()
        print("Maximum people per room: ")
        maxPeoplePer = input()
        if (minPeoplePer < 1):
            print("Bruh. No empty rooms allowed")
        elif (minPeoplePer > people.size / rooms):
            print("Min is too high. No possible allocation\n")
        elif (maxPeoplePer < people.size / rooms):
            print("Max is too low. No possible allocations\n")
        else: break
    

def explorePossibleSizes(numPeople, numRooms, minPeoplePer, maxPeoplePer):
