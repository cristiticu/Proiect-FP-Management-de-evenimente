from Validators.person_validator import PersonValidator
from Validators.event_validator import EventValidator

class BucketValidator:
    """
    Bucket Validator Class
    """
    def __init__(self):
        """
        Empty Constructor
        """
        pass

    def validateBucket(self, bucket):
        """
        Method for validating a bucket. Raises an exception if contents do not comply
        :param bucket: A bucket Instance
        :return: None
        """
        personValidator = PersonValidator()
        eventValidator = EventValidator()

        personValidator.validatePerson(bucket.extractPerson())
        eventValidator.validateEvent(bucket.extractEvent())
