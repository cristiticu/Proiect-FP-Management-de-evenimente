from Exceptions.custom_exceptions import EventError

class EventValidator:
    """
    Validator Class for the Event Model
    """
    def __init__(self):
        """
        Empty constructor
        """
        pass

    def validateEvent(self, event):
        """
        Method that validates an event. Raises EventError if contents do not comply
        :param event: The event to validate
        :return: None
        """
        errors = ""

        if event.getID() < 0:
            errors += "Bad ID for Event\n"

        if event.getAddress() == "" or event.getAddress().isspace():
            errors += "Bad Address for Event\n"

        date = event.getDate()
        dateElems = date.split('.')
        if event.getDate() == "" or event.getDate().isspace():
            errors += "Bad Date for Event\n"
        elif len(dateElems) != 3:
            errors += "Bad Date for Event\n"
        else:
            for dateElem in dateElems:
                if not dateElem.isnumeric():
                    errors += "Bad Date for Event\n"

        time = event.getTime()
        timeElems = time.split(':')
        if event.getTime() == "" or event.getTime().isspace():
            errors += "Bad Time for Event\n"
        elif len(timeElems) != 2:
            errors += "Bad Time for Event\n"
        else:
            for timeElem in timeElems:
                if not timeElem.isnumeric():
                    errors += "Bad Time for Event\n"

        if len(errors) > 0:
            raise EventError(errors)
