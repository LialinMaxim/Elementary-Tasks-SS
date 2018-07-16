import unittest
from sys import path
path.append('../')
from chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(ChessBoard.validation(1), 1)
        self.assertEqual(ChessBoard.validation(1.0), 1)
        self.assertEqual(ChessBoard.validation(-1), 1)

        self.assertRaises(TypeError, ChessBoard.validation, '1', 0)


if __name__ == '__main__':
    unittest.main()
