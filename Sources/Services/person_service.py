from Domains.person_domain import Person


class PersonService:
    """
    Person Service Class
    A class that manages a person Repository. It can access specific CRUD operations, other operations and validations
    """

    def __init__(self, personRepo, personValidator, bucketService):
        """
        Constructor for the Person Service Class
        :param personRepo: A repository, storing data
        :param personValidator: A person validator
        :param bucketService: A Bucket Service Instance, to create a Link between a Person Service and a Bucket Service
        """
        self.__repository = personRepo
        self.__validator = personValidator
        self.__bucketServiceLink = bucketService

    def getAllPersons(self):
        """
        Method for getting all the persons from the repository
        :return: A list with all the elements from the repository
        """
        return self.__repository.getAllElements()

    def getPerson(self, person):
        """
        Function for getting a specific person from the repository
        :param person: A template of the person (same ID)
        :return: The person if it exists
        """
        self.__validator.validatePerson(person)
        return self.__repository.getElement(person)

    def getPersonRawID(self, ID):
        """
        Method for getting a specific person from the repository using a raw ID
        :param ID: The ID of te person
        :return: The person if it exists, raises a repository exception otherwise
        """
        toGet = Person.getDummyPerson()
        toGet.forceID(ID)
        self.__validator.validatePerson(toGet)
        return self.__repository.getElement(toGet)

    def getAllPersonsWithName(self, name):
        """
        Method for getting a list of persons that contain a name
        :param name: The name to verify
        :return: A list of person instances
        """
        valid = Person.getDummyPerson()
        valid.setName(name)
        self.__validator.validatePerson(valid)
        personList = self.getAllPersons()
        returnList = []
        for person in personList:
            if name in person.getName():
                returnList.append(person)
        return returnList

    def addPerson(self, person):
        """
        Method for adding a person in the repository
        :param person: The person to add
        :return: None
        """
        self.__validator.validatePerson(person)
        self.__repository.addElement(person)

    def addMultiplePersons(self, personList):
        """
        Method for adding multiple persons to the repository
        :param personList: A list of person instances
        :return: None
        """
        for person in personList:
            # try:
            self.__validator.validatePerson(person)
            self.__repository.addElement(person)
        # except PersonError as msg:
        # print(msg)
        # except RepositoryError as msg:
        # print(msg)

    def addPersonRaw(self, name):
        """
        Method for adding a "raw" person in the repository
        :param name: The name of the raw person
        :return: None
        """
        newPerson = Person(name)
        self.__validator.validatePerson(newPerson)
        self.__repository.addElement(newPerson)

    def modifyPerson(self, person):
        """
        Method for modifying a person already in a repository
        :param person: The modified person (same ID)
        :return: None
        """
        self.__validator.validatePerson(person)
        self.__repository.modifyElement(person)
        self.__bucketServiceLink.modifyBucketsWithPerson(person)

    def modifyPersonRaw(self, ID, name):
        """
        Method for raw modifying a person already in a repository
        :param ID: The ID of the person to modify
        :param name: The modified name
        :return: None
        """
        toModify = Person(name)
        toModify.forceID(ID)
        self.__validator.validatePerson(toModify)
        self.__repository.modifyElement(toModify)
        self.__bucketServiceLink.modifyBucketsWithPerson(toModify)

    def deletePerson(self, person):
        """
        Method to delete a person already in a repository
        :param person: The person to delete
        :return: None
        """
        self.__validator.validatePerson(person)
        self.__repository.removeElement(person)
        self.__bucketServiceLink.removeBucketsWithPerson(person)

    def deletePersonRaw(self, ID):
        """
        Method to delete a person already in a repository, raw
        :param ID: The ID of the person to delete
        :return: None
        """
        toDelete = Person.getDummyPerson()
        toDelete.forceID(ID)
        self.__validator.validatePerson(toDelete)
        self.__repository.removeElement(toDelete)
        self.__bucketServiceLink.removeBucketsWithPerson(toDelete)
