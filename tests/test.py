from team30 import Player30

board = [['-', '-', 'o', 'x', '-', 'o', 'x', 'x', 'o'], ['-', '-', 'o', '-', 'o', '-', 'x', 'x', 'o'], ['-', '-', 'o', 'o', '-', '-', 'x', 'o', '-'], ['x', '-', '-', 'o', 'x', 'x', 'x', 'x', 'x'], ['o', 'o', 'o', '-', 'x', '-', '-', '-', 'o'], ['-', '-', '-', 'o', 'o', 'o', '-', '-', '-'], ['x', 'x', 'x', 'x', 'x', 'o', 'o', '-', '-'], ['-', '-', '-', '-', '-', 'x', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-']]
block = ['o', 'o', 'x', 'o', 'o', 'x', 'x', '-', '-']


v = Player30()

print v.eval(board,block,'x')