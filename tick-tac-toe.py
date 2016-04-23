


#this is the tic-tac-toe game for recurse center
import random
import sys
import ttt_analytics

#creating playground
field = [[11,12,13],[21,22,23],[31,32,33]]
		
#tic and tac
o = 'o'
x = 'x'

mark = ai_mark = ai_level = ''
turn_counter = 0

#random AI function
def random_ai(field):
    flag = 1
    while flag ==1:
        n = random.randint(0, 2)
        m = random.randint(0, 2)
        if field[n][m] != x and field[n][m] != o:
            field[n][m] = ai_mark
            flag = 0
    return field

#smart AI function
def test_ai(field):
    flag = 1

    name_ai, ai_i = check_if_gamer_win_lines(field, 'ai')
    name_human, human_i = check_if_gamer_win_lines(field, 'human')
    side_ai =  check_if_gamer_win_d(field, 'ai')
    side_human =  check_if_gamer_win_d(field, 'human')
    x_num, o_num = readcenter(field)
    key, check_x, check_y = check_corners(field)
    k = i = 0
    
    if name_ai !='zero' and flag == 1:
    	k = find_emty_one_in_lane(field, name_ai, ai_i)
    	if name_ai == 'line':
			field[ai_i][k] = ai_mark
    		
    	else:
			field[k][ai_i] = ai_mark
    	flag = 0
    	print 'find_emty_one_in_lane_ai'
    	
    elif side_ai !='zero' and flag == 1:
	k = i = 0
	k, i = find_emty_one_in_diagonal(field, side_ai)
    	field[k][i] = ai_mark
    	flag = 0
    	print 'find_emty_one_in_diagonal_ai'
    	
    elif name_human !='zero' and flag == 1:
    	k = find_emty_one_in_lane(field,name_human, human_i)
    	if name_human == 'line':
    		field[human_i][k] = ai_mark
    	else:
			field[k][human_i] = ai_mark
    	flag = 0
    	print 'find_emty_one_in_lane_human'
    	
    elif side_human !='zero' and flag == 1:
    	k, i = find_emty_one_in_diagonal(field, side_human)
    	field[k][i] = ai_mark
    	flag = 0
    	print 'find_emty_one_in_diagonal_human'
    	
    elif x_num == 0 and o_num == 0 and flag == 1:
		field[1][1] = ai_mark
		flag = 0
		print 'center'
		
    elif key != 'zero' and flag == 1:
		field[check_x][check_y] = ai_mark
		flag = 0
		print 'corner'
	
    return field


#functions for checking columns, lines, diagonals and center, it returns the number of ones and zeros in the selected line/column/diagonal
def readcolumn(field, m):
    x_num = o_num = i = 0
    while i < 3:
        if field[i][m]==x:
                x_num += 1
        if field[i][m]==o:
                o_num += 1
        i += 1
    return x_num, o_num

def readline(field, m):
	x_num = o_num = i = 0
	while i < 3:
        	if field[m][i]==x:
            		x_num += 1
        	if field[m][i]==o:
            		o_num += 1
        	i += 1
	return x_num, o_num

def readdiagonal(field, side):
    if side == 'left':
        n = k = 0
        m = h = 2
    if side == 'right':
        n = h = 0
        m = k = 2
    x_num, o_num = readcenter(field)
    if field[n][k]==x:
        x_num += 1
    if field[m][h]==x:
        x_num += 1
    if field[n][k]==o:
        o_num += 1
    if field[m][h]==o:
        o_num += 1
    return x_num, o_num

def readcenter(field):
    x_num = o_num = 0
    if field[1][1]==x:
        x_num = 1
    if field[1][1]==o:
        o_num = 1
    return x_num, o_num


#fuctions for returning position of next move for smart AI
def find_emty_one_in_lane(feild, name,  i):
	if name == 'line':
		k = 0
		print 'find_emty_one_in_lane - line'
		#print i
		if field[i][0] != x and field[i][0]!=o:
			k = 0
		if field[i][1] != x and field[i][1]!=o:
			k = 1
		if field[i][2] != x and field[i][2]!=o:
			k = 2
		#print i, k
	elif name == 'column':
		k = 0
		print 'find_emty_one_in_lane - column'
		if field[1][i] != x and field[0][i]!=o:
			k = 0
		if field[1][i] != x and field[1][i]!=o:
			k = 1
		if field[2][i] != x and field[2][i]!=o:
			k = 2
		print i, k
	else:
		print 'error'
	return k

def find_emty_one_in_diagonal(feild, side):
	i = k = 0
	if side == 'right':
		#print side
		if field[0][2] != x and field[0][2]!=o:
			k = 0
			i = 2
		if field[1][1] != x and field[1][1]!=o:
			k = i = 1
		if field[2][0] != x and field[2][0]!=o:
			k = 2
			i = 0
	else:
		#print side
		if field[0][0] != x and field[0][0]!=o:
			k = 0
			i = 0
		if field[1][1] != x and field[1][1]!=o:
			k = i = 1
		if field[2][2] != x and field[2][2]!=o:
			k = 2
			i = 2
		
	return k, i

