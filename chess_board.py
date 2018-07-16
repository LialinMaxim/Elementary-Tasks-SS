"""
Outputs a chessboard with the given sizes of height and width.
The program is launched via the main class call with parameters.
"""


class ChessBoard:
    def __init__(self, height=8, width=8):
        self.height = self.validation(height)
        self.width = self.validation(width)
        self.black = '■'
        self.white = '⬚'

    @staticmethod
    def validation(number):
        if type(number) != int and type(number) != float:
            raise TypeError('One of the first two parameters is not a number')
        return abs(round(number))

    def __repr__(self):
        """Outputs a chessboard with the given sizes of height and width"""
        new_board = []
        for i in range(self.height):
            s = ''.join(self.black if (i + j) % 2 == 0 else self.white for j in range(self.width))
            new_board.append(s)
        new_board = '\n'.join(new_board)
        return '\n{}\n'.format(new_board)


if __name__ == '__main__':
    p = ChessBoard(3, 4)
    print(p)
