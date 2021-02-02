#import
from question_6 import *
import unittest


class TestRemoveSpace(unittest.TestCase):
    def test_normal_string(self):
        #test the function when the string is printed without extra spaces
        s1 = "Bonjour dirac haha"
        self.assertEqual(remove_space2(s1), "Bonjour dirac haha")
    
    def test_remove_spaces(self):
        #test with spaces
        s1 = "Bonjour dirac haha"
        #test with multiple space at the beginning
        s2 = "Bonjour          dirac        haha"
        self.assertEqual(remove_space2(s2), s1)
    
    def test_remove_space_s(self):
        #test with multiple space in the middle
        s1 = "Bonjour dirac haha"
        s3 = "        Bonjour               dirac         haha"
        self.assertEqual(remove_space2(s3), s1)

    def test_remove_space_s_end(self):
        #test with multiple space everywhere
        s1 = "Bonjour dirac haha"
        s4 = "       Bonjour         dirac   haha        "
        self.assertEqual(remove_space2(s4), s1)

    def test_remove_space_end(self):
        #test for multiple space onle at the end
        s5 = "Bonjourdirachaha                "
        s6 = "Bonjourdirachaha"
        self.assertEqual(remove_space2(s5), s6)
    
    def test_type_error(self):
        #test if the function raised a value error
        values = [True, 1, 1.5, {"d" : "2"}, ["abc", "def"], None]
        for element in values:
            self.assertRaises(TypeError, remove_space2, element)

