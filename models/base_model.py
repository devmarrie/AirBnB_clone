#!/usr/bin/python3
import uuid
from datetime import datetime

"""
This is the base class of the AirBnb clone
It defines all common attributes/methods for other classes
"""


class BaseModel():
    """
    Containing both private and public attributes and methods.
    """
    def __init__(self):
        """
        It makes us able to create instance attributes
        attributes with (__) eg __str__ are called like str()
        those defined normally are called to the object after a dot
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print: [<class name>] (<self.id>)
        """
        class_name = self.__class__.__name__
        inst_id = self.id
        dict = self.__dict__
        return '[{}] ({}) {}'.format(class_name, inst_id, dict)

    def save(self):
        """
        updates the public instance attribute updated_at
        and gives it the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictonary with all key values of __dict__
        of the instance we created above and the class name
        Also returns the time in isoformat
        """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
