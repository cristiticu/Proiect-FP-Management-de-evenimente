from colorama import Fore


class Event:
    """
    Event Model
        A class that defines an Event data type
    """
    __lastUsedID = 0
    __eventInstanceNumber = 0

    def __init__(self, addr, date, time, desc):
        """
        Constructor for the Event data type
        :param addr: The address of the event
        :param date: The date of the event
        :param time: The time of the event
        :param desc: The description of the event
        """
        self.__id = Event.__createValidID()
        self.__address = addr
        self.__date = date
        self.__time = time
        self.__description = desc
        self.__isForced = False

    def __del__(self):
        """
        Destructor for the Event data type
        :return: None
        """
        Event.__eventInstanceNumber -= 1

    def __str__(self):
        """
        Defines string output from an event type
        :return: String output, formatted
        """
        return Fore.CYAN + str(self.getID()) + Fore.RESET + ': ' + self.getAddress() + " | " + self.getDate() + " | " + self.getTime() + " | " + self.getDescription()

    def __eq__(self, other):
        """
        Defines equality between two events
        :param other: The other event
        :return: True if the same, False otherwise
        """
        if self.getID() == other.getID():
            return True
        return False

    def __ne__(self, other):
        """
        Defines inequality between two events
        :param other: The other event
        :return: True if not equal, False otherwise
        """
        if self.getID() != other.getID():
            return True
        return False

    def getID(self):
        """
        Method for getting the ID of an event
        :return: The ID
        """
        return self.__id

    def getAddress(self):
        """
        Method for getting the address of an event
        :return: The address
        """
        return self.__address

    def getDate(self):
        """
        Method for getting the date of an event
        :return: The date
        """
        return self.__date

    def getTime(self):
        """
        Method for getting the time of an event
        :return: The time
        """
        return self.__time

    def getDescription(self):
        """
        Method for getting the description of an event
        :return: The description
        """
        return self.__description

    def setAddress(self, addr):
        """
        Method for setting the address of an event
        :param addr: The address to set
        :return: None
        """
        self.__address = addr

    def setDate(self, date):
        """
        Method for setting the date of an event
        :param date: The date to set
        :return: None
        """
        self.__date = date

    def setTime(self, time):
        """
        Method for setting the time of an event
        :param time: The time to set
        :return: None
        """
        self.__time = time

    def setDescription(self, desc):
        """
        Method for setting the description of an event
        :param desc: The description
        :return: None
        """
        self.__description = desc

    def __setID(self, sid):
        """
        Private method for setting the ID of an event, should not be called
        :param sid: The ID to force set
        :return: None
        """
        self.__id = sid

    def forceID(self, sid):
        """
        Method for forcing a particular ID to an event
        :param sid: The ID to force
        :return: None
        """
        self.__isForced = True
        self.__setID(sid)

    @staticmethod
    def getDummyEvent():
        """
        Static method for generating a dummy event
        :return: a dummy event
        """
        dummy = Event("DUMMY_ADDR", "01.01.01", "01:01", "DUMMY")
        return dummy

    @staticmethod
    def __createValidID():
        """
        Static method that creates a valid ID for an event
        :return: A valid ID
        """
        Event.__eventInstanceNumber += 1
        Event.__lastUsedID += 1
        return Event.__lastUsedID

    @staticmethod
    def getLastUsedID():
        """
        Static method that gets the last used ID of an event
        :return: The last used ID
        """
        return Event.__lastUsedID

    @staticmethod
    def resetIDValues():
        """
        Static method that resets the ID Values to 0
        :return: None
        """
        Event.__lastUsedID = 0
