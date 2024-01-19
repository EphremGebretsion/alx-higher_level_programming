from models.base import Base
from unittest import TestCase


class TestBase(TestCase):
    """
    tests the base class
    """

    def test_init(self):
        b = Base(10)
        self.assertAlmostEqual(b.id, 10)
        b.id = 12
        self.assertAlmostEqual(b.id, 12)
        b = Base()
        self.assertAlmostEqual(b.id, 1)
        b = Base()
        self.assertAlmostEqual(b.id, 2)

    def test_to_json(self):
        self.assertAlmostEqual(Base.to_json_string([]), "[]")
        lis = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        res = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertAlmostEqual(Base.to_json_string([lis]), res)

    def test_from_json(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])
        lis = [{"id": "5", "name": "ephi"}, {"size": 3}]
        js = '[{"id": "5", "name": "ephi"}, {"size": 3}]'
        self.assertAlmostEqual(Base.from_json_string(js), lis)
