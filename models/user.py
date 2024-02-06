#!/usr/bin/python3
"""Defines the User class."""
#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from base model.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self):
        BaseModel.__init__(self)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
    
    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of the instance"""
        return {
            "__class__": "User",
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
