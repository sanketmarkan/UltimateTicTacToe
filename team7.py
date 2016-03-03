''' put everything in the class player7
first we find out which cells are valid '''
''' The next step is to make the update function which will update
    the block state given an old move as we will surely require it
    while traversing it on the minimax tree'''

import random
import time
import sys
import copy

class Player7:

	def __init__(self):
		''' Variables Declared Here '''
		pass


	def get_block_list(self,old_move):
	    if old_move[0] == -1 and old_move[1] == -1 :
             # First Move therefore return all blocks
	     return range(9)
	    if old_move[0]%3 == 0 and old_move[1]%3 == 0 :
             # Top Left cell of block
             return [1,3]
            if old_move[0]%3 == 0 and old_move[1]%3 == 1 :
             # Top Middle cell of block
             return [0,2]
            if old_move[0]%3 == 0 and old_move[1]%3 == 2 :
             # Top Right cell of block
             return [1,5]
            if old_move[0]%3 == 1 and old_move[1]%3 == 0 :
             # Center Left cell of block
             return [0,6]
            if old_move[0]%3 == 1 and old_move[1]%3 == 1 :
             # Center Middle cell of block
             return [4]
            if old_move[0]%3 == 1 and old_move[1]%3 == 2 :
             # Center Right cell of block
             return [2,8]
            if old_move[0]%3 == 2 and old_move[1]%3 == 0 :
             # Bottom Left cell of block
             return [3,7]
            if old_move[0]%3 == 2 and old_move[1]%3 == 1 :
             # Bottom Middle cell of any block
             return [6,8]
            if old_move[0]%3 == 2 and old_move[1]%3 == 2 :
             # Bottom Right cell of any block
             return [5,7]

	def get_cell_list(self,allowed_block_list, board, block):

	    cell_list = []
            for i in range(len(allowed_block_list)) :
                if block[allowed_block_list[i]] != '-' : # the block is already won so we cannot move in that block
                    continue

                add_j = allowed_block_list[i]/3  # value to be added to first numbers from pairs  0,0 to 2,2 to get to block list
                add_k = allowed_block_list[i]%3  # value to be added to second numbers from pairs  0,0 to 2,2 to get to block list
                for j in range(3):
                 for k in range(3):
                        j_temp = j+add_j*3
                        k_temp = k+add_k*3    # j and k will give all elements of a given block

                        if(board[j_temp][k_temp]=='-') :  # if the cell is empty
                         cell_list.append( (j_temp,k_temp) )

            if len(cell_list) == 0 : #we have a free move

                 for j in range(9) :
                    for k in range(9) :
                        if board[j][k] == '-' and block[(j/3)*3+k/3] == '-' :  # If the cell is empty
                            cell_list.append((j,k))
            return cell_list


        def get_block_number(self,old_move):  # returns the block number of a cell  tested and works fine
            return ((old_move[0]/3)*3+old_move[1]/3)


        def get_cell_list_from_block(self,block_number):  #retruns the 9 cells within a block tested and works fine
            cell_list = []
            add_j = block_number/3  # value to be added to first numbers from pairs  0,0 to 2,2 to get to block list
            add_k = block_number%3  # value to be added to second numbers from pairs  0,0 to 2,2 to get to block list
            for j in range(3):
                for k in range(3):
                    j_temp = j+add_j*3
                    k_temp = k+add_k*3    # j and k will give all elements of a given block
                    cell_list.append([j_temp,k_temp])
            return cell_list

        def update_block_list(self,old_move,temp_board,temp_block):
            if old_move[0]==-1 and old_move[1]==-1:
                return temp_block
            block_number = self.get_block_number(old_move)
            cell_list = self.get_cell_list_from_block(block_number) # Get All cells in the block where last move was played
            block = copy.deepcopy(temp_block)
            board = copy.deepcopy(temp_board)
            for i in range(8):
                cell1 = three_in_a_row[i][0]
                cell2 = three_in_a_row[i][1]
                cell3 = three_in_a_row[i][2]
                if board[cell_list[cell1][0]][cell_list[cell1][1]] == board[cell_list[cell2][0]][cell_list[cell2][1]] ==  board[cell_list[cell3][0]][cell_list[cell3][1]] == 'x' :
                    if block[block_number]=='-':
                        block[block_number] = 'x'

                if board[cell_list[cell1][0]][cell_list[cell1][1]] == board[cell_list[cell2][0]][cell_list[cell2][1]] ==  board[cell_list[cell3][0]][cell_list[cell3][1]] == 'o' :
                    if block[block_number]=='-':
                        block[block_number] = 'o'

            draw_flag = 0
            for i in range(9):
                if board[cell_list[i][0]][cell_list[i][1]] == '-': # at least one is empty
                    draw_flag = 1
            if draw_flag ==0: # no empty cell in block
                block[block_number] = 'D'
            return block


        def utility_func(self,temp_board,flag,block) :
            board = copy.deepcopy(temp_board)
            if flag == 'x':
                opponent = 'o'
            else :
                opponent = 'x'
            heuristic = [[0,-1,-10,-1000],[1,0,0,0],[10,0,0,0],[1000,0,0,0]]
            list_block = []
            for i in range(9):
                temp_score = 0
                elements = self.get_cell_list_from_block(i)
                #print elements[0]
                #print 'xx'
                for j in range(8):
                    my_piece = 0
                    opponent_piece = 0
                    for k in range(3):
                        piece = board[elements[three_in_a_row[j][k]][0]][elements[three_in_a_row[j][k]][1]]
                        if piece == flag :
                            my_piece = my_piece + 1
                        elif piece == opponent :
                            opponent_piece = opponent_piece + 1
                    temp_score += heuristic[my_piece][opponent_piece]
                list_block.append(float(temp_score)/float(1000)) # max score is 130

            maxi = -1*float("inf")
            mini = float("inf")
            ret = 0
            for i in range(8):
