def initilaize():
    board=[
    ['wR','wN','wB','wK','wQ','wB','wN','wR'],
    ['wP','wP','wP','wP','wP','wP','wP','wP'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['bP','bP','bP','bP','bP','bP','bP','bP'],
    ['bR','bN','bB','bK','bQ','bB','bN','bR'],]
    return board

def rook_move(board,from_r,from_c,move_list,enemy_color):
    (f1,f2,f3,f4)=(False,False,False,False)
    for i in range(1,8):
        #rook done
        if from_r < 8 and from_c+int(i) < 8 and f1==False:
	        if board[from_r][from_c+int(i)] == '.':
		        move_list.append(str(from_r)+str(from_c+int(i)))
	        elif board[from_r][from_c+int(i)][0] == enemy_color:
		        move_list.append(str(from_r)+str(from_c+int(i)))
		        f1=True
	        elif board[from_r][from_c+int(i)][0] != enemy_color:
		        f1=True

        if from_r +int(i)< 8 and from_c < 8 and f2==False:
            if board[from_r+int(i)][from_c] == '.':
                move_list.append(str(from_r+int(i))+str(from_c))
            elif board[from_r+int(i)][from_c][0] == enemy_color:
                move_list.append(str(from_r+int(i))+str(from_c))
                f2=True
            elif board[from_r+int(i)][from_c][0] != enemy_color:
                f2=True

        if from_r -int(i)< 8 and from_c < 8 and f3==False:
            if board[from_r-int(i)][from_c] == '.':
                move_list.append(str(from_r-int(i))+str(from_c))
            elif board[from_r-int(i)][from_c][0] == enemy_color:
                move_list.append(str(from_r-int(i))+str(from_c))
                f3=True
            elif board[from_r-int(i)][from_c][0] != enemy_color:
                f3=True

        if from_r < 8 and from_c-int(i) < 8 and f4==False:
	        if board[from_r][from_c-int(i)] == '.':
		        move_list.append(str(from_r)+str(from_c-int(i)))
	        elif board[from_r][from_c-int(i)][0] == enemy_color:
		        move_list.append(str(from_r)+str(from_c-int(i)))
		        f4=True
	        elif board[from_r][from_c-int(i)][0] != enemy_color:
		        f4=True
    return move_list

def bishop_move(board,from_r,from_c,move_list,enemy_color):
    #bishop done
    (f8,f7,f5,f6)=(False,False,False,False)
    for i in range(1,8):
        if from_r +int(i)< 8 and from_c+int(i) < 8 and f5==False:
            if board[from_r+int(i)][from_c+int(i)] == '.':
                move_list.append(str(from_r+int(i))+str(from_c+int(i)))
            elif board[from_r+int(i)][from_c+int(i)][0] == enemy_color:
                move_list.append(str(from_r+int(i))+str(from_c+int(i)))
                f5=True
            elif board[from_r+int(i)][from_c+int(i)][0] != enemy_color:
                f5=True

        if from_r -int(i)< 8 and from_c-int(i) < 8 and f6==False:
            if board[from_r-int(i)][from_c-int(i)] == '.':
                move_list.append(str(from_r-int(i))+str(from_c-int(i)))
            elif board[from_r-int(i)][from_c-int(i)][0] == enemy_color:
                move_list.append(str(from_r-int(i))+str(from_c-int(i)))
                f6=True
            elif board[from_r-int(i)][from_c-int(i)][0] != enemy_color:
                f6=True

        if from_r +int(i)< 8 and from_c-int(i) < 8 and f7==False:
            if board[from_r+int(i)][from_c-int(i)] == '.':
                move_list.append(str(from_r+int(i))+str(from_c-int(i)))
            elif board[from_r+int(i)][from_c-int(i)][0] == enemy_color:
                move_list.append(str(from_r+int(i))+str(from_c-int(i)))
                f7=True
            elif board[from_r+int(i)][from_c-int(i)][0] != enemy_color:
                f7=True

        if from_r -int(i)< 8 and from_c+int(i) < 8 and f8==False:
            if board[from_r-int(i)][from_c+int(i)] == '.':
                move_list.append(str(from_r-int(i))+str(from_c+int(i)))
            elif board[from_r-int(i)][from_c+int(i)][0] == enemy_color:
                move_list.append(str(from_r-int(i))+str(from_c+int(i)))
                f8=True
            elif board[from_r-int(i)][from_c+int(i)][0] != enemy_color:
                f8=True
    return move_list

def knight_move(board,from_r,from_c,move_list,enemy_color):
    #1
    if  (from_r+2 <= 7 and from_c-1 >= 0):
        if (board[from_r+2][from_c-1] == '.' ):
            move_list.append(str(from_r+2)+str(from_c-1))
        elif enemy_color in board[from_r+2][from_c-1]:
            move_list.append(str(from_r+2)+str(from_c-1))
    #2
    if (from_r+2 <= 7 and from_c+1 <= 7):
        if (board[from_r+2][from_c+1]  == '.' ):
            move_list.append(str(from_r+2)+str(from_c+1))
        elif enemy_color in board[from_r+2][from_c+1]:
            move_list.append(str(from_r+2)+str(from_c+1))
    #3
    if  (from_r-2 >= 0 and from_c-1 >= 0):
        if (board[from_r-2][from_c-1] == '.'):
            move_list.append(str(from_r-2)+str(from_c-1))
        elif enemy_color in board[from_r-2][from_c-1]:
            move_list.append(str(from_r-2)+str(from_c-1))
    #4
    if (from_r-2 >= 0 and from_c+1 <=7):
        if (board[from_r-2][from_c+1] == '.'):
            move_list.append(str(from_r-2)+str(from_c+1))
        elif enemy_color in board[from_r-2][from_c+1]:
            move_list.append(str(from_r-2)+str(from_c+1))
    #5
    if (from_r-1 >= 0 and from_c-2 >= 0):
        if (board[from_r-1][from_c-2] == '.'):
            move_list.append(str(from_r-1)+str(from_c-2))
        elif enemy_color in board[from_r-1][from_c-2]:
            move_list.append(str(from_r-1)+str(from_c-2))
    #6
    if (from_r+1 <= 7 and from_c-2 >= 0):
        if (board[from_r+1][from_c-2] == '.'):
            move_list.append(str(from_r+1)+str(from_c-2))
        elif enemy_color in board[from_r+1][from_c-2]:
            move_list.append(str(from_r+1)+str(from_c-2))
    #7
    if (from_r-1 >= 0 and from_c+2 <= 7):
        if (board[from_r-1][from_c+2] == '.'):
            move_list.append(str(from_r-1)+str(from_c+2))
        elif enemy_color in board[from_r-1][from_c+2]:
            move_list.append(str(from_r-1)+str(from_c+2))
    #8
    if (from_r+1 <= 7 and from_c+2 <= 7):
        if (board[from_r+1][from_c+2] == '.'):
            move_list.append(str(from_r+1)+str(from_c+2))
        elif enemy_color in board[from_r+1][from_c+2]:
            move_list.append(str(from_r+1)+str(from_c+2))

    return move_list

def pawn_move(board,from_r,from_c,move_list,enemy_color):
    if enemy_color=='b' and from_r+1<=7:
        if from_r == 1:
            move=2                  #initial two moves played by pawn
        else:
            move =1
        for i in range(move):
                if board[from_r+1+int(i)][from_c] == '.':
                    move_list.append(str(from_r+1+int(i))+str(from_c))
                if board[from_r+1+int(i)][from_c+1] != '.' and board[from_r+1][from_c+1][0] == enemy_color:
                    move_list.append(str(from_r+1+int(i))+str(from_c+1))
                if board[from_r+1+int(i)][from_c-1] != '.' and board[from_r+1][from_c-1][0] == enemy_color:
                    move_list.append(str(from_r+1+int(i))+str(from_c-1))

    if enemy_color=='w' and from_r-1>=0:
        if from_r ==6:
            move = 2
        else:
            move =1
        for i in range(move):
            if board[from_r-1-int(i)][from_c] == '.':
                move_list.append(str(from_r-1-int(i))+str(from_c))
            if board[from_r-1-int(i)][from_c+1] != '.' and board[from_r-1][from_c+1][0] == enemy_color:
                move_list.append(str(from_r-1-int(i))+str(from_c+1))
            if board[from_r-1-int(i)][from_c-1] != '.' and board[from_r-1][from_c-1][0] == enemy_color:
                move_list.append(str(from_r-1-int(i))+str(from_c-1))
    return move_list

def king_move(board,from_r,from_c,move_list,enemy_color):
    for i in range(from_r-1,from_r+2):                 #fr=7,fc=4      tr=6 tc=4
        for j in range(from_c-1,from_c+2):
            if (i<8 and i>0) and (j>0 and j<8):
                if board[i][j] == '.':
                    move_list.append(str(i)+str(j))
                elif board[i][j][0] == enemy_color:
                    move_list.append(str(i)+str(j))

    return move_list

def actual_move(frm,to):
    #actual conversion of moves from board parameters to list parameters
    change={8:0,7:1,6:2,5:3,4:4,3:5,2:6,1:7}
    frm=str(change[int(frm[-1])])+str(ord(frm[0])-97)      #from swaped
    to=str(change[int(to[-1])])+str(ord(to[0])-97)      #to swaped
    return frm,to

def give_movements(board,color,move):
    # To get the (to,from,piece) from the given user input
    piece=''
    to=''
    frm=''
    flag_x=False
    if move.startswith('o'):                    #special moves such as castling
        pass
#         special_moves(board,color,move)
#         return None,None,None,None,False
    else:
        # if move[0].isupper():
        #     piece=move.pop(0)
        # else:
        #     piece = 'P'
        move=move.split('-')               #e2-e4

        to=move[1]                                                                              #########################################
        frm=move[0]                                                                            ######################################
        frm,to=actual_move(frm,to)
        piece = find_piece(board,color,frm)               #which piece is at frm location
        move_list=possible_moves(board,color,piece,frm)
        valid=rule_check(to,move_list)
        if valid == 1:
            return board,color, piece, to, frm
        return board,0,0,0,0

def find_piece(board,color,frm):
    piece=''
    frm=int(frm)
    piece=board[frm / 10][frm % 10]        #frm=56 (row,col) on list
    return piece[-1]

# def special_moves(board,color,moves):
#     if color == 'b' and moves.strip() == 'o-o-o':
#         if board[7][3] == 'bK':
#             if board[7][7] == 'bR':
#                 if board[7][4] == board[7][5] == board[7][6]:
#                     movement(color,'R','h1','f1')
#                     movement(color,'K','d1','h1')
#                     return True
#     elif color == 'b' and moves.strip() == 'o-o':
#         if board[7][3] == 'bK':
#             if board[7][0] == 'bR':
#                 if board[7][1] == board[7][2]:
#                     movement(color,'R','a1','c1')
#                     movement(color,'K','d1','a1')
#                     return True
#     elif color == 'w' and moves.strip() == 'o-o-o':
#         if board[0][3] == 'wK':
#             if board[0][7] == 'wR':
#                 if board[0][4] == board[0][5] == board[0][6]:
#                     movement(color,'R','h8','f8')
#                     movement(color,'K','d8','h8')
#                     return True
#     elif color == 'w' and moves.strip() == 'o-o':
#         if board[0][3] == 'wK':
#             if board[0][0] == 'wR':
#                 if board[0][1] == board[0][2]:
#                     movement(color,'R','a8','c8')
#                     movement(color,'K','d8','a8')
#                     return True
#     else:
#         return False

def possible_moves(board,color,pieces,frm):
    #all values are less than one in movelist
    #actually they are correct in list but not on chess board
    if color == 'w':
        c_name='White'
        enemy_color='b'
    else:
        enemy_color='w'
        c_name='Black'
    move_list=[]
    from_r=int(frm) // 10
    from_c=int(frm) % 10
    if pieces=='K':
        # print ' moving piece ',c_name,' king'
        move_list = king_move(board,from_r,from_c,move_list,enemy_color)
    elif pieces == 'Q':
        # print ' moving piece ',c_name,' Queen'
        move_list = rook_move(board,from_r,from_c,move_list,enemy_color)
        move_list += bishop_move(board,from_r,from_c,move_list,enemy_color)
    elif pieces == 'R':
        # print ' moving piece ',c_name,' Rook'
        move_list = rook_move(board,from_r,from_c,move_list,enemy_color)
    elif pieces == 'B':
        # print ' moving piece ',c_name,' Bishop'
        move_list = bishop_move(board,from_r,from_c,move_list,enemy_color)
    elif pieces =='N':
        # print ' moving piece ',c_name,' Knight'
        move_list = knight_move(board,from_r,from_c,move_list,enemy_color)
    elif pieces == 'P':
        # print ' moving piece ',c_name,' Pawn'
        move_list = pawn_move(board,from_r,from_c,move_list,enemy_color)
    else:
        print "error piece = ",pieces
        return []
    #movelist is 5d and decremented by 1
    #inc_list def does swap and incr 1
    # move_list=list_incr(move_list)
    return move_list            #problem may arise in index calling board values cause [row,col=(0,0),(7,7)]

def rule_check(to,move_list):
    if move_list==[]:
         return False
    for i in move_list:
        if to == i :
            return True
    return False

def movements(board,color,piece,to,frm):
    # prev_board=board
    row =int(frm) // 10
    col=int(frm) % 10
    board[row][col]='.'

    row=int(to) // 10
    col=int(to) % 10
    board[row][col]=str(color+piece)
    new_board=board
    flag_check=ischeck(new_board,color,piece,to)    #after movements see if next moves may threat to enemy king
    print_board(new_board,flag_check)
    return new_board

def print_board(board,flag_check=False):
    if flag_check == True:
        print "********************CHESS BOARD**********************\n\n###CHECK TO KING\n\n"
    else:
        print "********************CHESS BOARD**********************\n\n"
    for i,no in zip(board,range(8,0,-1)):
        print no,'     ',
        for j in i:
            if j =='.':
                j+=' '
            print j,'    ',
        print '\n\n',
    print '\n\n         a      b        c       d       e       f       g      h'
    print '\n\n***************************************************'

def ischeck(board,color,piece,frm):
    if color == 'w':
        enemy_color='b'
    else:
        enemy_color= 'w'
    move_list=possible_moves(board,color,piece,frm)
    enemy_king_loc=[str(board.index(i))+str(i.index(j)) for i in board for j in i if j==enemy_color+'K' ]              #43
    if enemy_king_loc == []:
        return False
    # (enemy_king_loc_r,enemy_king_loc_c)=(enemy_king_loc[0],enemy_king_loc[-1])
    # king_loc=chr(int(enemy_king_loc[-1])+97)+enemy_king_loc[0]                   #eg = d5
    for i in move_list:
        if i==enemy_king_loc[0]:
            print "check"
            return True
    return False

def main():
    n=0
    print ('**************CHESS PROGRAM*******************\n\n')
    print '################((  RULES  ))##################'
    print '\nexample moves:\n - e2-e3    =    to move the piece  from e2 to e3\n - e2xe3  =  to execute the piece at e3 by e2\n - use the side row and column to give moves'
    print ' - - - - - general move :  from(RowColumn) (-/x) to(RowColumn)\n\n\n\n'
    choice=raw_input(' (to exit the game press ((( # ))))\n\n >>>>>>>>>press 1 to start the game : >>>>>>>> ')
    if choice == '1':
        print ('Initializing board .....')
        board=initilaize()
        print_board(board)
        print ('initialized. white moves first')

        # moveee=['b7-b5','a2-a4','c8-a6','a4-b5','a6-b5']

        while True:
        # for i in moveee:
            if n%2 == 0:
                color = 'w'
                print '( WHITE COLOR )'
                n+=1
            else:
                color = 'b'
                print '( BLACK COLOR )'
                n+=1


            move=raw_input(' move : ')
            if move == '#':
                break
            # move=i
            # print move
            move=move.strip()
            if '-' in move or 'x' in move:
                if len(move) == 5:
                    board1,color,piece,to,frm=give_movements(board,color,move)
            else:
                print ' \n !! invalid move '
                n -= 1
                continue
            if color==piece==0:
                print "!!!!!!!!!  Not a valid move, please try again...."
                n -= 1
                continue
            board=movements(board1,color,piece,to,frm)
    print '\n\n\n !!! you pressed # \n\nProgram Closed.......'


if __name__ == '__main__':
    main()
