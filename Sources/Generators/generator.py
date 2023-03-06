import random
import string

from Domains.person_domain import Person
from Domains.event_domain import Event

def generateRandomPersons(numberPersons):
    """
    Function that generates a list of random Persons
    :param numberPersons: The number of persons to generate
    :return: A list of random persons
    """
    lst = []
    letters = string.ascii_letters
    for counter in range(numberPersons):
        nameLen = random.randint(7, 17)
        name = (''.join(random.choice(letters) for i in range(nameLen)))
        randPerson = Person(name)
        lst.append(randPerson)
    return lst

def generateRandomEvents(numberEvents):
    """
    Function that generates a list of random Events
    :param numberEvents: The number of events to generate
    :return: A list of random events
    """
    lst = []
    letters = string.ascii_letters
    digits = string.digits
    for counter in range(numberEvents):
        addressLen = random.randint(10, 25)
        descLen = random.randint(15, 30)

        address = (''.join(random.choice(letters) for i in range(addressLen)))

        date = str(random.randint(1, 31))
        date += '.'
        date += str(random.randint(1, 12))
        date += '.'
        date += str(random.randint(2010, 2026))

        time = str(random.randint(1, 23))
        time += ':'
        time += str(random.randint(0, 59))

        desc = (''.join(random.choice(letters) for i in range(descLen)))

        randEvent = Event(address, date, time, desc)
        lst.append(randEvent)

    return lst

def generateRandomBuckets(personList, eventList):
    """
    Function for generating random connections between persons and events
    :param personList: a list of persons
    :param eventList: a list of events
    :return: A list of random buckets
    """
    numberOfConnections = random.randint(10, 25)
    lst = []
    for cont in range(numberOfConnections):
        selectedPerson = random.randint(personList[0].getID(), personList[len(personList) - 1].getID())
        numberOfEvents = random.randint(3, 10)
        for event in range(numberOfEvents):
            selectedEvent = random.randint(eventList[0].getID(), eventList[len(eventList) - 1].getID())
            bucket = [selectedPerson, selectedEvent]
            lst.append(bucket)
    return lst
