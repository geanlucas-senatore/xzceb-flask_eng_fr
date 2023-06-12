import unittest

from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertEqual(english_to_french("this was a text in english"), "c'était un texte en anglais")

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("bon après-midi"), "Good Afternoon")
        self.assertEqual(french_to_english("c'était un texte en français"), "it was a text in French")     

unittest.main()