from Repositories.repository import Repository

from Domains.person_domain import Person
from Domains.event_domain import Event
from Domains.bucket_domain import Bucket

class FileRepository(Repository):
    """
    Repository for CRUD Operations in the form of a List of Elements, using a .entries file
        C: Create
        R: Read
        U: Update
        D: Delete
    """

    def __init__(self, fileName):
        """
        Constructor for the File Repository Subclass.
        :param fileName: The complete file name of a data file
        """
        super().__init__()
        self.__file = fileName
        self.__contains = ""
        self.loadElementsFromFile()

    def loadElementsFromFile(self):
        """
        Method for loading data from a file and constructing objects from it
        :return: None
        """
        try:
            with open(self.__file, "r") as readFile:
                self.__contains= readFile.readline()[:-1]
                for loadedLine in readFile.readlines():
                    loadedLine = loadedLine[:-1]
                    splitArguments = loadedLine.split(";")
                    if self.__contains == "#TYPEPERSON":
                        newPerson = Person(splitArguments[1])
                        newPerson.forceID(int(splitArguments[0]))
                        self.addElement(newPerson)
                    elif self.__contains == "#TYPEEVENT":
                        newEvent = Event(splitArguments[1], splitArguments[2], splitArguments[3], splitArguments[4])
                        newEvent.forceID(int(splitArguments[0]))
                        self.addElement(newEvent)
                    elif self.__contains == "#TYPERELATION":
                        newPerson = Person(splitArguments[1])
                        newPerson.forceID(int(splitArguments[0]))
                        newEvent = Event(splitArguments[3], splitArguments[4], splitArguments[5], splitArguments[6])
                        newEvent.forceID(int(splitArguments[2]))
                        newBucket = Bucket(newPerson, newEvent)
                        self.addElement(newBucket)
        except FileNotFoundError as msg:
            print(msg)

    def saveElementsToFile(self):
        """
        Method for storing the data from the repository to a specified file
        :return: None
        """
        try:
            with open(self.__file, "w") as writeToFile:
                if self.__contains == "#TYPEPERSON":
                    writeToFile.write("#TYPEPERSON\n")
                    for person in self.getAllElements():
                        writeToFile.write(str(person.getID())+";"+person.getName()+"\n")
                elif self.__contains == "#TYPEEVENT":
                    writeToFile.write("#TYPEEVENT\n")
                    for event in self.getAllElements():
                        writeToFile.write(str(event.getID())+";"+event.getAddress()+";"+event.getDate()+";"+event.getTime()+";"+event.getDescription()+"\n")
                elif self.__contains == "#TYPERELATION":
                    writeToFile.write("#TYPERELATION\n")
                    for bucket in self.getAllElements():
                        person = bucket.extractPerson()
                        event = bucket.extractEvent()
                        writeToFile.write(str(person.getID()) + ";" + person.getName() + ";")
                        writeToFile.write(str(event.getID()) + ";" + event.getAddress() + ";" + event.getDate() + ";" + event.getTime() + ";" + event.getDescription() + "\n")
        except FileNotFoundError as msg:
            print(msg)