#check field on the closet to win situation
def check_if_gamer_win_d(field, gamer):
	side = 'zero'
	check_x, check_o = readdiagonal(field, 'left')
	if (check_x == 2 and check_o <1 and ai_mark=='x' and gamer=='ai') or  (check_o == 2 and check_x <1 and ai_mark=='o' and gamer=='ai') or (check_x == 2 and check_o <1 and ai_mark=='x' and gamer=='human') or  (check_o == 2 and check_x <1 and ai_mark=='o'and gamer=='human'):	
		side = 'left'
	check_x, check_o = readdiagonal(field, 'right')
	if (check_x == 2 and check_o <1 and ai_mark=='x' and gamer=='ai') or  (check_o == 2 and check_x <1 and ai_mark=='o' and gamer=='ai') or (check_x == 2 and check_o <1 and ai_mark=='x'and gamer=='human') or  (check_o == 2 and check_x <1 and ai_mark=='o'and gamer=='human'):
		side = 'right'
	return side

#functions for checking if human or AI going to win on next turn
def check_if_gamer_win_lines(field, gamer):
	name = 'zero'
	i_return = 0
	line = [0, 1, 2]
	for i in line:
		check_x, check_o = readline(field, i)
		if (check_x == 2 and check_o <1 and ai_mark=='x' and gamer=='ai') or  (check_o == 2 and check_x <1 and ai_mark=='o' and gamer == 'ai') or (check_x == 2 and ai_mark=='o' and check_o<1 and gamer=='human') or (check_o == 2 and check_x <1 and ai_mark=='x' and gamer=='human'):
			name = 'line'
			i_return = i

	for i in line:
		check_x, check_o = readcolumn(field, i)
		if (check_x == 2 and check_o <1 and ai_mark=='x') or (check_o == 2 and check_x <1 and ai_mark=='o' and gamer == 'ai') or (check_x == 2 and ai_mark=='o' and check_o<1 and gamer=='human') or (check_o == 2 and check_x <1 and ai_mark=='x' and gamer=='human'):
			name = 'column'
			i_return = i

	return (name,i_return)
		
#function for checking corners 
def check_corners(field):               
	key = 'zero'
	check_x = check_y = 0
	if field[0][0] != x and field[0][0] != o:
		key = 'true'
		check_x = check_y = 0 
	if field[2][0] != x and field[2][0] != o:
		key = 'true'
		check_x = 2 
		check_y = 0	
	if field[0][2] != x and field[0][2] != o:
		key = 'true'
		check_x = 0 
		check_y = 2
	
	if field[2][2] != x and field[2][2] != o:
		key = 'true'
		check_x = check_y = 2
	return key, check_x, check_y
		

#check field on the win situation
def ifwin(field):
    check_x, check_o = readdiagonal(field, 'left')
    win(check_x, check_o)
    check_x, check_o = readdiagonal(field, 'right')
    win(check_x, check_o)
    i = 0
    while i < 3:
        check_x, check_o = readline(field, i)
        win(check_x, check_o)
        i += 1
    i = 0
    while i < 3:
        check_x, check_o = readcolumn(field, i)
        win(check_x, check_o)
        i += 1
        
#the end of the game if someone won
def win(check_x, check_o):
    if check_x == 3:
        print 'X - win!'
        sys.exit()
    if check_o == 3:
        print 'O - win!'
        sys.exit()
        
#input of users turn
def user_input():
    flag = True
    while flag ==True:
        try:
            input = raw_input()
            n = int(input[0])-1
            m = int(input[1])-1
            if field[n][m] != x and field[n][m] != o:
                field[n][m] = mark
                flag = False
            else:
                print "Please try again. This cell already taken."
        except:
            print "Please try again. Number is not valid."

#printing of playground in a readable format
def printline(field):
    print '________'
    for line in field:
        A = ''
        for a in line:
            s = str(a)
            if s == 'x' or s == 'o':
                s = s + ' '
            A = A + s + ' '
        print A
    print '________'

#selection side
print "Please choose your side: x or o"
while True:
    mark = raw_input()
    if mark == 'x':
        turn = 'your_turn'
        ai_mark = o
        break
    
    elif mark == 'o':
        turn = 'ai_turn'
        ai_mark = x
        break

    else:
        print "Please try again. Choose your side: x or o"

#selection of AI level
print "Please choose AI level: smart or random"
while True:
    ai_level = raw_input()
    if ai_level == 'smart' or ai_level == 'random' or ai_level == 'test':
        break
    
    else:
        print "Please try again. Choose AI level: smart or random"


printline(field)

#the game itself
while True:
    if turn == 'your_turn':
        print "Type cells number:"
        user_input()
        printline(field)
        ifwin(field)
        turn = 'ai_turn'
        turn_counter +=1
        if turn_counter>8:
            break

    if turn == 'ai_turn':
        if ai_level == 'random':
            field = random_ai(field)
        elif ai_level == 'smart':
            field = test_ai(field)
        printline(field)
        ifwin(field)
        turn = 'your_turn'
        turn_counter +=1
        if turn_counter>8:
            break

#if it took more than 8 turns, and no one has won - this is a draw
print 'Drawn!'
sys.exit()
