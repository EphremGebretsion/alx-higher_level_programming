import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO
import json


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
        my3 = Rectangle(1, 2, 3, 4, 5)
        self.assertAlmostEqual(my3.id, 5)

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

    def test_area(self):
        my = Rectangle(2, 3)
        self.assertAlmostEqual(my.area(), 6)

    def test_str(self):
        my = Rectangle(3, 5, 2, 4, 1457)
        self.assertAlmostEqual(my.__str__(), '[Rectangle] (1457) 2/4 - 3/5')

    def test_disp(self):
        my = Rectangle(2, 2)
        out = StringIO()
        sys.stdout = out
        my.display()
        sys.stdout = sys.__stdout__
        val = out.getvalue()
        out.close()
        self.assertAlmostEqual(val, "##\n##\n")

        my1 = Rectangle(2, 2, 1)
        out = StringIO()
        sys.stdout = out
        my1.display()
        sys.stdout = sys.__stdout__
        self.assertAlmostEqual(out.getvalue(), " ##\n ##\n")
        out.close()

        my2 = Rectangle(2, 2, 1, 1)
        out = StringIO()
        sys.stdout = out
        my2.display()
        sys.stdout = sys.__stdout__
        self.assertAlmostEqual(out.getvalue(), "\n ##\n ##\n")

    def test_dicionary(self):
        my = Rectangle(4, 5, 1, 3, 143)
        d = {'x': 1, 'y': 3, 'id': 143, 'height': 5, 'width': 4}
        self.assertAlmostEqual(my.to_dictionary(), d)

    def test_update(self):
        my = Rectangle(1, 2, 3, 4, 189)
        d = my.to_dictionary()
        my.update()
        self.assertAlmostEqual(d, my.to_dictionary())
        my.update(23)
        self.assertAlmostEqual(my.id, 23)
        my.update(157, 8)
        self.assertAlmostEqual(my.id, 157)
        self.assertAlmostEqual(my.width, 8)
        my.update(78, 22, 7)
        self.assertAlmostEqual(my.id, 78)
        self.assertAlmostEqual(my.width, 22)
        self.assertAlmostEqual(my.height, 7)
        my.update(89, 4, 3, 8)
        self.assertAlmostEqual(my.id, 89)
        self.assertAlmostEqual(my.width, 4)
        self.assertAlmostEqual(my.height, 3)
        self.assertAlmostEqual(my.x, 8)
        my.update(7, 33, 12, 1, 9)
        self.assertAlmostEqual(my.id, 7)
        self.assertAlmostEqual(my.width, 33)
        self.assertAlmostEqual(my.height, 12)
        self.assertAlmostEqual(my.x, 1)
        self.assertAlmostEqual(my.y, 9)

        my.update(id = 4)
        self.assertAlmostEqual(my.id, 4)
        my.update(id = 89, width = 1)
        self.assertAlmostEqual(my.id, 89)
        self.assertAlmostEqual(my.width, 1)
        my.update(id = 33, width = 3, height = 54)
        self.assertAlmostEqual(my.id, 33)
        self.assertAlmostEqual(my.width, 3)
        self.assertAlmostEqual(my.height, 54)
        my.update(id = 2, width = 11, height = 12, x = 3)
        self.assertAlmostEqual(my.id, 2)
        self.assertAlmostEqual(my.width, 11)
        self.assertAlmostEqual(my.height, 12)
        self.assertAlmostEqual(my.x, 3)
        my.update(id = 23, width = 56, height = 32, x = 7, y = 12)
        self.assertAlmostEqual(my.id, 23)
        self.assertAlmostEqual(my.width, 56)
        self.assertAlmostEqual(my.height, 32)
        self.assertAlmostEqual(my.x, 7)
        self.assertAlmostEqual(my.y, 12)

    def test_create(self):
        my = Rectangle.create(id = 34)
        d = {'x': 0, 'y': 0, 'id': 34, 'height': 1, 'width': 1}
        self.assertAlmostEqual(my.to_dictionary(), d)
        my = Rectangle.create(id = 23, width = 11)
        d = {'x': 0, 'y': 0, 'id': 23, 'height': 1, 'width': 11}
        self.assertAlmostEqual(my.to_dictionary(), d)
        my = Rectangle.create(id = 32, width = 33, height = 8)
        d = {'x': 0, 'y': 0, 'id': 32, 'height': 8, 'width': 33}
        self.assertAlmostEqual(my.to_dictionary(), d)
        my = Rectangle.create(id = 89, width = 2, height = 7, x = 5)
        d = {'x': 5, 'y': 0, 'id': 89, 'height': 7, 'width': 2}
        self.assertAlmostEqual(my.to_dictionary(), d)
        my = Rectangle.create(id = 7, width = 4, height = 3, x = 32, y = 3)
        d = {'x': 32, 'y': 3, 'id': 7, 'height': 3, 'width': 4}
        self.assertAlmostEqual(my.to_dictionary(), d)

    def test_save(self):
        Rectangle.save_to_file(None)
        lis = ''
        with open("Rectangle.json", "r") as my_file:
            lis = my_file.read()
        self.assertAlmostEqual(lis, '[]')

        Rectangle.save_to_file([])
        lis = ''
        json_lis = []
        with open("Rectangle.json", "r") as my_file:
            lis = my_file.read()
            my_file.seek(0)
            json_lis = json.load(my_file)
        self.assertAlmostEqual(lis, '[]')
        self.assertAlmostEqual(json_lis, [])

        res = [{'x': 0, 'y': 0, 'id': 17, 'height': 2, 'width': 1}]
        json_lis = []
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 17)])
        with open("Rectangle.json", "r") as my_file:
            json_lis = json.load(my_file)
        self.assertAlmostEqual(json_lis, res)

    def test_load(self):
        Rectangle.save_to_file([Rectangle(12, 23, 0, 0, 17)])
        res = {'x': 0, 'y': 0, 'id': 17, 'height': 23, 'width': 12}
        lis = Rectangle.load_from_file()
        self.assertAlmostEqual(lis[0].to_dictionary(), res)