#                maxi = max(maxi,list_block[three_in_a_row[i][0]]+list_block[three_in_a_row[i][1]]+list_block[three_in_a_row[i][2]])
#                mini = min(mini,list_block[three_in_a_row[i][0]]+list_block[three_in_a_row[i][1]]+list_block[three_in_a_row[i][2]])
#                ret  = ret + ( list_block[three_in_a_row[i][0]]+list_block[three_in_a_row[i][1]]+list_block[three_in_a_row[i][2]])*2000
                prob = list_block[three_in_a_row[i][0]]+list_block[three_in_a_row[i][1]]+list_block[three_in_a_row[i][2]]
                if prob<=-3:
                    ret = ret + ( -3 + (prob+3)*(1000-10)) *2000
                elif prob>-3 and prob<=-2:
                    ret = ret +  ( -2 + (prob+2)*(10-1) )*2000
                elif prob>-2 and prob<=-1:
                    ret = ret + ( - 1 + (prob+1)*(1-0))*2000
                elif prob>-1 and prob<=0:
                    ret = ret + (prob*(0+1))*2000
                elif prob > 0 and prob <= 1:
                    ret = ret +( prob*(1-0))*2000
                elif prob>1 and prob<=2:
                    ret = ret + (1 + (prob-1)*(1-0))*2000
                elif prob> 2 and prob<=3:
                    ret = ret + (2 + (prob-2)*(10-1))*2000
                elif prob>3:
                    ret = ret + (3 + (prob-3)*(1000-10) )*2000
            return ret



        def print_list(self,li):
            for i in range(len(li)):
                for j in range(len(li[i])):
                    print str(li[i][j]) + ' ',
                print


        def check_terminal_state(self,board):
            for i in range(len(three_in_a_row)):
                if board[three_in_a_row[i][0]] == board[three_in_a_row[i][1]] == board[three_in_a_row[i][2]] == 'x':
                    return 'x'

                if board[three_in_a_row[i][0]] == board[three_in_a_row[i][1]] == board[three_in_a_row[i][2]] == 'o':
                    return 'o'

            return '-'
        def tree_func(self,max_or_min , height , alpha , beta , temp_board , temp_block , old_move, flag,time_left):
            board = copy.deepcopy(temp_board) # initializing the board
            block = copy.deepcopy(temp_block) # initializing the block
            if flag == 'x':
                nflag = 'o'
            if flag == 'o' :
                nflag = 'x'


            if max_or_min == 0 :  # it is a min node and so our opponent
                value = float("inf")
            else : # it is a max node so it is us
                value = -1*float("inf")


            block = self.update_block_list(old_move,board,block) # here the function added by motwani will be used
            allowed_block_list = self.get_block_list(old_move)

            allowed_cell_list = self.get_cell_list(allowed_block_list,board,block) # getting the cell list for the next move
            random.shuffle(allowed_cell_list)
            winner = self.check_terminal_state(board)
            if winner == flag :
                return float("inf")
            elif winner == nflag :
                return -1*float("inf")
            if time_left <= 0.000400 or len(allowed_cell_list) ==0 or height >=8:
                raju = self.utility_func(board,flag,block)
                return raju
