from Exceptions.custom_exceptions import RepositoryError


class Repository:
    """
    Repository for CRUD Operations in the form of a List of Elements
        C: Create
        R: Read
        U: Update
        D: Delete
    """
    def __init__(self):
        """
        Constructor for the Repository Class. The class contains an element list
        """
        self.__elements = []

    def __str__(self):
        """
        Method for converting a Repository Instance to a printable string
        :return: A string containing information about the Repository Instance
        """
        rstr = "["
        for element in self.getAllElements():
            rstr += str(element) + ', '
        rstr += "]"
        return rstr

    def __len__(self):
        """
        Method for getting the length of the Repository
        :return: The length of the element list
        """
        return len(self.getAllElements())

    def getAllElements(self):
        """
        Method for getting the list of elements from a Repository Instance
        :return: The element list
        """
        return self.__elements

    def addElement(self, element):
        """
        Method that adds a particular element to the list of elements
        :param element: A particular element
        :return: None
        """
        if element in self.__elements:
            raise RepositoryError("Element already in Repository\n")
        self.__elements.append(element)

    def getElement(self, element):
        """
        Method that searches and returns an element
        :param element: The element to be searched in the list
        :return: The element if it exists, or raises an exception if it's not found
        """
        if element not in self.__elements:
            raise RepositoryError("Element not in Repository\n")
        for elem in self.__elements:
            if elem == element:
                return elem

    def getElementByIndex(self, index):
        """
        Method that searches and returns an element
        :param index: The index of the element to be returned
        :return: The element if it exists, or raises an exception if it's not found
        """
        if index in range(0, len(self)):
            return self.__elements[index]
        else:
            raise RepositoryError("Element not in Repository\n")

    def removeElement(self, element):
        """
        Method that removes a particular element from the repository
        :param element: The element to be removed
        :return: None
        """
        if element not in self.__elements:
            raise RepositoryError("Element not in Repository\n")
        for elem in self.__elements:
            if elem == element:
                self.__elements.remove(elem)
                return

    def modifyElement(self, element):
        """
        Method that modifies a particular element from the repository
        :param element: The modified element that will replace the old one
        :return: None
        """
        if element not in self.__elements:
            raise RepositoryError("Element not in Repository\n")
        for index in range(0, len(self.__elements)):
            if self.__elements[index] == element:
                self.__elements[index] = element
                return

    def setNewElementList(self, newList):
        """
        Method that saves a new list in the repository
        :param newList: The list to be saved
        :return: None
        """
        self.__elements = newList
