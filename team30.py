import random
import copy
inf = 1000000000000

class Player30:
	def move(self,board,block,old_move,flag):
		if(old_move[0] == -1 and old_move[1] == -1):
                        return (4,4)
		allowed_moves = self.get_moves(board,block,old_move,flag)

		move = self.heuristic_func(board,block,allowed_moves,flag)
		#print move
		#heuristic function here
		return move


	def heuristic_func(self,board,block,allowed_moves,flag):
		return self.alpha_beta(board,block,allowed_moves,flag)
		#return allowed_moves[random.randrange(len(allowed_moves))]
	def alpha_beta(self,board,block,allowed_moves,flag):
		x,ans = self.max_value(board,block,allowed_moves,flag,-1*inf,inf,0)
		return ans

	def max_value(self,board,block,allowed_moves,flag,a,b,depth):
		if depth>5:
			return random.randrange(1,50),allowed_moves[0]
		if self.win(block,flag):
			return self.win(block,flag)

		v = -1*inf
		ans = allowed_moves[0]
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			x,qq = self.min_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1)
			if v < x:
				v = x
				ans = move
			if v >= b:
				return v,ans
			a = max(a,v)
		return v,ans

	def min_value(self,board,block,allowed_moves,flag,a,b,depth):
		if depth>5:
			return random.randrange(1,50),allowed_moves[0]
		if self.win(block,flag):
			return self.win(block,flag)

		v = inf
		ans = allowed_moves[0]
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			x,qq = self.max_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1)
			if v > x:
				v = x
				ans = move 
			if v <= a:
				return v,ans
			b = min(b,v)
		return v,ans

	def win(self,block,flag):
		sblock = []
		new = []
		for i in range(3):
			for j in range(3):
				new.append(block[3*i+j])
			sblock.append(new)
			new = []

		a = self.check(sblock,flag)
		if a:
			return 1
		nflag = 'x'
		if(flag == 'x'):
			nflag = 'o'
		a = self.check(sblock,nflag)
		if a:
			return -1
		return 0
			

	def print_lists(self,gb, bs):
		print '=========== Game Board ==========='
		for i in range(9):
			if i > 0 and i % 3 == 0:
				print
			for j in range(9):
				if j > 0 and j % 3 == 0:
					print " " + gb[i][j],
				else:
					print gb[i][j],

			print
		print "=================================="

		print "=========== Block Status ========="
		for i in range(0, 9, 3):
			print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
		print "=================================="
		print
	
	def apply_move(self,board,block,move,flag):
		block2 = copy.deepcopy(block)
		board2 = copy.deepcopy(board)
		board2[move[0]][move[1]] = flag
		block2 = self.update_block(board2,block2,move,flag)
		return board2,block

	def update_block(self,board,block,move,flag):
		block_r = move[0]/3
		block_c = move[1]/3

		#horizontal direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			if(j>block_r*3+2 or j<block_r*3 ):
				continue
			elif(board[j][move[1]] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#vertical direction
		count = 0
		for i in range(5):
			j = move[1]+i-2
			if(j>block_c*3+2 or j<block_c*3 ):
				continue
			elif(board[move[0]][j] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#diagonal-left direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			k = move[1]+i-2
			if(j>block_r*3+2 or j<block_r*3 or k>block_c*3+2 or k<block_c*3 ):
				continue
			elif(board[j][k] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#diagonal-right direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			k = move[1]+2-i
			if(j>block_r*3+2 or j<block_r*3 or k>block_c*3+2 or k<block_c*3 ):
				continue
			elif(board[j][k] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
		
		return block


	def get_moves(self,board,block,old_move,flag):

		blocks_allowed = []
		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			blocks_allowed = [1,3]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
			blocks_allowed = [1,5]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
			blocks_allowed = [3,7]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
			blocks_allowed = [5,7]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
			blocks_allowed = [0,2]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
			blocks_allowed = [0,6]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
			blocks_allowed = [6,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
			blocks_allowed = [2,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
			blocks_allowed = [4]
		else:
			sys.exit(1)

		#print old_move
		#print blocks_allowed


		for i in blocks_allowed:
			if block[i] != '-':
				blocks_allowed.remove(i)

		for i in blocks_allowed:
			if block[i] != '-':
				blocks_allowed.remove(i)
		
		#print blocks_allowed
		
		if blocks_allowed == []:
			for i in range(len(block)):
				if block[i] == '-':
					blocks_allowed.append(i)
		
		return self.get_empty(board,block,blocks_allowed)

	def get_empty(self,board,block,blocks_allowed):

		cells = []
		for i in range(len(blocks_allowed)):
			r = blocks_allowed[i]/3
			c = blocks_allowed[i]%3
			for j in range(r*3,r*3+3):
				for k in range(c*3,c*3+3):
					if board[j][k] == '-':
						cells.append((j,k))


		if cells == []:
			for i in range(len(block)):
				if block[i] == '-':
					blocks_allowed.append(i)

			for i in range(len(blocks_allowed)):
				r = blocks_allowed[i]/3
				c = blocks_allowed[i]%3
				for j in range(r*3,r*3+3):
					for k in range(c*3,c*3+3):
						if board[j][k] == '-':
							cells.append((j,k))
		return cells