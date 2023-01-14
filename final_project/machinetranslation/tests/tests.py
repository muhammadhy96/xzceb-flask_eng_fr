import unittest
from ibm_watson import ApiException

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertNotEqual(english_to_french("Hello"), "Bonsoir")

    def test3(self):
        self.assertRaises(ApiException, english_to_french,"")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Hi")

    def test3(self):
        self.assertRaises(ApiException, french_to_english, "")

if __name__ == '__main__':
    unittest.main()