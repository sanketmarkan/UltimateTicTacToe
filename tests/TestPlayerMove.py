from team30 import Player30

self = Player30()

block = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
board = [['x', 'o', '-', '-', 'x', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', 'o', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', 'x', '-', '-'], ['-', '-', '-', 'o', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'x', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', 'o', '-', '-', '-', '-', '-']]
old_move = (8,3)
flag = 'x'
global t,de
t = 0.00001
de = 0
import time
a = time.time()
allowed_moves = self.get_moves(board,block,old_move,flag)
move = self.heuristic_func(board,block,allowed_moves,flag)
print time.time() - a 
print move
