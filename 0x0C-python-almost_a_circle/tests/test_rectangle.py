import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_Rect(self):
        my = Rectangle(5, 8)
        self.assertAlmostEqual(my.width, 5)
        self.assertAlmostEqual(my.height, 8)
        my1 = Rectangle(12, 3, 8)
        self.assertAlmostEqual(my1.x, 8)
        self.assertAlmostEqual(my1.y, 0)
        my2 = Rectangle(1, 2, 3, 4)
        self.assertAlmostEqual(my2.width, 1)
        self.assertAlmostEqual(my2.height, 2)
        self.assertAlmostEqual(my2.x, 3)
        self.assertAlmostEqual(my2.y, 4)

    def test_recEr(self):
        with self.assertRaises(TypeError):
            my = Rectangle("12", 3)

        with self.assertRaises(TypeError):
            my = Rectangle(2, "7")

        with self.assertRaises(TypeError):
            my = Rectangle(1, 2, "3", 3)

        with self.assertRaises(TypeError):
            my = Rectangle(13, 32, 4, "2")

    def test_valEr(self):
        with self.assertRaises(ValueError):
            my = Rectangle(-3, 6)
        with self.assertRaises(ValueError):
            my = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            my = Rectangle(2, -3)
        with self.assertRaises(ValueError):
            my = Rectangle(8, 0)
        with self.assertRaises(ValueError):
            my = Rectangle(1, 2, -2, 8)
        with self.assertRaises(ValueError):
            my = Rectangle(3, 8, 2, -4)
