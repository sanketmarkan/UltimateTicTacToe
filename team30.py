import random
import copy
import time
inf = 1000000000000

class Player30:

	def move(self,board,block,old_move,flag):
		global t,de
		de = 0
		t2 = time.time()
		t = 0.000007
		if(old_move[0] == -1 and old_move[1] == -1):
                        return (4,4)
		allowed_moves = self.get_moves(board,block,old_move,flag)

		move = self.heuristic_func(board,block,allowed_moves,flag)
		print time.time() - t2
		print de
		return move


	def heuristic_func(self,board,block,allowed_moves,flag):
		return self.alpha_beta(board,block,allowed_moves,flag)
		#return allowed_moves[random.randrange(len(allowed_moves))]
	def alpha_beta(self,board,block,allowed_moves,flag):
		x,ans = self.max_value(board,block,allowed_moves,flag,-1*inf,inf,0,11.8/1.0)
		return ans

	def eval(self,board,block,flag):
		return self.winningposs(board,block,flag)

	def max_value(self,board,block,allowed_moves,flag,a,b,depth,rtime):
		t = 0.00004
		if rtime <= 2*t:
			a = 1
			if depth % 2:
				a = -1
			return a*self.eval(board,block,flag),allowed_moves[0]
		#if depth > 4:
		#	return -1*self.eval(board,block,flag),allowed_moves[0]
		v = -1*inf
		ans = allowed_moves[0]
		#print rtime/float((len(allowed_moves)))
		#if depth == 0:
		#	print allowed_moves
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			if len(next_moves) == 0:
				x = 10000*self.win(temp_block,flag)
			else:
				x,qq = self.min_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1,rtime/float(len(allowed_moves)+0.1))
			if v < x:
				v = x
				ans = move
			if v >= b:
				return v,ans
			a = max(a,v)
		return v,ans

	def min_value(self,board,block,allowed_moves,flag,a,b,depth,rtime):
		#if depth == 1:
		#	print rtime
#		global t,de
		t = 0.00004

#		de = max(de,depth)
		if rtime <= 2*t:
			a = 1
			if depth % 2:
				a = -1
			return a*self.eval(board,block,flag),allowed_moves[0]
		#if depth > 4:
		#	return -1*self.eval(board,block,flag),allowed_moves[0]
		
		v = inf
		ans = allowed_moves[0]
		#print rtime/float((len(allowed_moves)))
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			if len(next_moves) == 0:
				x = 10000*self.win(temp_block,flag)
			else:	
				x,qq = self.max_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1,rtime/float(len(allowed_moves)+0.1))
			if v > x:
				v = x
				ans = move 
			if v <= a:
				return v,ans
			b = min(b,v)
		return v,ans

	def check(self,block,flag):
		inline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		for i in range(8):
			count = 0
			for j in range(3):
				if block[inline[i][j]] == flag:
					count+=1
			if count == 3:
				return True
		return False

	def win(self,block,flag):
		a = self.check(block,flag)
		if a:
			return 1
		nflag = 'x'
		if(flag == 'x'):
			nflag = 'o'
		a = self.check(block,nflag)
		if a:
			return -1
		return 0

	def evalwp(self,board,inline,flag):
		if '-' not in board:
			return 0
		pc = 0
		oc = 0
		oflag = 'x'
		if flag == 'x':
			oflag = 'o'
		for seq in inline:
			fil_seq = [board[i] for i in seq if board[i] != '-']
			if flag in fil_seq:
				if oflag in fil_seq:
					continue
				if len(fil_seq) > 1:
					pc += 7
				if len(fil_seq) > 2:
					pc += 7
				pc += 1
			elif oflag in fil_seq:
				if len(fil_seq) > 1:
					oc += 7
				if len(fil_seq) > 2:
					oc += 7
				oc += 1
		return pc - oc

	def winningposs(self,board,block,flag):
		inline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		if self.win(block,flag):
			a = self.win(block,flag)
			cells = 0
			for i in range(9):
				r = i/3
				c = i%3
				for j in range(3):
					for k in range(3):
						if board[3*r+j][3*c+k] == '-':
							cells += 1
			return (10**6 + cells) * a

		if '-' not in block:
			return 0

		lis2 = []
		ret = 25*self.evalwp(block,inline,flag)
		for i in range(9):
			r = i/3
			c = i%3
			lis = []
			for j in range(3):
				for k in range(3):
					lis.append(board[3*r+j][3*c+k])
			temp = self.evalwp(lis,inline,flag)
			lis2.append(temp)
			ret += temp

		for i in range(8):
			prob = 0
			for j in range(3):
				prob += lis2[inline[i][j]]
			prob /= 15.0
			if prob<=-3:
				ret = ret + ( -3 - (prob+3)*(15-8)) *30
			elif prob>-3 and prob<=-2:
				ret = ret +  ( -2 - (prob+2)*(8-1) )*30
			elif prob>-2 and prob<=-1:
				ret = ret + ( - 1 - (prob+1)*(1-0))*30
			elif prob>-1 and prob<=0:
				ret = ret + (prob*(0+1))*30
			elif prob > 0 and prob <= 1:
				ret = ret +( prob*(1-0))*30
			elif prob>1 and prob<=2:
				ret = ret + (1 + (prob-1)*(1-0))*30
			elif prob> 2 and prob<=3:
				ret = ret + (2 + (prob-2)*(8-1))*30
			elif prob>3:
				ret = ret + (3 + (prob-3)*(15-8) )*30
		return ret

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
		return board2,block2

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
