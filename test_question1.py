import question1
import unittest

class TestCase(unittest.TestCase):
    def test_reverse_1(self):
        self.assertEqual(question1.word_reverse("My name is V Tadimeti"), "Tadimeti V is name My")

    def test_reverse_2(self):
        self.assertEqual(question1.word_reverse("Hello World"), "World Hello")

if __name__ == "__main__":
    unittest.main(verbosity=2)