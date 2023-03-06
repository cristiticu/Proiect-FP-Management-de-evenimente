from colorama import Fore

from Domains.person_domain import Person
from Domains.event_domain import Event

class Bucket:
    """
    Bucket Model
        A class that defines a bucket data type: a list consisting of two elements, a PERSON instance and an EVENT
        instance. An object of type bucket can be seen as a Many-to-Many relationship between an event and a person
    """
    def __init__(self, person=Person.getDummyPerson(), event=Event.getDummyEvent()):
        """
        Bucket Constructor
        :param person: A Person Instance
        :param event: An Event Instance
        """
        self.__bucket = [person, event]

    def __str__(self):
        """
        Formatting method
        :return: A formatted string containing bucket information
        """
        return str(self.extractPerson()) + Fore.MAGENTA + " <-> " + Fore.RESET + str(self.extractEvent())

    def __eq__(self, other):
        """
        Equality Method
        :param other: The other bucket instance
        :return: True if the same, False otherwise
        """
        if self.extractEvent() == other.extractEvent() and self.extractPerson() == other.extractPerson():
            return True
        return False

    def __ne__(self, other):
        """
        Inequality Method
        :param other: The other bucket instance
        :return: True if not the same, False otherwise
        """
        if self.extractEvent() != other.extractEvent() or self.extractPerson() != other.extractPerson():
            return True
        return False

    def getBucket(self):
        """
        Function for getting the bucket
        :return: The Bucket
        """
        return self.__bucket

    def extractPerson(self):
        """
        Function for extracting the person from a bucket
        :return: The Person
        """
        return self.__bucket[0]

    def extractEvent(self):
        """
        Function for extracting the event from a bucket
        :return: The event
        """
        return self.__bucket[1]

    def setBucket(self, person, event):
        """
        Function for setting a bucket
        :param person: A person instance
        :param event: An event instance
        :return: None
        """
        self.__bucket.clear()
        self.__bucket.append(person)
        self.__bucket.append(event)
