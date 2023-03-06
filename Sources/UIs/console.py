from Exceptions.custom_exceptions import RepositoryError, PersonError, EventError, BucketError, ValidationError
from Generators.generator import generateRandomEvents, generateRandomPersons, generateRandomBuckets
from colorama import Fore, init

init(autoreset=True)


class Console:
    """
    A Class capable of interacting with the user through the terminal. It calls the necessary Service Methods and renders
    the UI.
    """

    def __init__(self, personService, eventService, bucketService):
        """
        Constructor for the Console Class
        :param personService: A PersonService Instance
        :param eventService: An EventService Instance
        :param bucketService: A BucketService Instance
        """
        self.__personService = personService
        self.__eventService = eventService
        self.__bucketService = bucketService

    def __printPersonsShort(self):
        """
        Method for printing a shortened version of person data
        :return: None
        """
        personList = self.__personService.getAllPersons()
        printableLen = len(personList)
        notPrinted = 0
        if printableLen > 3:
            notPrinted = printableLen - 3
            printableLen = 3
        if printableLen == 0:
            print(Fore.YELLOW + "Empty", end='')

        for i in range(0, printableLen):
            print(personList[i], end='', sep='')
            if i < printableLen - 1:
                print(", ", end='', sep='')
        if notPrinted > 0:
            print(" ... and ", notPrinted, " others", sep='', end='')
        print("\n")

    def __printEventsShort(self):
        """
        Method for printing a shortened version of event data
        :return: None
        """
        eventList = self.__eventService.getAllEvents()
        printableLen = len(eventList)
        notPrinted = 0
        if printableLen > 3:
            notPrinted = printableLen - 3
            printableLen = 3
        if printableLen == 0:
            print(Fore.YELLOW + "Empty", end='')

        for i in range(0, printableLen):
            print(eventList[i], end='', sep='')
            if i < printableLen - 1:
                print(", ", end='', sep='')
        if notPrinted > 0:
            print(" ... and ", notPrinted, " others", sep='', end='')
        print("\n")

    def __printBucketsShort(self):
        """
        Method for printing a shortened version of bucket data
        :return: None
        """
        bucketList = self.__bucketService.getAllBuckets()
        printableLen = len(bucketList)
        notPrinted = 0
        if printableLen > 3:
            notPrinted = printableLen - 3
            printableLen = 3
        if printableLen == 0:
            print(Fore.YELLOW + "Empty", end='')

        for i in range(0, printableLen):
            print(bucketList[i], end='', sep='')
            if i < printableLen - 1:
                print(", ", end='', sep='')
        if notPrinted > 0:
            print(" ... and ", notPrinted, " others", end='', sep='')
        print("\n")

    def __printPersonsAndEvents(self):
        """
        A method for printing persons and events
        :return: None
        """
        personList = self.__personService.getAllPersons()
        eventList = self.__eventService.getAllEvents()
        personIndex = 0
        eventIndex = 0

        while personIndex < len(personList) or eventIndex < len(eventList):
            if personIndex < len(personList):
                print(personList[personIndex], " " * (50 - len(personList[personIndex].getName())), "|          ", sep='', end='')
                personIndex += 1
            else:
                print(" " * 50 + "|          ", sep='', end='')
            if eventIndex < len(eventList):
                print(eventList[eventIndex], sep='', end='')
                eventIndex += 1
            print("\n", sep='', end='')

    def __printAllPersons(self):
        """
        Method for printing all the persons
        :return: None
        """
        personList = self.__personService.getAllPersons()
        for i in range(0, len(personList)):
            print(personList[i])

    def __printAllEvents(self):
        """
        Method for printing all the events
        :return: None
        """
        eventList = self.__eventService.getAllEvents()
        for i in range(0, len(eventList)):
            print(eventList[i])

    def __printAllBuckets(self):
        """
        Method for printing all the buckets
        :return: None
        """
        bucketList = self.__bucketService.getAllBuckets()
        for i in range(0, len(bucketList)):
            print(bucketList[i])

    def __getIntegerInput(self):
        """
        Method for reading an integer
        :return: The read integer
        """
        selection = int(input())
        return selection

    def __getStringInput(self):
        """
        Method for reading a string
        :return: The read string
        """
        strInput = input()
        return strInput

    def __renderAddPersonUI(self):
        """
        Main Method for rendering the Add Person UI
        :return: None
        """
        print("Enter a name: ", end='', sep='')
        name = self.__getStringInput()
        self.__personService.addPersonRaw(name)

    def __renderAddEventUI(self):
        """
        Main Method for rendering the Add Event UI
        :return: None
        """
        print("Enter event data")
        print("Enter an address: ", end='', sep='')
        address = self.__getStringInput()
        print("Enter a date: ", end='', sep='')
        date = self.__getStringInput()
        print("Enter a time: ", end='', sep='')
        time = self.__getStringInput()
        print("Enter a description: ", end='', sep='')
        description = self.__getStringInput()
        self.__eventService.addEventRaw(address, date, time, description)

    def __renderAddBucketUI(self):
        """
        Main Method for rendering the Add Bucket UI
        :return: None
        """
        self.__printPersonsAndEvents()
        print("Select a person ID: ", sep='', end='')
        personID = self.__getIntegerInput()
        print("Select an event ID: ", sep='', end='')
        eventID = self.__getIntegerInput()

        selectedPerson = self.__personService.getPersonRawID(personID)
        selectedEvent = self.__eventService.getEventRawID(eventID)

        self.__bucketService.addBucket(selectedPerson, selectedEvent)

    def __renderModifyPersonUI(self):
        """
        Main Method for rendering the Modify Person UI
        :return: None
        """
        self.__printAllPersons()
        print("Select a person ID: ", sep='', end='')
        personID = self.__getIntegerInput()
        print("Enter a new name: ", sep='', end='')
        newName = self.__getStringInput()

        self.__personService.modifyPersonRaw(personID, newName)

    def __renderModifyEventUI(self):
        """
        Main Method for rendering the Modify Event UI
        :return: None
        """
        self.__printAllEvents()
        print("Select an event ID:", sep='', end='')
        eventID = self.__getIntegerInput()
        print("Enter new event data")
        print("Enter a new address: ", end='', sep='')
        address = self.__getStringInput()
        print("Enter a  new date: ", end='', sep='')
        date = self.__getStringInput()
        print("Enter a new time: ", end='', sep='')
        time = self.__getStringInput()
        print("Enter a new description: ", end='', sep='')
        description = self.__getStringInput()
        self.__eventService.modifyEventRaw(eventID, address, date, time, description)

    def __renderRemovePersonUI(self):
        """
        Main Method for rendering the Remove Person UI
        :return: None
        """
        self.__printAllPersons()
        print("Select a person ID:", sep='', end='')
        personID = self.__getIntegerInput()

        self.__personService.deletePersonRaw(personID)

    def __renderRemoveEventUI(self):
        """
        Main Method for rendering the Remove Event UI
        :return: None
        """
        self.__printAllEvents()
        print("Select an event ID:", sep='', end='')
        eventID = self.__getIntegerInput()

        self.__eventService.deleteEventRaw(eventID)

    def __renderSearchPersonIDUI(self):
        """
        Main method for rendering the search person by ID UI
        :return: None
        """
        print("Enter a person ID: ", sep='', end='')
        personID = self.__getIntegerInput()

        print("The person is: ", self.__personService.getPersonRawID(personID))
        input("Press ENTER to Continue . . .")

    def __renderSearchPersonNameUI(self):
        """
        Main method for rendering the search person by Name UI
        :return: None
        """
        print("Enter a name: ", sep='', end='')
        personName = self.__getStringInput()

        print("Persons that match the name are: ")
        lst = self.__personService.getAllPersonsWithName(personName)
        for elem in lst:
            print(elem)
        input("Press ENTER to Continue . . .")

    def __renderSearchEventIDUI(self):
        """
        Main method for rendering the search event by ID UI
        :return: None
        """
        print("Enter an event ID: ", sep='', end='')
        eventID = self.__getIntegerInput()

        print("The event is: ", self.__eventService.getEventRawID(eventID))
        input("Press ENTER to Continue . . .")

    def __renderSearchEventDateUI(self):
        """
        Main method for rendering the search event by date UI
        :return: None
        """
        print("Enter a date: ", sep='', end='')
        eventDate = self.__getStringInput()

        print("Events that match the date are: ")
        lst = self.__eventService.getAllEventsWithDate(eventDate)
        for elem in lst:
            print(elem)
        input("Press ENTER to Continue . . .")

    def __renderSearchEventTimeUI(self):
        """
        Main method for rendering the search event by time UI
        :return: None
        """
        print("Enter a time: ", sep='', end='')
        eventTime = self.__getStringInput()

        print("Events that match the time are: ")
        lst = self.__eventService.getAllEventsWithTime(eventTime)
        for elem in lst:
            print(elem)
        input("Press ENTER to Continue . . .")

    def __renderSearchEventAddressUI(self):
        """
        Main method for rendering the search event by address UI
        :return: None
        """
        print("Enter an address: ", sep='', end='')
        eventAddress = self.__getStringInput()

        print("Events that match the address are: ")
        lst = self.__eventService.getAllEventsWithAddress(eventAddress)
        for elem in lst:
            print(elem)
        input("Press ENTER to Continue . . .")

    def __renderGeneratePersonsUI(self):
        """
        Main method for rendering the generate-person function UI
        :return: None
        """
        print("Enter a number of persons: ", sep='', end='')
        numPersons = self.__getIntegerInput()
        personLst = generateRandomPersons(numPersons)
        self.__personService.addMultiplePersons(personLst)
        print("Added", numPersons, "Persons")
        input("Press ENTER to Continue . . .")

    def __renderGenerateEventsUI(self):
        """
        Main method for rendering the generate-event function UI
        :return: None
        """
        print("Enter a number of events: ", sep='', end='')
        numEvents = self.__getIntegerInput()
        eventLst = generateRandomEvents(numEvents)
        self.__eventService.addMultipleEvents(eventLst)
        print("Added", numEvents, "Events")
        input("Press ENTER to Continue . . .")

    def __renderGenerateBucketsUI(self):
        """
        Main method for rendering the generate-buckets function UI
        :return: None
        """
        bucketList = generateRandomBuckets(self.__personService.getAllPersons(), self.__eventService.getAllEvents())
        for bucket in bucketList:
            selectedPerson = self.__personService.getPersonRawID(bucket[0])
            selectedEvent = self.__eventService.getEventRawID(bucket[1])
            try:
                self.__bucketService.addBucket(selectedPerson, selectedEvent)
            except RepositoryError:
                pass
        input("Press ENTER to Continue . . .")

    def __renderGetOrderedListOfEventsUI(self):
        """
        Main method for rendering the function UI for getting an ordered list of all the events a person goes to
        :return: None
        """
        self.__printAllPersons()
        print("Select a Person ID")
        personID = self.__getIntegerInput()
        selectedPerson = self.__personService.getPersonRawID(personID)
        bucketList = self.__bucketService.getOrderedListOfEvents(selectedPerson)
        print("The sorted events are: ")
        for elem in bucketList:
            print(elem)
        input("Press ENTER to Continue . . .")

    def __renderGetListOfPersonsWithMostEventsUI(self):
        """
        Main method for rendering the function UI for getting a list of the persons with the most events
        :return: None
        """
        tupleList = self.__bucketService.getListOfPersonsWithMostEvents(self.__personService.getAllPersons())
        with open("Datafiles/reports.output", "w") as writeReport:
            for elem in tupleList:
                if elem[1] != 0:
                    print(elem[0], (' ' * (40 - len(elem[0].getName()))), " goes to ", Fore.MAGENTA+str(elem[1])+Fore.RESET, " events")
                    writeReport.write(str(elem[0].getID())+": "+elem[0].getName()+(' ' * (40 - len(elem[0].getName())))+" goes to "+str(elem[1])+" events\n")
        input("Press ENTER to Continue . . .")

    def __renderPercentOfEventsWithMostPersonsUI(self):
        """
        Main Method for rendering the function UI for getting the top 20% of events with most attendees
        :return: None
        """
        tupleList = self.__bucketService.getOrderedEventsByPersons(self.__eventService.getAllEvents())
        twentyPercent = int(len(tupleList) * 0.2)
        for count in range(twentyPercent):
            print(tupleList[count][0], (' ' * (40 - len(tupleList[count][0].getDescription()))), " has ", Fore.MAGENTA+str(tupleList[count][1])+Fore.RESET, " attendees")
        input("Press ENTER to Continue . . .")

    def __renderAverageEventsPerPerson(self):
        """
        Main method for rendering the function UI for getting the average number of events a person goes to
        :return: None
        """
        personList = self.__personService.getAllPersons()
        average = self.__bucketService.getAverageEventsPerPerson(personList)
        print("The average number of events a person goes to is ", Fore.MAGENTA+str(average))
        input("Press ENTER to Continue . . .")

    def __printMenuDictionaryDescription(self, menuDictionary):
        """
        General method for printing descriptions
        :param menuDictionary: A method dictionary
        :return: None
        """
        menuDescriptions = {self.__renderPersonMenuUI: "Person Functions Menu",
                            self.__renderEventMenuUI: "Event Functions Menu",
                            self.__renderRelationMenuUI: "Relationships Functions Menu",
                            self.__renderAddPersonUI: "Add a person",
                            self.__renderModifyPersonUI: "Modify a person",
                            self.__renderRemovePersonUI: "Remove a person",
                            self.__renderAddEventUI: "Add an event",
                            self.__renderModifyEventUI: "Modify an event",
                            self.__renderRemoveEventUI: "Remove an event",
                            self.__renderAddBucketUI: "Book a person to an event",
                            self.__renderSearchPersonIDUI: "Search a person by an ID",
                            self.__renderSearchPersonNameUI: "Search a name in the list",
                            self.__renderSearchEventIDUI: "Search an event by an ID",
                            self.__renderSearchEventDateUI: "Search an event by a date",
                            self.__renderSearchEventTimeUI: "Search an event by time",
                            self.__renderGeneratePersonsUI: "Generate a number of persons",
                            self.__renderGenerateEventsUI: "Generate a number of events",
                            self.__renderSearchEventAddressUI: "Search an event by address",
                            self.__renderGetOrderedListOfEventsUI: "Print an ordered list of events a person goes to",
                            self.__renderGenerateBucketsUI: "Generate random relations",
                            self.__renderGetListOfPersonsWithMostEventsUI: "Print persons ordered by number of events",
                            self.__renderPercentOfEventsWithMostPersonsUI: "Print the top 20% of events with most persons",
                            self.__renderAverageEventsPerPerson: "Print the average events per person"}
        exitIndex = len(menuDictionary) + 1
        for keys in menuDictionary:
            print(Fore.GREEN + str(keys), sep='', end='')
            print(" - ", menuDescriptions[menuDictionary[keys]], "\n", sep='', end='')
        print(Fore.LIGHTRED_EX + str(exitIndex), sep='', end='')
        print(" - ", "Exit", sep='', end='')

    def __renderPersonMenuUI(self):
        """
        General method for the Person Menu UI
        :return: None
        """
        personMenuDictionary = {1: self.__renderAddPersonUI,
                                2: self.__renderModifyPersonUI,
                                3: self.__renderRemovePersonUI,
                                4: self.__renderSearchPersonIDUI,
                                5: self.__renderSearchPersonNameUI,
                                6: self.__renderGeneratePersonsUI}

        exitIndex = len(personMenuDictionary) + 1
        userSelection = -1
        while userSelection != exitIndex:
            print("\n=============\n", "Available Options")
            self.__printMenuDictionaryDescription(personMenuDictionary)

            print("\nYour Selection: ", sep='', end='')
            userSelection = self.__getIntegerInput()

            if userSelection == exitIndex:
                return
            elif userSelection in range(1, len(personMenuDictionary) + 1):
                personMenuDictionary[userSelection]()

    def __renderEventMenuUI(self):
        """
        General method for the Event Menu UI
        :return: None
        """
        eventMenuDictionary = {1: self.__renderAddEventUI,
                               2: self.__renderModifyEventUI,
                               3: self.__renderRemoveEventUI,
                               4: self.__renderSearchEventIDUI,
                               5: self.__renderSearchEventDateUI,
                               6: self.__renderSearchEventTimeUI,
                               7: self.__renderSearchEventAddressUI,
                               8: self.__renderGenerateEventsUI}

        exitIndex = len(eventMenuDictionary) + 1
        userSelection = -1
        while userSelection != exitIndex:
            print("\n=============\n", "Available Options")
            self.__printMenuDictionaryDescription(eventMenuDictionary)

            print("\nYour Selection: ", sep='', end='')
            userSelection = self.__getIntegerInput()

            if userSelection == exitIndex:
                return
            elif userSelection in range(1, len(eventMenuDictionary) + 1):
                eventMenuDictionary[userSelection]()

    def __renderRelationMenuUI(self):
        """
        General method for the Relation Menu UI
        :return: None
        """
        relationMenuDictionary = {1: self.__renderAddBucketUI,
                                  2: self.__renderGetOrderedListOfEventsUI,
                                  3: self.__renderGetListOfPersonsWithMostEventsUI,
                                  4: self.__renderPercentOfEventsWithMostPersonsUI,
                                  5: self.__renderAverageEventsPerPerson,
                                  6: self.__renderGenerateBucketsUI}

        exitIndex = len(relationMenuDictionary) + 1
        userSelection = -1
        while userSelection != exitIndex:
            print("\n=============\n", "Available Options")
            self.__printMenuDictionaryDescription(relationMenuDictionary)

            print("\nYour Selection: ", sep='', end='')
            userSelection = self.__getIntegerInput()

            if userSelection == exitIndex:
                return
            elif userSelection in range(1, len(relationMenuDictionary) + 1):
                relationMenuDictionary[userSelection]()

    def renderMainMenuUI(self):
        """
        Method for rendering the Main Menu
        :return: None
        """
        mainMenuDictionary = {1: self.__renderPersonMenuUI,
                              2: self.__renderEventMenuUI,
                              3: self.__renderRelationMenuUI}
        exitIndex = len(mainMenuDictionary) + 1
        userSelection = -1
        while userSelection != exitIndex:
            try:
                print("\n" * 60, "=============\n", "Persons in Database:", sep='')
                self.__printPersonsShort()
                print("Events in Database:")
                self.__printEventsShort()
                print("Buckets in Database:")
                self.__printBucketsShort()
                print("\n=============\n", "Available Options")
                self.__printMenuDictionaryDescription(mainMenuDictionary)

                print("\nYour Selection: ", sep='', end='')
                userSelection = self.__getIntegerInput()

                if userSelection == exitIndex:
                    return
                elif userSelection in range(1, len(mainMenuDictionary) + 1):
                    mainMenuDictionary[userSelection]()
            except RepositoryError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except PersonError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except EventError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except ValidationError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except ValueError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except TypeError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except IndexError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except BucketError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
            except ZeroDivisionError as msg:
                print(Fore.RED + str(msg))
                input("Press ENTER to Continue . . .")
