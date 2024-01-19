import unittest
from models.square import Square
import os
from io import StringIO
import json


class TestSquare(unittest.TestCase):
    def test_init(self):
        my = Square(12)
        self.assertAlmostEqual(my.width, 12)
        self.assertAlmostEqual(my.height, 12)
        my = Square(7, 2)
        self.assertAlmostEqual(my.width, 7)
        self.assertAlmostEqual(my.height, 7)
        self.assertAlmostEqual(my.x, 2)
        my = Square(1, 2, 3)
        self.assertAlmostEqual(my.width, 1)
        self.assertAlmostEqual(my.height, 1)
        self.assertAlmostEqual(my.x, 2)
        self.assertAlmostEqual(my.y, 3)

        my = Square(1, 2, 3, 534)
        self.assertAlmostEqual(my.width, 1)
        self.assertAlmostEqual(my.height, 1)
        self.assertAlmostEqual(my.x, 2)
        self.assertAlmostEqual(my.y, 3)
        self.assertAlmostEqual(my.id, 534)

    def test_Err(self):
        with self.assertRaises(TypeError):
            Square("54")
        with self.assertRaises(TypeError):
            Square(23, "32")
        with self.assertRaises(TypeError):
            Square(3, 2, "4")

    def test_val(self):
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(2, -5)
        with self.assertRaises(ValueError):
            Square(4, 3, -4)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(23, 0, 0, 30)
        self.assertEqual(s.__str__(), '[Square] (30) 0/0 - 23')

    def test_dictionary(self):
        s = Square(2, 3, 1, 78)
        d = {'id': 78, 'x': 3, 'size': 2, 'y': 1}
        self.assertAlmostEqual(s.to_dictionary(), d)

    def test_update(self):
        s = Square(2, 3, 1, 78)
        d = {'id': 78, 'x': 3, 'size': 2, 'y': 1}
        s.update()
        self.assertAlmostEqual(s.to_dictionary(), d)
        s.update(8)
        self.assertAlmostEqual(s.id, 8)
        s.update(80, 23)
        self.assertAlmostEqual(s.id, 80)
        self.assertAlmostEqual(s.size, 23)
        s.update(2, 3, 1)
        self.assertAlmostEqual(s.id, 2)
        self.assertAlmostEqual(s.size, 3)
        self.assertAlmostEqual(s.x, 1)
        s.update(23, 2, 3, 6)
        self.assertAlmostEqual(s.id, 23)
        self.assertAlmostEqual(s.size, 2)
        self.assertAlmostEqual(s.x, 3)
        self.assertAlmostEqual(s.y, 6)

        s.update(id=78)
        self.assertAlmostEqual(s.id, 78)
        s.update(id=3, size=2)
        self.assertAlmostEqual(s.id, 3)
        self.assertAlmostEqual(s.size, 2)
        s.update(id=65, size=3, x=2)
        self.assertAlmostEqual(s.id, 65)
        self.assertAlmostEqual(s.size, 3)
        self.assertAlmostEqual(s.x, 2)
        s.update(id=88, size=2, x=1, y=5)
        self.assertAlmostEqual(s.id, 88)
        self.assertAlmostEqual(s.size, 2)
        self.assertAlmostEqual(s.x, 1)
        self.assertAlmostEqual(s.y, 5)

    def test_create(self):
        s = Square.create(id=2)
        self.assertAlmostEqual(s.id, 2)
        s = Square.create(id=22, size=2)
        self.assertAlmostEqual(s.id, 22)
        self.assertAlmostEqual(s.size, 2)
        s = Square.create(id=88, size=35, x=3)
        self.assertAlmostEqual(s.id, 88)
        self.assertAlmostEqual(s.size, 35)
        self.assertAlmostEqual(s.x, 3)
        s = Square.create(id=21, size=6, x=11, y=3)
        self.assertAlmostEqual(s.id, 21)
        self.assertAlmostEqual(s.size, 6)
        self.assertAlmostEqual(s.x, 11)
        self.assertAlmostEqual(s.y, 3)

    def test_save(self):
        Square.save_to_file(None)
        lis = []
        with open("Square.json", "r") as my_file:
            lis = json.load(my_file)
        self.assertAlmostEqual(lis, [])
        Square.save_to_file([])
        lis = []
        with open("Square.json", "r") as my_file:
            lis = json.load(my_file)
        self.assertAlmostEqual(lis, [])
        Square.save_to_file([Square(23, 0, 0, 31)])
        lis = []
        with open("Square.json", "r") as my_file:
            lis = json.load(my_file)
        self.assertEqual(lis, [{'id': 31, 'x': 0, 'size': 23, 'y': 0}])

    def test_load(self):
        Square.save_to_file([Square(23, 0, 0, 12)])
        lis = Square.load_from_file()
        res = lis[0].to_dictionary()
        self.assertEqual(res, {'id': 12, 'x': 0, 'size': 23, 'y': 0})
        os.system("rm Square.json")
        lis = Square.load_from_file()
        self.assertAlmostEqual(lis, [])
