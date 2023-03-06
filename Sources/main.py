from UIs.console import Console
from Repositories.repository import Repository
from Repositories.file_repository import FileRepository

from Services.person_service import PersonService
from Validators.person_validator import PersonValidator

from Services.event_service import EventService
from Validators.event_validator import EventValidator

from Services.bucket_service import BucketService
from Validators.bucket_validator import BucketValidator

from UnitTests.tests import runTests

if __name__ == '__main__':
    runTests()

    selection = False
    userInput = ""
    while not selection:
        print("Select an operating mode\n1 - Memory Mode\n2 - File Mode")
        userInput = input()
        if userInput == "1":
            selection = True
            personRepo = Repository()
            eventRepo = Repository()
            bucketRepo = Repository()
        elif userInput == "2":
            selection = True
            personRepo = FileRepository("Datafiles/persons.entries")
            eventRepo = FileRepository("Datafiles/events.entries")
            bucketRepo = FileRepository("Datafiles/relations.entries")

    personValid = PersonValidator()
    eventValid = EventValidator()
    bucketValid = BucketValidator()

    bucketService = BucketService(bucketRepo, bucketValid)
    personService = PersonService(personRepo, personValid, bucketService)
    eventService = EventService(eventRepo, eventValid, bucketService)

    mainConsoleDriver = Console(personService, eventService, bucketService)

    mainConsoleDriver.renderMainMenuUI()

    if userInput == "2":
        print("\nSave Changes?\n1 - Yes\n2 - No")
        saveChanges = input()
        if saveChanges == "1":
            personRepo.saveElementsToFile()
            eventRepo.saveElementsToFile()
            bucketRepo.saveElementsToFile()
