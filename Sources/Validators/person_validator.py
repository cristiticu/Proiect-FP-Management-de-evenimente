from Exceptions.custom_exceptions import PersonError

class PersonValidator:
    """
    Validator Class for the Person Model
    """
    def __init__(self):
        """
        Empty Initializer
        """
        pass

    def validatePerson(self, person):
        """
        Method for validating a person Instance
        :param person: The person to validate
        :return: None, raises PersonError if contents do not comply
        """
        errors = ""

        if person.getID() < 0:
            errors += "Bad ID for Person\n"
        if person.getName() == "" or person.getName().isspace():
            errors += "Bad Name for Person\n"

        for char in person.getName():
            if ord(char) != 32 and (65 > ord(char) or ord(char) > 90) and (97 > ord(char) or ord(char) > 122):
                errors += "Bad Name for Person\n"
                break

        if len(errors) > 0:
            raise PersonError(errors)
