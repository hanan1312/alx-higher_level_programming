import unittest
import json
from models.base import Base

""" test base class """
class TestBase(unittest.TestCase):

    """ test init with width id function """
    def test_init_with_id(self):
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    """ test init without id function """
    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    """ test to json str empty function """
    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    """ test to json str non empty function """
    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "Alice"}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "Alice"}]')

    """ test empty save to file function """
    def test_save_to_file_empty(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    """ test from json to str empty function """
    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    """ test from json str non empty function """
    def test_from_json_string_non_empty(self):
        json_string = '[{"id": 30, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 30, "name": "Bob"}])

    """ test create empty function """
    def test_create_empty(self):
        self.assertEqual(Base.create(), None)

if __name__ == "__main__":
    unittest.main()
