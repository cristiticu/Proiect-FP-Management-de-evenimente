from Domains.event_domain import Event


class EventService:
    """
    Event Service Class
    A class that manages an event Repository. It can access specific CRUD operations, other operations and validations
    """

    def __init__(self, eventRepo, eventValidator, bucketService):
        """
        Event Service Constructor
        :param eventRepo: A Repository
        :param eventValidator: An Event Validator
        :param bucketService: A Bucket Service Instance
        """
        self.__repository = eventRepo
        self.__validator = eventValidator
        self.__bucketServiceLink = bucketService

    def getAllEvents(self):
        """
        Method for getting all the events in the Repository
        :return: The list of Events from the Repository
        """
        return self.__repository.getAllElements()

    def getEvent(self, event):
        """
        Method for getting a specific event from the Repository.
        :param event: The Event template to get
        :return: The requested event
        """
        self.__validator.validateEvent(event)
        return self.__repository.getElement(event)

    def getEventRawID(self, ID):
        """
        Method for getting a specific event using a raw ID
        :param ID: The ID of the event
        :return: The requested event
        """
        toGet = Event.getDummyEvent()
        toGet.forceID(ID)
        self.__validator.validateEvent(toGet)
        return self.__repository.getElement(toGet)

    def getAllEventsWithAddress(self, address):
        """
        Method for getting a list of events that contain a specific address bit
        :param address: The address bit
        :return: The list of events that contain the address bit
        """
        valid = Event.getDummyEvent()
        valid.setAddress(address)
        self.__validator.validateEvent(valid)
        eventList = self.getAllEvents()
        returnList = []
        for event in eventList:
            if address in event.getAddress():
                returnList.append(event)
        return returnList

    def getAllEventsWithDate(self, date):
        """
        Method for getting a list of events that contain a specific date bit
        :param date: The date bit
        :return: The list of events that contain the date bit
        """
        valid = Event.getDummyEvent()
        valid.setDate(date)
        self.__validator.validateEvent(valid)
        eventList = self.getAllEvents()
        returnList = []
        for event in eventList:
            if date in event.getDate():
                returnList.append(event)
        return returnList

    def getAllEventsWithTime(self, time):
        """
        Method for getting a list of events that contain a specific time bit
        :param time: The address bit
        :return: The list of events that contain the time bit
        """
        valid = Event.getDummyEvent()
        valid.setTime(time)
        self.__validator.validateEvent(valid)
        eventList = self.getAllEvents()
        returnList = []
        for event in eventList:
            if time in event.getTime():
                returnList.append(event)
        return returnList

    def addEvent(self, event):
        """
        Method that adds an event to the repository
        :param event: The event to add
        :return: None
        """
        self.__validator.validateEvent(event)
        self.__repository.addElement(event)

    def addMultipleEvents(self, eventList):
        """
        Method for adding multiple events to the repository
        :param eventList: A list of person instances
        :return: None
        """
        for event in eventList:
            # try:
            self.__validator.validateEvent(event)
            self.__repository.addElement(event)
        # except EventError as msg:
        # print(msg)
        # except RepositoryError as msg:
        # print(msg)

    def addEventRaw(self, addr, date, time, desc=''):
        """
        Method that adds a raw event to the repository
        :param addr: The raw address
        :param date: The raw date
        :param time: The raw time
        :param desc: the raw description
        :return: None
        """
        newEvent = Event(addr, date, time, desc)
        self.__validator.validateEvent(newEvent)
        self.__repository.addElement(newEvent)

    def modifyEvent(self, event):
        """
        Method that modifies an event
        :param event: The modified event template
        :return: None
        """
        self.__validator.validateEvent(event)
        self.__repository.modifyElement(event)
        self.__bucketServiceLink.modifyBucketsWithEvent(event)

    def modifyEventRaw(self, ID, address, date, time, description=''):
        """
        Method that modifies an event, raw
        :param ID: The ID of the event to modify
        :param address: The modified address
        :param date: The modified date
        :param time: The modified time
        :param description: The modified description
        :return: None
        """
        toModify = Event(address, date, time, description)
        toModify.forceID(ID)
        self.__validator.validateEvent(toModify)
        self.__repository.modifyElement(toModify)
        self.__bucketServiceLink.modifyBucketsWithEvent(toModify)

    def deleteEvent(self, event):
        """
        Method that deletes a specific event
        :param event: The event template to delete
        :return: None
        """
        self.__validator.validateEvent(event)
        self.__repository.removeElement(event)
        self.__bucketServiceLink.removeBucketsWithEvent(event)

    def deleteEventRaw(self, ID):
        """
        Method that deletes a specific event, raw
        :param ID: The ID of the event to delete
        :return: None
        """
        toDelete = Event.getDummyEvent()
        toDelete.forceID(ID)
        self.__validator.validateEvent(toDelete)
        self.__repository.removeElement(toDelete)
        self.__bucketServiceLink.removeBucketsWithEvent(toDelete)
