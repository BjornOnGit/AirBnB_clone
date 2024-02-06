"""This is the file storage class for AirBnB"""
import json

class FileStorage:
    """ 
    This class  serializes instances to a JSON file and deserializes JSON files to instances
    """
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, _ = key.split('.')
                    cls = globals()[class_name]
                    self.__objects[key] = cls.from_dict(value)
        except FileNotFoundError:
            pass
