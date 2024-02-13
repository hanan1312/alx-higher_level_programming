import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "Alice"}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "Alice"}]')

    def test_save_to_file_empty(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_non_empty(self):
        json_string = '[{"id": 30, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 30, "name": "Bob"}])

    def test_create_empty(self):
        self.assertEqual(Base.create(), None)

  self.assertEqual([obj.id for obj in objects], [50, 60])

if __name__ == "__main__":
    unittest.main()
