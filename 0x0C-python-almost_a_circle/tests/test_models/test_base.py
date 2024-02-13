import unittest
import json
from models.base import Base

""" test base class """
class TestBase(unittest.TestCase):

    def test_init_with_id(self):
    """ test init with width id function """
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
    """ test init without id function """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
    """ test to json str empty function """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
     """ test to json str non empty function """
        data = [{"id": 1, "name": "Alice"}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "Alice"}]')

    def test_save_to_file_empty(self):
    """ test empty save to file function """
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string_empty(self):
    """ test from json to str empty function """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_non_empty(self):
    """ test from json str non empty function """
        json_string = '[{"id": 30, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 30, "name": "Bob"}])

    def test_create_empty(self):
    """ test create empty function """
        self.assertEqual(Base.create(), None)

if __name__ == "__main__":
    unittest.main()
