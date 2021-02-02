#import
import unittest
from question_10 import *

class Test_get_sequence(unittest.TestCase):

    def test_0(self):
        self.assertEqual(get_sequence(0), [])
    
    def test_less_0(self):
        "test with numbers less than 0"
        self.assertEqual(get_sequence(-10), [])
    
    def test_with_greather_0(self):
        "test with number > 0"
        self.assertEqual(get_sequence(4), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    
    def test_not_equal(self):
        "test with number not equal the expected"
        self.assertNotEqual(get_sequence(4), [1, 2, 3, 4])

    def test_Type_error(self):
        #passing other element that str
        values = [True, "dirac", 1.5, {"d" : "2"}, ["abc", "def"], None]
        for element in values:
            self.assertRaises(TypeError, get_sequence, element)