from Domains.bucket_domain import Bucket
from UsedFunctions.custom_sort import compareEvent, customSortedWrapper


class BucketService:
    """
    Bucket Service Class
    A class that manages a bucket Repository. It can access specific CRUD operations, other operations and validations
    """
    def __init__(self, bucketRepo, bucketValid):
        """
        Bucket Service constructor
        :param bucketRepo: A Repository
        :param bucketValid: A Bucket Validator
        """
        self.__repository = bucketRepo
        self.__validator = bucketValid

    def getAllBuckets(self):
        """
        Method for getting the bucket list
        :return: The list of buckets
        """
        return self.__repository.getAllElements()

    def getBucket(self, bucket):
        """
        Method for getting a specific bucket
        :param bucket: The bucket template to request
        :return: The Bucket
        """
        self.__validator.validateBucket(bucket)
        return self.__repository.getElement(bucket)

    def getAllBucketsWithPerson(self, person):
        """
        Method for getting all buckets with a specific person
        :param person: The person (must be a person object)
        :return: The list of buckets with person in them
        """
        lst = self.__repository.getAllElements()
        returnLst = []
        for bucket in lst:
            if person == bucket.extractPerson():
                returnLst.append(bucket)
        return returnLst

    def getAllBucketsWithPersonRecursive(self, person, index = 0):
        """
        Recursive method for getting all buckets with a specific event
        :param person: The person (must be a person object)
        :param index: Start index, should be 0
        :return: The list of buckets with person in them
        """
        lst = self.__repository.getAllElements()
        if index in range(len(lst)):
            result = self.getAllBucketsWithPersonRecursive(person, index + 1)
            if person == lst[index].extractPerson():
                result.append(lst[index])
            return result
        return []

    def getAllBucketsWithEvent(self, event):
        """
        Method for getting all buckets with a specific event
        :param event: The event (must be an event object)
        :return: The list of buckets with event in them
        """
        lst = self.__repository.getAllElements()
        returnLst = []
        for bucket in lst:
            if event == bucket.extractEvent():
                returnLst.append(bucket)
        return returnLst

    def getAllBucketsWithEventRecursive(self, event, index = 0):
        """
        Recursive method for getting all buckets with a specific event
        :param event: The event (must be an event object)
        :param index: Start index, should be 0
        :return: The list of buckets with event in them
        """
        lst = self.__repository.getAllElements()
        if index in range(len(lst)):
            result = self.getAllBucketsWithEventRecursive(event, index + 1)
            if event == lst[index].extractEvent():
                result.append(lst[index])
            return result
        return []

    def addBucket(self, person, event):
        """
        Method for adding a bucket to the list
        :param person: A Person Instance
        :param event: An Event Instance
        :return: None
        """
        newBucket = Bucket(person, event)
        self.__validator.validateBucket(newBucket)
        self.__repository.addElement(newBucket)

    def addBucketComplete(self, bucket):
        """
        Method for adding a complete bucket to the list
        :param bucket: The bucket object to add
        :return: None
        """
        self.__validator.validateBucket(bucket)
        self.__repository.addElement(bucket)

    def modifyBucketsWithPerson(self, person):
        """
        Method for modifying the person from a bucket
        :param person: The modified person
        :return: None
        """
        bucketList = self.__repository.getAllElements()
        for bucket in bucketList:
            if person == bucket.extractPerson():
                bucket.setBucket(person, bucket.extractEvent())

    def modifyBucketsWithEvent(self, event):
        """
        Method for modifying the event from a bucket
        :param event:
        :return: None
        """
        bucketList = self.__repository.getAllElements()
        for bucket in bucketList:
            if event == bucket.extractEvent():
                bucket.setBucket(bucket.extractPerson(), event)

    def removeBucketsWithPerson(self, person):
        """
        Method for removing a bucket that contains a specific person
        :param person: The person
        :return: None
        """
        allBuckets = self.__repository.getAllElements()
        modifiedBuckets = []
        for bucket in allBuckets:
            if bucket.extractPerson() != person:
                modifiedBuckets.append(bucket)
        self.__repository.setNewElementList(modifiedBuckets)

    def removeBucketsWithEvent(self, event):
        """
        Method for removing a bucket that contains a specific event
        :param event: The event
        :return: None
        """
        allBuckets = self.__repository.getAllElements()
        modifiedBuckets = []
        for bucket in allBuckets:
            if bucket.extractEvent() != event:
                modifiedBuckets.append(bucket)
        self.__repository.setNewElementList(modifiedBuckets)

    def getOrderedEventsByPersons(self, eventList):
        """
        Method for getting an ordered list of events by attendees
        :param eventList: A list of persons
        :return: A tuple list containing elements ([event], [number of attendees])
        """
        tupleList = []
        for event in eventList:
            personCount = len(self.getAllBucketsWithEvent(event))
            eventTuple = (event, personCount)
            tupleList.append(eventTuple)
        tupleList.sort(key=lambda k: k[1], reverse=True)
        return tupleList

    def getListOfPersonsWithMostEvents(self, personList):
        """
        Method for getting an ordered list of persons by events
        :param personList: A list of persons
        :return: A tuple list containing elements ([person], [number of events])
        """
        tupleList = []
        for person in personList:
            eventCount = len(self.getAllBucketsWithPerson(person))
            personTuple = (person, eventCount)
            tupleList.append(personTuple)
        tupleList.sort(key=lambda k: k[1], reverse=True)
        return tupleList

    def getOrderedListOfEvents(self, selectedPerson):
        """
        Method for getting an ordered list of events a person goes to
        :param selectedPerson: The person instance
        :return: An ordered list of buckets
        """
        bucketList = self.getAllBucketsWithPerson(selectedPerson)
        bucketList = customSortedWrapper(bucketList, function= "Shell", cmp=compareEvent)
        return bucketList

    def getAverageEventsPerPerson(self, personList):
        """
        Method for getting the average number of events a person goes to
        :param personList: A list of persons
        :return: The average number of events a person goes to
        """
        totalPersons = len(personList)
        sumOfEvents = 0
        for person in personList:
            sumOfEvents += len(self.getAllBucketsWithPerson(person))
        return sumOfEvents / totalPersons

        # Analiza complexitatii functiei getAverageEventsPerPerson:
        #
        #
        #
