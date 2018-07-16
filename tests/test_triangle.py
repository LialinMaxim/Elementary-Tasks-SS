from unittest import TestCase, main
from sys import path

path.append('../')

from triangles import Triangle


class TestTriangle(TestCase):

    def test_triangle_area(self):
        options = [
            [(1, 2, 3), None],
            [(1, 2, 30), None],
            [(2, 2, 2), 1.0],
            [(2.0, 2.0, 2.0), 1.0],
            [(100, 100, 100), 353.5534],
        ]
        for sides, result in options:
            self.assertEqual(Triangle.triangle_area(sides), result)


if __name__ == '__main__':
    main()
