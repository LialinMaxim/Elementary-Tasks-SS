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
            s = ''  # new current line of board
            for j in range(self.width):
                if (i + j) % 2 == 0:
                    s += self.black
                else:
                    s += self.white
            new_board.append(s)
        return '\n' + '\n'.join(new_board) + '\n'