# 173   # totalPerson = len(personList)
        #               ~~~~    <- len(n) este functie constanta                                                     => O(1)
        #            ~~~        <- Atribuire                                                                         => O(1)
        #
        #
        #
# 174   # sumOfEvents = 0
        #            ~~~        <- Atribuire                                                                         => O(1)
        #
        #
        #
# 175   # for person in personList
        # ~~~        ~~~        <- iterare peste toate persoanele din personList                                     => O(N)  <-|
        #                                                                                                                       |
        #                                                                                                                       |
        #                                                                                                                       |=> O(N^2 + 2*N)
# 176   # sumOfEvents += len(self.getAllBucketsWithPerson(person))                                                              |
        #                         ~~~~~~~~~~~~~~~~~~~~~~~~   <- getAllBucketsWithPerson(n) este functie liniara      => O(N)  <-|
        #                ~~~        <- len(n) este functie constanta                                                 => O(1)  <-|
        #             ~~~           <- Atribuire                                                                     => O(1)  <-|
        #
        #
        #
# 177   # return sumOfEvents / totalPersons
        #                   ~~~    <- Impartire                                                                      => O(1)
        #
        #
        #                                                                                        --------
        # TOTAL COMPLEXITATE: O(1) + O(1) + O(1) + O(N^2 + 2*N) + O(1) =   O(N^2 + 2*N + 4)   =   O(N^2) = Best case = worst case = average case
        #                                                                                        --------
        #