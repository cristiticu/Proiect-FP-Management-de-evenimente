from colorama import Fore


class Person:
    """
    Person Model
        A class that defines a Person data type
    """
    __lastUsedID = 0
    __personInstanceNumber = 0

    def __init__(self, nameString):
        """
        Constructor for the Person Class
        :param nameString: The name of the person, a String
        """
        self.__id = Person.__createValidID()
        # nameList = nameString.split()
        # lastName = str(nameList[0])
        # firstNames = ' '.join(nameList[1:])
        # self.__name = {"lastName": lastName,
        #                "firstName": firstNames}
        self.__name = nameString
        self.__isForced = False

    def __del__(self):
        """
        Destructor for the Person Class. It decreases the number of Person Instances by one
        :return: None
        """
        Person.__personInstanceNumber -= 1

    def __str__(self):
        """
        Method for getting a printable string out of the Person Instance
        :return: A printable String containing adequate information
        """
        return Fore.CYAN + str(self.getID()) + Fore.RESET + ': ' + self.getName()

    def __eq__(self, other):
        """
        Method that defines equality between two Instances of Person
        :param other: The other Person
        :return: True if they are the same, False otherwise
        """
        if self.getID() == other.getID():
            return True
        return False

    def __ne__(self, other):
        """
        Method that defines two different Instances of Person
        :param other: The other Person
        :return: True if they are different, False otherwise
        """
        if self.getID() != other.getID():
            return True
        return False

    def getID(self):
        """
        Method for getting the ID of a Person
        :return: The ID
        """
        return self.__id

    def getName(self):
        """
        Method for getting the Name of a Person
        :return: The Name
        """
        # nameString = ""
        # for key in self.__name:
        #     nameString += self.__name[key] + " "
        # return nameString[:-1]
        return self.__name

    def setName(self, nameString):
        """
        Method for setting the Name of a Person
        :param nameString: The Name
        :return: None
        """
        # nameList = nameString.split()
        # lastName = str(nameList[0])
        # firstNames = ' '.join(nameList[1:])
        # self.__name = {"lastName": lastName,
        #                "firstName": firstNames}
        self.__name = nameString

    def __setID(self, sid):
        """
        Private method for setting the ID of a Person. Under no circumstances should the user set the ID of a Person,
        as it is passed automatically as valid
        :param sid: The ID to be set
        :return: None
        """
        self.__id = sid

    def forceID(self, sid):
        """
        Method for forcing a certain ID onto a Person. This method should be used only to create Dummy Persons that
        act like another Person for equality purposes
        :param sid: The forced ID
        :return: None
        """
        self.__isForced = True
        self.__setID(sid)

    @staticmethod
    def getDummyPerson():
        """
        A static method that generates a Dummy Person
        :return: a new Dummy Person
        """
        dummy = Person("DUMMY")
        return dummy

    @staticmethod
    def __createValidID():
        """
        A private static method that creates a valid ID for a Person Instance. It is called by the constructor
        and should not be called by the user
        :return: A valid ID to be passed to the constructor
        """
        Person.__personInstanceNumber += 1
        Person.__lastUsedID += 1
        return Person.__lastUsedID

    @staticmethod
    def getLastUsedID():
        """
        A static method that returns the last used ID by a Person Instance
        :return: The last used ID by a constructor
        """
        return Person.__lastUsedID

    @staticmethod
    def resetIDValues():
        """
        Static method that resets the ID Values to 0
        :return: None
        """
        Person.__lastUsedID = 0