#            if   height == 4: # if height is 4 we return the utility
#                raju = self.utility_func(board,flag,block)
#                return raju

            for i in range(len(allowed_cell_list)) :

                if max_or_min == 0 :  # minimizer, so updating the best move correspondingly
                        board[allowed_cell_list[i][0]][allowed_cell_list[i][1]] = nflag
                        value = min(value,self.tree_func(1,height+1,alpha,beta,board ,block,allowed_cell_list[i],flag,time_left/float(len(allowed_cell_list)+2)))
                        board[allowed_cell_list[i][0]][allowed_cell_list[i][1]]='-'


                else : # maximizer , so updating the best move accordingly
                        board[allowed_cell_list[i][0]][allowed_cell_list[i][1]] = flag
                        value = max(value,self.tree_func(0,height+1,alpha,beta,board ,block,allowed_cell_list[i],flag,time_left/float(len(allowed_cell_list)+2)))
                        board[allowed_cell_list[i][0]][allowed_cell_list[i][1]]='-'

                if max_or_min == 0 : # a minimizer node and value < aplha no need to check children further
                    if value < alpha :
                        return value
                else :
                    if value > beta :
                        return value

                if max_or_min == 0 : # a minimizer node , so updating the value of beta
                    beta = min(beta,value)
                else : # maximizer so upating the value of aplha
                    alpha = max(alpha ,value)

            return value

	def move(self,temp_board,temp_block,old_move,flag):
                global t
                t= time.time()
                global three_in_a_row
                three_in_a_row = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
                board = copy.deepcopy(temp_board)
                block = copy.deepcopy(temp_block)
                allowed_block_list = self.get_block_list(old_move)
    	        allowed_cell_list = self.get_cell_list(allowed_block_list,board,block)

                if old_move[0]==-1 and old_move[1]==-1:
                    return (4,4)
                best_move = allowed_cell_list[random.randrange(len(allowed_cell_list))]
                value = -1*float("inf")     # initial value for the root node
                alpha = -1*float("inf")  # initial alpha value for the root node
                beta = float("inf")      # initial beta value for the root node
                for i in range(len(allowed_cell_list)):
                    if time.time() - t > 11.5 :
                        old_stdout = sys.stdout
                        log_file = open("message.log","a")
                        sys.stdout = log_file
                        print "Returned due to lack of time, Best Move is",best_move[0],best_move[1]
                        sys.stdout = old_stdout
                        log_file.close()
                        return (best_move[0],best_move[1])

                    board[allowed_cell_list[i][0]][allowed_cell_list[i][1]] = flag
                    temp_value = self.tree_func(0,1,alpha,beta,board,block,allowed_cell_list[i],flag,11.5/float(len(allowed_cell_list)+1))
                    board[allowed_cell_list[i][0]][allowed_cell_list[i][1]] = '-'

                    if time.time() - t > 11.5 :
                        old_stdout = sys.stdout
                        log_file = open("message.log","a")
                        sys.stdout = log_file
                        print "Returned due to lack of time, Best Move is",best_move[0],best_move[1]
                        sys.stdout = old_stdout
                        log_file.close()
                        return (best_move[0],best_move[1])
                    if temp_value > value : # next child having better value , so update the best move
                        value = temp_value
                        best_move = allowed_cell_list[i]

                    alpha = max(alpha,value) # updating value of alpha

                    if value > beta:  # no need to check further children
                        return (best_move[0],best_move[1])
                return (best_move[0],best_move[1])


if __name__ == '__main__':  # add test cases here

    '''old_move = [-1 , -1]
    flag = 'x'
    board = []
    block = []
    temp_l = []

    for i in range(9) :
        temp_list = []
        for j in range(9) :
            temp_list.append('-')
        board.append(temp_list)

    board[3][3]='o'
    old_move = [3 , 3]

    for i in range(9) :
        block.append('-')
	p = player7()
	temp_l = p.move(board,block,old_move,flag)

    print temp_l '''
    p = Player7()
