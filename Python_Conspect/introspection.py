from inspect import getsource, isfunction, ismethod


class Board:
    """Это класс для доски крестиков-ноликов."""

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


game = Board()
print(type(game))

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

print(isinstance(game, Board))
print(isinstance(game, str))

print(game.__class__)

print(dir(game))

print('__str__' in dir(game))
print(hasattr(game, '__str__'))

print('------------------')
print(game.__class__.__dict__)

print(getsource(Board))

print(isfunction(game.display))
print(ismethod(game.display))

print(game.__doc__) 
print(print.__doc__)