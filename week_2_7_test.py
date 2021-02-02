#import
from week_2_7 import *
import unittest

class Test_count_letters(unittest.TestCase):
    #test the method count letters
    def test_with_empty(self):
        #pass en empty string
        self.assertEqual(count_letters(""), {})
    
    def test_with_non_empty(self):
        #pass a string
        ex_dic = {"d": 1, "i": 1, "r": 1, "a":1, "c":1}
        self.assertDictEqual(count_letters("dirac"), ex_dic)
    
    def test_type_error(self):
        #passing other element that str
        values = [True, 1, 1.5, {"d" : "2"}, ["abc", "def"], None]
        for element in values:
            self.assertRaises(TypeError, count_letters, element)