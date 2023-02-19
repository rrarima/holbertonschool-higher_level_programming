import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """
    
    def test_auto_assign_id(self):
        """
        Test that Base assigns a unique ID automatically.
        """
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
    
    def test_auto_assign_id_plus_one(self):
        """
        Test that Base assigns an ID that is one greater than the
        previous ID if it exists.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b2.id + 1, b3.id)
    
    def test_save_passed_id(self):
        """
        Test that Base saves the ID passed to it.
        """
        b = Base(89)
        self.assertEqual(b.id, 89)
    
    def test_to_json_string_with_none(self):
        """
        Test that Base.to_json_string returns "[]" when given None.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_to_json_string_with_empty_list(self):
        """
        Test that Base.to_json_string returns "[]" when given an empty list.
        """
        self.assertEqual(Base.to_json_string([]), "[]")
    
    def test_to_json_string_with_list_of_dict(self):
        """
        Test that Base.to_json_string returns a string when given a list
        of dictionaries, each containing an 'id' key.
        """
        lst = [{'id': 12}]
        self.assertIsInstance(Base.to_json_string(lst), str)
    
    def test_from_json_string_with_none(self):
        """
        Test that Base.from_json_string returns an empty list when given None.
        """
        self.assertEqual(Base.from_json_string(None), [])
    
    def test_from_json_string_with_empty_list(self):
        """
        Test that Base.from_json_string returns an empty list when given "[]".
        """
        self.assertEqual(Base.from_json_string("[]"), [])
    
    def test_from_json_string_with_list_of_dict(self):
        """
        Test that Base.from_json_string returns a list of dictionaries, each
        containing an 'id' key, when given a string in JSON format.
        """
        json_string = '[{ "id": 89 }]'
        lst = Base.from_json_string(json_string)
        self.assertIsInstance(lst, list)
        self.assertIsInstance(lst[0], dict)
        self.assertIn('id', lst[0])

if __name__ == '__main__':
    unittest.main()
