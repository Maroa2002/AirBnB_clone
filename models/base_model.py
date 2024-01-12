#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""contains the parent class BaseModel"""


class BaseModel:
    """The parent class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance with a unique id,
        created_at, and updated_at attributes.
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime\
                        .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """prints: [<class name>] (<self.id>) <self.__dict__>"""

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic