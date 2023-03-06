import unittest

from Domains.bucket_domain import Bucket
from Domains.person_domain import Person
from Domains.event_domain import Event
from Repositories.file_repository import FileRepository
from Repositories.repository import Repository

from Services.person_service import PersonService
from Services.event_service import EventService
from Services.bucket_service import BucketService

from Generators.generator import generateRandomPersons, generateRandomEvents, generateRandomBuckets

from Exceptions.custom_exceptions import RepositoryError, PersonError, EventError
from Validators.bucket_validator import BucketValidator
from Validators.event_validator import EventValidator
from Validators.person_validator import PersonValidator


class TestPersonDomainCases(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Person One")
        self.person2 = Person("Person Two")
        self.person3 = Person("Person Three")
        self.person1Copy = Person("Person OneCopy")
        self.person1Copy.forceID(self.person1.getID())
        self.person1ID = 1
        self.person2ID = 2
        self.person3ID = 3

    def tearDown(self):
        del self.person1
        del self.person2
        del self.person3
        del self.person1Copy
        Person.resetIDValues()

    def test_eqOverload(self):
        self.assertEqual(self.person1, self.person1Copy)

    def test_neOverload(self):
        self.assertNotEqual(self.person1, self.person2)
        self.assertFalse(self.person1 == self.person2)
        self.assertTrue(self.person1 != self.person3)
        self.assertFalse(self.person1 != self.person1)
        self.assertNotEqual(self.person2, self.person3)

    def test_strOverload(self):
        self.assertEqual(str(self.person1), "\x1b[36m1\x1b[39m: Person One")

    def test_getLastUsedID(self):
        self.newPerson = Person("New!")
        self.assertEqual(Person.getLastUsedID(), self.newPerson.getID())

    def test_GetName(self):
        self.assertEqual(self.person1.getName(), "Person One")
        self.assertEqual(self.person2.getName(), "Person Two")
        self.assertEqual(self.person3.getName(), "Person Three")

    def test_GetID(self):
        self.assertEqual(self.person1.getID(), self.person1ID)
        self.assertEqual(self.person2.getID(), self.person2ID)
        self.assertEqual(self.person3.getID(), self.person3ID)

    def test_SetName(self):
        self.person1.setName("Person Modified")
        self.assertEqual(self.person1.getName(), "Person Modified")

    def test_ForceID(self):
        self.person1.forceID(505404)
        self.assertEqual(self.person1.getID(), 505404)

class TestEventDomainCases(unittest.TestCase):
    def setUp(self):
        self.event1 = Event("Event 1 Street", "01.01.01", "12:30", "Event Number 1")
        self.event2 = Event("Event 2 Street", "02.01.01", "12:30", "Event Number 2")
        self.event3 = Event("Event 3 Street", "03.01.01", "12:30", "Event Number 3")
        self.event1Copy = Event("Event 1 Copy Street", "01.01.01", "12:30", "Event Number 1 Copy")
        self.event1Copy.forceID(self.event1.getID())
        self.event1ID = 1
        self.event2ID = 2
        self.event3ID = 3

    def tearDown(self):
        Event.resetIDValues()
        del self.event1
        del self.event2
        del self.event3
        del self.event1Copy

    def test_eqOverload(self):
        self.assertEqual(self.event1, self.event1Copy)

    def test_neOverload(self):
        self.assertNotEqual(self.event1, self.event2)
        self.assertFalse(self.event1 == self.event2)
        self.assertTrue(self.event1 != self.event3)
        self.assertFalse(self.event1 != self.event1)
        self.assertNotEqual(self.event2, self.event3)

    def test_strOverload(self):
        self.assertEqual(str(self.event1), "\x1b[36m1\x1b[39m: Event 1 Street | 01.01.01 | 12:30 | Event Number 1")

    def test_getLastUsedID(self):
        self.newEvent = Event.getDummyEvent()
        self.assertEqual(Event.getLastUsedID(), self.newEvent.getID())

    def test_GetAddress(self):
        self.assertEqual(self.event1.getAddress(), "Event 1 Street")
        self.assertEqual(self.event2.getAddress(), "Event 2 Street")
        self.assertEqual(self.event3.getAddress(), "Event 3 Street")

    def test_GetDate(self):
        self.assertEqual(self.event1.getDate(), "01.01.01")
        self.assertEqual(self.event2.getDate(), "02.01.01")
        self.assertEqual(self.event3.getDate(), "03.01.01")

    def test_GetTime(self):
        self.assertEqual(self.event1.getTime(), "12:30")
        self.assertEqual(self.event2.getTime(), "12:30")
        self.assertEqual(self.event3.getTime(), "12:30")

    def test_GetDesc(self):
        self.assertEqual(self.event1.getDescription(), "Event Number 1")
        self.assertEqual(self.event2.getDescription(), "Event Number 2")
        self.assertEqual(self.event3.getDescription(), "Event Number 3")

    def test_GetID(self):
        self.assertEqual(self.event1.getID(), self.event1ID)
        self.assertEqual(self.event2.getID(), self.event2ID)
        self.assertEqual(self.event3.getID(), self.event3ID)

    def test_SetAddress(self):
        self.event1.setAddress("Set Address")
        self.assertEqual(self.event1.getAddress(), "Set Address")

    def test_SetDate(self):
        self.event1.setDate("06.06.06")
        self.assertEqual(self.event1.getDate(), "06.06.06")

    def test_SetTime(self):
        self.event1.setTime("20:30")
        self.assertEqual(self.event1.getTime(), "20:30")

    def test_SetDesc(self):
        self.event1.setDescription("Set Description")
        self.assertEqual(self.event1.getDescription(), "Set Description")

    def test_ForceID(self):
        self.event1.forceID(505404)
        self.assertEqual(self.event1.getID(), 505404)

class TestBucketDomainCases(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Person One")
        self.person2 = Person("Person Two")
        self.event1 = Event("Event 1 Street", "01.01.01", "12:30", "Event Number 1")
        self.event2 = Event("Event 2 Street", "02.01.01", "12:30", "Event Number 2")
        self.bucket1 = Bucket(self.person1, self.event1)
        self.bucket2 = Bucket(self.person2, self.event1)
        self.bucket1Copy = Bucket(self.person1, self.event1)

    def tearDown(self):
        del self.person1
        del self.person2
        del self.event1
        del self.event2
        del self.bucket1
        del self.bucket2
        del self.bucket1Copy
        Person.resetIDValues()
        Event.resetIDValues()

    def test_eqOverload(self):
        self.assertTrue(self.bucket1 == self.bucket1Copy)
        self.assertFalse(self.bucket1 == self.bucket2)

    def test_neOverload(self):
        self.assertTrue(self.bucket1 != self.bucket2)
        self.assertFalse(self.bucket1 != self.bucket1)

    def test_strOverload(self):
        self.assertEqual(str(self.bucket1), str(self.person1) + "\x1b[35m <-> \x1b[39m" + str(self.event1))

    def test_GetBucket(self):
        self.assertEqual(self.bucket1.getBucket(), [self.person1, self.event1])
        self.assertEqual(self.bucket2.getBucket(), [self.person2, self.event1])

    def test_SetBucket(self):
        self.bucket1.setBucket(self.person1, self.event2)
        self.assertEqual(self.bucket1.getBucket(), [self.person1, self.event2])

    def test_ExtractPerson(self):
        self.assertIs(self.bucket1.extractPerson(), self.person1)
        self.assertIs(self.bucket2.extractPerson(), self.person2)

    def test_ExtractEvent(self):
        self.assertIs(self.bucket1.extractEvent(), self.event1)
        self.assertIs(self.bucket2.extractEvent(), self.event1)

class TestRepositoryCases(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Person One")
        self.person2 = Person("Person Two")
        self.person1Copy = Person("Person One Copy")
        self.person1Copy.forceID(self.person1.getID())
        self.event1 = Event("Event 2 Street", "02.01.01", "12:30", "Event Number 2")
        self.event2 = Event("Event 3 Street", "03.01.01", "12:30", "Event Number 3")
        self.event1Copy = Event("Event 1 Copy Street", "01.01.01", "12:30", "Event Number 1 Copy")
        self.event1Copy.forceID(self.event1.getID())

        self.repoNumbers = Repository()
        self.repoPersons = Repository()
        self.repoEvents = Repository()

    def tearDown(self):
        del self.person1
        del self.person2
        del self.person1Copy
        del self.event1
        del self.event2
        del self.event1Copy
        Person.resetIDValues()
        Event.resetIDValues()

    def test_strOverload(self):
        self.repoNumbers.addElement(1)
        self.repoNumbers.addElement(2)
        self.assertEqual(str(self.repoNumbers), "[1, 2, ]")

    def test_lenOverload(self):
        self.repoNumbers.addElement(1)
        self.repoNumbers.addElement(2)
        self.assertEqual(len(self.repoNumbers), 2)

    def test_getAllElements(self):
        self.repoNumbers.addElement(1)
        self.repoNumbers.addElement(2)
        self.repoPersons.addElement(self.person1)
        self.repoEvents.addElement(self.event1)
        self.repoEvents.addElement(self.event2)
        self.assertEqual(self.repoNumbers.getAllElements(), [1, 2])
        self.assertEqual(self.repoPersons.getAllElements(), [self.person1])
        self.assertEqual(self.repoEvents.getAllElements(), [self.event1, self.event2])

    def test_addElementWHITEBOX(self):
        self.repoNumbers.addElement(1)
        self.assertEqual(self.repoNumbers.getAllElements(), [1])
        self.repoNumbers.addElement(2)
        self.assertEqual(self.repoNumbers.getAllElements(), [1, 2])
        self.assertRaises(RepositoryError, self.repoNumbers.addElement, 2)
        self.repoPersons.addElement(self.person1)
        self.assertEqual(self.repoPersons.getAllElements(), [self.person1])
        self.repoEvents.addElement(self.event1)
        self.assertEqual(self.repoEvents.getAllElements(), [self.event1])
        self.repoEvents.addElement(self.event2)
        self.assertEqual(self.repoEvents.getAllElements(), [self.event1, self.event2])

    def test_addElementBLACKBOX(self):
        self.repoNumbers.addElement(1)
        self.assertEqual(self.repoNumbers.getAllElements(), [1])
        self.repoNumbers.addElement(100)
        self.assertEqual(self.repoNumbers.getAllElements(), [1, 100])

    def test_getElement(self):
        self.repoPersons.addElement(self.person1)
        self.assertIs(self.repoPersons.getElement(self.person1Copy), self.person1)
        self.assertRaises(RepositoryError, self.repoNumbers.getElement, 2)

    def test_getElementByIndex(self):
        self.repoPersons.addElement(self.person1)
        self.repoPersons.addElement(self.person2)
        self.assertEqual(self.repoPersons.getElementByIndex(0), self.person1)
        self.assertEqual(self.repoPersons.getElementByIndex(1), self.person2)
        self.assertRaises(RepositoryError, self.repoNumbers.getElementByIndex, 2)

    def test_removeElement(self):
        self.repoPersons.addElement(self.person1)
        self.repoPersons.addElement(self.person2)
        self.assertEqual(len(self.repoPersons), 2)
        self.assertEqual(self.repoPersons.getAllElements(), [self.person1, self.person2])
        self.repoPersons.removeElement(self.person1Copy)
        self.assertEqual(len(self.repoPersons), 1)
        self.assertEqual(self.repoPersons.getAllElements(), [self.person2])
        self.assertRaises(RepositoryError, self.repoNumbers.removeElement, 2)

    def test_modifyElement(self):
        self.repoPersons.addElement(self.person1)
        self.person1Copy.setName("Person Modified")
        self.repoPersons.modifyElement(self.person1Copy)
        self.assertEqual(self.repoPersons.getElement(self.person1).getName(), "Person Modified")
        self.assertRaises(RepositoryError, self.repoNumbers.modifyElement, 2)

    def test_setNewElementList(self):
        self.repoNumbers.setNewElementList([0, 3, 4])
        self.assertEqual(self.repoNumbers.getAllElements(), [0, 3, 4])

class TestGeneratorCases(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Person One")
        self.person2 = Person("Person Two")
        self.event1 = Event("Event 1 Street", "01.01.01", "12:30", "Event Number 1")
        self.event2 = Event("Event 2 Street", "02.01.01", "12:30", "Event Number 2")
        self.personList = [self.person1, self.person2]
        self.eventList = [self.event1, self.event2]

    def tearDown(self):
        del self.person1
        del self.person2
        del self.event1
        del self.event2
        Person.resetIDValues()
        Event.resetIDValues()

    def test_GenerateRandomPersons(self):
        number = 5
        lst = generateRandomPersons(number)
        self.assertEqual(len(lst), number)
        number = 0
        lst = generateRandomPersons(number)
        self.assertEqual(len(lst), number)

    def test_generateRandomEvents(self):
        number = 5
        lst = generateRandomEvents(number)
        self.assertEqual(len(lst), number)
        number = 0
        lst = generateRandomEvents(number)
        self.assertEqual(len(lst), number)

    def test_generateRandomBuckets(self):
        lst = generateRandomBuckets(self.personList, self.eventList)
        self.assertGreaterEqual(len(lst), 10 * 3)
        self.assertLessEqual(len(lst), 25 * 10)
        self.assertIn(lst[0][0], [1, 2])
        self.assertIn(lst[0][1], [1, 2])
        self.assertIn(lst[1][0], [1, 2])
        self.assertIn(lst[1][1], [1, 2])

class TestPersonServiceCases(unittest.TestCase):
    def setUp(self):
        self.personRepo = Repository()
        self.personValidator = PersonValidator()
        self.bucketRepo = Repository()
        self.bucketValidator = BucketValidator()
        self.bucketService = BucketService(self.bucketRepo, self.bucketValidator)

        self.person1 = Person("Person One")
        self.person2 = Person("Person Two")
        self.person1Copy = Person("Person One Copy")
        self.person1Copy.forceID(self.person1.getID())

        self.personService = PersonService(self.personRepo, self.personValidator, self.bucketService)

    def tearDown(self):
        del self
        Person.resetIDValues()
        Event.resetIDValues()

    def test_getAllPersons(self):
        self.personService.addPerson(self.person1)
        self.assertEqual(self.personService.getAllPersons(), [self.person1])
        self.personService.addPerson(self.person2)
        self.assertEqual(self.personService.getAllPersons(), [self.person1, self.person2])

    def test_getPerson(self):
        self.personService.addPerson(self.person1)
        self.assertEqual(self.personService.getPerson(self.person1), self.person1)
        self.assertEqual(self.personService.getPerson(self.person1), self.person1Copy)

    def test_getPersonRawID(self):
        self.personService.addPerson(self.person1)
        self.assertEqual(self.personService.getPersonRawID(1), self.person1)
        self.assertEqual(self.personService.getPersonRawID(1), self.person1Copy)

    def test_getAllPersonsWithName(self):
        self.personService.addPerson(self.person1)
        self.assertEqual(self.personService.getAllPersonsWithName("Person"), [self.person1])
        self.personService.addPerson(self.person2)
        self.assertEqual(self.personService.getAllPersonsWithName("Person"), [self.person1, self.person2])

    def test_addPerson(self):
        self.assertEqual(self.personService.getAllPersons(), [])
        self.personService.addPerson(self.person1)
        self.assertEqual(self.personService.getAllPersons(), [self.person1])
        self.personService.addPerson(self.person2)
        self.assertEqual(self.personService.getAllPersons(), [self.person1, self.person2])

    def test_addMultiplePersons(self):
        self.personService.addMultiplePersons([self.person1, self.person2])
        self.assertEqual(self.personService.getAllPersons(), [self.person1, self.person2])
        self.assertRaises(RepositoryError, self.personService.addMultiplePersons, [self.person1, self.person2])

    def test_addPersonRaw(self):
        self.personService.addPersonRaw("Raw Person")
        self.assertEqual(len(self.personService.getAllPersonsWithName("Raw Person")), 1)

    def test_modifyPerson(self):
        self.person1Copy.setName("Modified Name")
        self.personService.addPerson(self.person1)
        self.personService.modifyPerson(self.person1Copy)
        self.assertEqual(len(self.personService.getAllPersons()), 1)
        self.assertEqual(self.personService.getAllPersons()[0].getName(), "Modified Name")

    def test_modifyPersonRaw(self):
        self.personService.addPerson(self.person1)
        self.personService.modifyPersonRaw(self.person1.getID(), "Modified Name")
        self.assertEqual(len(self.personService.getAllPersons()), 1)
        self.assertEqual(self.personService.getAllPersons()[0].getName(), "Modified Name")

    def test_deletePerson(self):
        self.personService.addPerson(self.person1)
        self.personService.deletePerson(self.person1Copy)
        self.assertEqual(len(self.personService.getAllPersons()), 0)
        self.assertEqual(self.personService.getAllPersons(), [])

    def test_deletePersonRaw(self):
        self.personService.addPerson(self.person1)
        self.personService.deletePersonRaw(self.person1.getID())
        self.assertEqual(len(self.personService.getAllPersons()), 0)
        self.assertEqual(self.personService.getAllPersons(), [])

class TestEventServiceCases(unittest.TestCase):
    def setUp(self):
        self.eventRepo = Repository()
        self.eventValidator = EventValidator()
        self.bucketRepo = Repository()
        self.bucketValidator = BucketValidator()
        self.bucketService = BucketService(self.bucketRepo, self.bucketValidator)

        self.event1 = Event("Event 1 Street", "01.01.01", "12:30", "Event Number 1")
        self.event2 = Event("Event 2 Street", "02.01.01", "12:30", "Event Number 2")
        self.event3 = Event("Event 3 Street", "03.01.01", "12:30", "Event Number 3")
        self.event1Copy = Event("Event 1 Copy Street", "01.01.01", "12:30", "Event Number 1 Copy")
        self.event1Copy.forceID(self.event1.getID())

        self.eventService = EventService(self.eventRepo, self.eventValidator, self.bucketService)

    def tearDown(self):
        del self
        Person.resetIDValues()
        Event.resetIDValues()

    def test_getAllEvents(self):
        self.assertEqual(self.eventService.getAllEvents(), [])
        self.eventService.addEvent(self.event1)
        self.assertEqual(self.eventService.getAllEvents(), [self.event1])
        self.eventService.addEvent(self.event2)
        self.eventService.addEvent(self.event3)
        self.assertEqual(self.eventService.getAllEvents(), [self.event1, self.event2, self.event3])

    def test_getEvent(self):
        self.eventService.addEvent(self.event1)
        self.assertEqual(self.eventService.getEvent(self.event1), self.event1)
        self.assertEqual(self.eventService.getEvent(self.event1Copy), self.event1)

    def test_getEventRawID(self):
        self.eventService.addEvent(self.event1)
        self.assertEqual(self.eventService.getEventRawID(self.event1.getID()), self.event1)
        self.assertEqual(self.eventService.getEventRawID(self.event1Copy.getID()), self.event1)

    def test_getAllEventsWithAddress(self):
        self.eventService.addEvent(self.event1)
        self.eventService.addEvent(self.event2)
        self.eventService.addEvent(self.event3)
        self.assertEqual(self.eventService.getAllEventsWithAddress("Event"), [self.event1, self.event2, self.event3])
        self.assertEqual(self.eventService.getAllEventsWithAddress("2"), [self.event2])

    def test_getAllEventsWithDate(self):
        self.eventService.addEvent(self.event1)
        self.eventService.addEvent(self.event2)
        self.eventService.addEvent(self.event3)
        self.assertEqual(self.eventService.getAllEventsWithDate("01.01.01"), [self.event1])
        self.assertEqual(self.eventService.getAllEventsWithDate("02.01.01"), [self.event2])

    def test_getAllEventsWithTime(self):
        self.eventService.addEvent(self.event1)
        self.eventService.addEvent(self.event2)
        self.eventService.addEvent(self.event3)
        self.assertEqual(self.eventService.getAllEventsWithTime("12:30"), [self.event1, self.event2, self.event3])

    def test_addEvent(self):
        self.assertEqual(self.eventService.getAllEvents(), [])
        self.assertEqual(len(self.eventService.getAllEvents()), 0)
        self.eventService.addEvent(self.event1)
        self.assertEqual(self.eventService.getAllEvents(), [self.event1])
        self.assertEqual(len(self.eventService.getAllEvents()), 1)

    def test_addMultipleEvents(self):
        self.assertEqual(self.eventService.getAllEvents(), [])
        self.assertEqual(len(self.eventService.getAllEvents()), 0)
        self.eventService.addMultipleEvents([self.event1, self.event3])
        self.assertEqual(self.eventService.getAllEvents(), [self.event1, self.event3])
        self.assertEqual(len(self.eventService.getAllEvents()), 2)

    def test_addEventRaw(self):
        self.assertEqual(self.eventService.getAllEvents(), [])
        self.assertEqual(len(self.eventService.getAllEvents()), 0)
        self.eventService.addEventRaw("Raw", "01.01.01", "12:30", "Raw")
        self.assertEqual(self.eventService.getAllEvents()[0].getDescription(), "Raw")
        self.assertEqual(len(self.eventService.getAllEvents()), 1)

    def test_modifyEvent(self):
        self.eventService.addEvent(self.event1)
        self.event1Copy.setDescription("Modified Description")
        self.eventService.modifyEvent(self.event1Copy)
        self.assertEqual(self.eventService.getAllEvents()[0].getDescription(), "Modified Description")

    def test_modifyEventRaw(self):
        self.eventService.addEvent(self.event1)
        self.eventService.modifyEventRaw(self.event1.getID(), self.event1.getAddress(), self.event1.getDate(), self.event1.getTime(), "Modified Description")
        self.assertEqual(self.eventService.getAllEvents()[0].getDescription(), "Modified Description")

    def test_deleteEvent(self):
        self.eventService.addEvent(self.event1)
        self.eventService.deleteEvent(self.event1Copy)
        self.assertEqual(self.eventService.getAllEvents(), [])

    def test_deleteEventRaw(self):
        self.eventService.addEvent(self.event1)
        self.eventService.deleteEventRaw(self.event1.getID())
        self.assertEqual(self.eventService.getAllEvents(), [])

class TestBucketServiceCases(unittest.TestCase):
    def setUp(self):
        self.repo = Repository()
        self.valid = BucketValidator()
        self.bucketService = BucketService(self.repo, self.valid)
        self.p1 = Person.getDummyPerson()
        self.p2 = Person.getDummyPerson()
        self.p1Copy = Person.getDummyPerson()
        self.p1Copy.forceID(self.p1.getID())
        self.e1 = Event.getDummyEvent()
        self.e2 = Event.getDummyEvent()
        self.e3 = Event.getDummyEvent()
        self.e1Copy = Event.getDummyEvent()
        self.e1Copy.forceID(self.e1.getID())
        self.b1 = Bucket(self.p1, self.e1)
        self.b2 = Bucket(self.p1, self.e2)
        self.b3 = Bucket(self.p1, self.e3)
        self.b4 = Bucket(self.p2, self.e1)
        self.b5 = Bucket(self.p2, self.e2)
    def tearDown(self):
        del self
        Person.resetIDValues()
        Event.resetIDValues()

    def test_getAllBuckets(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getAllBuckets(), [self.b1, self.b2])

    def test_getBucket(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.assertEqual(self.bucketService.getBucket(self.b1), self.b1)

    def test_getAllBucketsWithPerson(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.bucketService.addBucket(self.p1, self.e3)
        self.assertEqual(self.bucketService.getAllBucketsWithPerson(self.p1), [self.b1, self.b2, self.b3])

    def test_getAllBucketsWithPersonRecursive(self):
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e2)
        self.bucketService.addBucket(self.p1, self.e2)
        self.bucketService.addBucket(self.p2, self.e3)
        self.bucketService.addBucket(self.p1, self.e3)
        self.assertEqual(self.bucketService.getAllBucketsWithPersonRecursive(self.p1), [self.b3, self.b2, self.b1])

    def test_getAllBucketsWithEvent(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.assertEqual(self.bucketService.getAllBucketsWithEvent(self.e1), [self.b1, self.b4])

    def test_getAllBucketsWithEventRecursive(self):
        self.bucketService.addBucket(self.p2, self.e2)
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getAllBucketsWithEventRecursive(self.e1), [self.b4, self.b1])

    def test_addBucket(self):
        self.assertEqual(self.bucketService.getAllBuckets(), [])
        self.bucketService.addBucket(self.p1, self.e1)
        self.assertEqual(self.bucketService.getAllBuckets(), [self.b1])

    def test_addBucketComplete(self):
        self.assertEqual(self.bucketService.getAllBuckets(), [])
        self.bucketService.addBucketComplete(self.b1)
        self.assertEqual(self.bucketService.getAllBuckets(), [self.b1])

    def test_modifyBucketsWithPerson(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.bucketService.addBucket(self.p1, self.e3)
        self.p1Copy.setName("Modified Name")
        self.bucketService.modifyBucketsWithPerson(self.p1Copy)
        self.bucketList = self.bucketService.getAllBucketsWithPerson(self.p1)
        for bucket in self.bucketList:
            self.assertEqual(bucket.extractPerson().getName(), "Modified Name")

    def test_modifyBucketsWithEvent(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.e1Copy.setAddress("Modified Address")
        self.bucketService.modifyBucketsWithEvent(self.e1Copy)
        self.bucketList = self.bucketService.getAllBucketsWithEvent(self.e1)
        for bucket in self.bucketList:
            self.assertEqual(bucket.extractEvent().getAddress(), "Modified Address")

    def test_removeBucketsWithPerson(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.bucketService.addBucket(self.p1, self.e3)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.removeBucketsWithPerson(self.p1)
        self.assertEqual(self.bucketService.getAllBuckets(), [self.b4])

    def test_removeBucketsWithEvent(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p2, self.e2)
        self.bucketService.removeBucketsWithEvent(self.e1)
        self.assertEqual(self.bucketService.getAllBuckets(), [self.b5])

    def test_getOrderedEventsByPersons(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getOrderedEventsByPersons([self.e1, self.e2]), [(self.e1, 2), (self.e2, 1)])

    def test_getListOfPersonsWithMostEvents(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getListOfPersonsWithMostEvents([self.p1, self.p2]), [(self.p1, 2), (self.p2, 1)])

    def test_getOrderedListOfEvents(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getOrderedListOfEvents(self.p1), [self.b1, self.b2])

    def test_getAverageEventsPerPerson(self):
        self.bucketService.addBucket(self.p1, self.e1)
        self.bucketService.addBucket(self.p2, self.e1)
        self.bucketService.addBucket(self.p1, self.e2)
        self.assertEqual(self.bucketService.getAverageEventsPerPerson([self.p1, self.p2]), 3/2)

class TestPersonValidatorCases(unittest.TestCase):
    def setUp(self):
        self.validPerson = Person("I am valid")
        self.notValidPersonCharacter = Person("Not Valid 5")
        self.notValidPersonSpaces = Person("   ")
        self.notValidIDPerson = Person("Not valid!")
        self.notValidIDPerson.forceID(-1)

        self.validator = PersonValidator()

    def tearDown(self):
        del self
        Person.resetIDValues()

    def test_validatePerson(self):
        self.assertRaises(PersonError, self.validator.validatePerson, self.notValidPersonCharacter)
        self.assertRaises(PersonError, self.validator.validatePerson, self.notValidPersonSpaces)
        self.assertRaises(PersonError, self.validator.validatePerson, self.notValidIDPerson)

class TestEventValidatorCases(unittest.TestCase):
    def setUp(self):
        self.notValidAddress = Event("  ", "01.01.01", "15:30", "Not valid")
        self.notValidID = Event("Valid", "01.01.01", "15:30", "Not valid")
        self.notValidID.forceID(-1)

        self.notValidDate = Event("Valid", "  ", "15:30", "Not valid")
        self.notValidDate2 = Event("Valid", "01", "15:30", "Not valid")
        self.notValidDate3 = Event("Valid", "0g.2f.2d", "15:30", "Not valid")

        self.notValidTime = Event("Valid", "01.01.01", "   ", "Not valid")
        self.notValidTime2 = Event("Valid", "01.01.01", "15:30:50", "Not valid")
        self.notValidTime3 = Event("Valid", "01.01.01", "15:gf", "Not valid")
        self.validator = EventValidator()

    def tearDown(self):
        del self
        Event.resetIDValues()

    def test_validateEvent(self):
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidAddress)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidID)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidDate)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidDate2)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidDate3)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidTime)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidTime2)
        self.assertRaises(EventError, self.validator.validateEvent, self.notValidTime3)

class TestFileRepositoryCases(unittest.TestCase):
    def setUp(self):
        self.testPersonsFile = "Datafiles/TEST_PERSONS.entries"
        self.testEventsFile = "Datafiles/TEST_EVENTS.entries"
        self.testRelationsFile = "Datafiles/TEST_RELATIONS.entries"
        self.personRepo = FileRepository(self.testPersonsFile)
        self.eventRepo = FileRepository(self.testEventsFile)
        self.bucketRepo = FileRepository(self.testRelationsFile)

        self.person1 = Person("Test Person One")
        self.person1.forceID(1)
        self.person2 = Person("Test Person Two")
        self.person2.forceID(2)
        self.event1 = Event("Address", "01.01.01", "15:30", "Event One")
        self.event1.forceID(1)
        self.event2 = Event("Address Two", "02.02.02", "18:00", "Event Two")
        self.event2.forceID(2)
        self.bucket1 = Bucket(self.person1, self.event1)
        self.bucket2 = Bucket(self.person2, self.event2)

    def tearDown(self):
        Person.resetIDValues()
        Event.resetIDValues()
        del self

    def test_loadAndSave(self):
        self.assertEqual(self.personRepo.getAllElements()[0].getID(), self.person1.getID())
        self.assertEqual(self.personRepo.getAllElements()[1].getID(), self.person2.getID())
        self.assertEqual(self.eventRepo.getAllElements()[0].getID(), self.event1.getID())
        self.assertEqual(self.eventRepo.getAllElements()[1].getID(), self.event2.getID())
        self.assertEqual(self.bucketRepo.getAllElements()[0].extractPerson().getID(), self.person1.getID())
        self.assertEqual(self.bucketRepo.getAllElements()[1].extractPerson().getID(), self.person2.getID())
        self.assertEqual(self.bucketRepo.getAllElements()[0].extractEvent().getID(), self.event1.getID())
        self.assertEqual(self.bucketRepo.getAllElements()[1].extractEvent().getID(), self.event2.getID())

        self.personRepo.saveElementsToFile()
        self.eventRepo.saveElementsToFile()
        self.bucketRepo.saveElementsToFile()

        with open(self.testPersonsFile, "r") as testRead:
            self.assertEqual(testRead.readline(), "#TYPEPERSON\n")
            self.assertEqual(testRead.readline(), str(self.person1.getID())+";"+self.person1.getName()+"\n")
            self.assertEqual(testRead.readline(), str(self.person2.getID())+";"+self.person2.getName()+"\n")
            self.assertEqual(testRead.readline(), "")
        with open(self.testEventsFile, "r") as testRead:
            self.assertEqual(testRead.readline(), "#TYPEEVENT\n")
            self.assertEqual(testRead.readline(), str(self.event1.getID())+";"+self.event1.getAddress()+";"+self.event1.getDate()+";"+self.event1.getTime()+";"+self.event1.getDescription()+"\n")
            self.assertEqual(testRead.readline(), str(self.event2.getID())+";"+self.event2.getAddress()+";"+self.event2.getDate()+";"+self.event2.getTime()+";"+self.event2.getDescription()+"\n")
            self.assertEqual(testRead.readline(), "")
            self.assertEqual(testRead.readline(), "")
        with open(self.testRelationsFile, "r") as testRead:
            self.assertEqual(testRead.readline(), "#TYPERELATION\n")
            self.assertEqual(testRead.readline(), "1;Test Person One;1;Address;01.01.01;15:30;Event One\n")
            self.assertEqual(testRead.readline(), "2;Test Person Two;2;Address Two;02.02.02;18:00;Event Two\n")
            self.assertEqual(testRead.readline(), "")


def runTests():
    unittest.main(module="UnitTests.tests", exit=False, verbosity=2)
