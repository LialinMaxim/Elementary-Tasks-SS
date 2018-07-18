from unittest import TestCase, main
from sys import path
path.append('../')

from file_parser import file_parser


class TestFileParser(TestCase):
    def test_file_parser(self):
        f = 'static/test.txt'
        self.assertEqual(file_parser(f, 'F'), 55)


if __name__ == '__main__':
    main()
