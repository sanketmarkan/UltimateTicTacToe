
	def eval2(self,temp_board,inline,flag):
		oflag = 'x'
		val = 0
		if flag == 'x':
			oflag = 'o'
		for i in range(8):
			c1 = 0
			c2 = 0
			for j in range(3):
				if temp_board[inline[i][j]] == flag:
					c1+=1
				elif temp_board[inline[i][j]] == oflag:
					c2+=1
			#some values are here
			if c2 ==3 and c1 == 0:
				val += 100
			elif c1 == 2 and c2 == 0:
				val += 10
			elif c1 == 1 and c2 == 0:
				val += 1
			elif c1 == 3 and c2 == 0:
				val += 100
			elif c1 == 0 and c2 == 2:
				val -= 10
			elif c1 == 0 and c2 == 1:
				val -= 1
		#	print val,
		#print temp_board
		return val


	def eval(self,board,block,flag):
		inline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		val = []
		for k in range(9):
			r = k/3
			c = k%3
			#print r,c
			temp_board = []
			for i in range(3):
				for j in range(3):
					#print i+3*r,j+3*c,"            ",
					temp_board.append(board[i+3*r][j+3*c])
				#print
			val.append(self.eval2(temp_board,inline,flag))
		####print val
		maa = -1*inf
		mia = inf
		for i in range(8):
			value = 0
			for j in range(3):
				value += val[inline[i][j]]
			maa = max(maa,value)
			mia = min(mia,value)

		#print maa,mia
		return maa+mia+self.eval2(block,inline,flag)
