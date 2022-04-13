"""
This is a 8-puzzle problem which separated to 4 part.
It's third part for following code.
This function will calculate the Manhattan distance between current state & goal state.
The goal state's sequence is [0,1,2,3,4,5,6,7,8].
Definition of Manhattan distance:
The move step(including row and column) difference between current state and goal state.

Usage:
Input the test times, first.
Then, input a string like:[X X X X X X X X X]
Parameter:
X is the number between 0 ~ 8, those presens the sequence of a puzzle state.

P.S.
The cal_Manhattan_distance function reference:https://www.796t.com/post/N2l4NjY=.html
"""
import copy
def main():
    test_amount = int(input())       #The times for test
    for i in range(test_amount):
        sequence_string = input()  #The value for the 8-puzzle.
        no_zero_sequence = string_handle(sequence_string ,'none') 
        sequence = string_handle(sequence_string , 'empty tile')

        goal_sequence = [0,1,2,3,4,5,6,7,8]

        puzzle_matrix = [[0,0,0],[0,0,0],[0,0,0]]
        
        if isSolvable(no_zero_sequence) == True:

            puzzle_matrix = create_coordinate( sequence )
            current_puzzle_matrix = copy.deepcopy(puzzle_matrix)
            current_sequence = copy.deepcopy(sequence)
            
            index = 0
            number = sequence[index]
            print( cal_Manhattan_distance(sequence) )
        else :
            pass
            # print("unsolvable")

# The String input will be like [X X X X X X X X X] 
# This function will eliminate the inputs like "[" , "]" , " " and "0" except reserve operator.
def string_handle(sequence,reserve_operator):
    if(reserve_operator == 'none'):
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
        sequence = sequence.replace("0","")
    else :  # reserve_operator == "empty tile"
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
    return sequence

# If the problem is N-puzzle,and the N is not an even(is an odd)
# Then the disorder_count must plus the row of the empty tile(input likes "0") Before check if resolvable
def empty_tile_row_index(sequence):
    sequence = string_handle(sequence)
    row = 0
    for i in range(len(sequence)):
        if sequence[i] == "0":
            if i // 3 == 0:
                row = 0
            elif i // 3 == 1:
                row = 1
            else :
                row = 2
    return row

def find_point(sequence , number):
    if(sequence[0] == "["):
        sequence = string_handle(sequence,'empty tile')
    row = 0
    column = 0
    for i in range(len(sequence)):
        if sequence[i] == str(number):
            if i // 3 == 0:
                row = 0
                column = (i % 3)
            elif i // 3 == 1:
                row = 1
                column = (i % 3)
            else :
                row = 2
                column = (i % 3)
    # print("[row,column] = [%d,%d]" %(row,column))
    return [row,column]

#To check this N-puzzle if solvable for the N is an even(Odd version not be written)
def isSolvable(sequence):
    disorder_count = 0
    for i in range(len (sequence )):
        for j in range ( len (sequence )):
            a = sequence[i]
            b = sequence[j]
            if a > b :
                disorder_count += 1
            else :
                pass
    return (disorder_count % 2 == 0)

def successor(puzzle_matrix, sequence , number):

    point = find_point(sequence , number)

    if( is_legal_postition( point , puzzle_matrix , 'up' ) ):
        print('move %s to up' % number)
        swap_points_coordinates( puzzle_matrix , sequence , number , 'up')
        sequence = matrix_to_sequence(puzzle_matrix)
        print(sequence)
        # print_sequence(current_sequence)

    if( is_legal_postition( point , puzzle_matrix , 'down' ) ) :     
        print("move %s to down" % number)
        swap_points_coordinates( puzzle_matrix , sequence , number , 'down')
        sequence = matrix_to_sequence(puzzle_matrix)
        print(sequence)
        # print_sequence(current_sequence)

    if( is_legal_postition( point , puzzle_matrix , 'left' ) ) :
        print("move %s to left" % number)
        swap_points_coordinates(puzzle_matrix , sequence , number , 'left')
        sequence = matrix_to_sequence(puzzle_matrix)
        print(sequence)
        # print_sequence(current_sequence)
        
    if( is_legal_postition( point , puzzle_matrix , 'right' ) ) :
        pass
        print("move %s to right" % number)
        swap_points_coordinates( puzzle_matrix , sequence , number , 'right')
        sequence = matrix_to_sequence(puzzle_matrix)
        # print(current_sequence)
        # print_sequence(current_sequence)

    else :
        pass
        # print("illegal")
        # successor(sequence)
        pass

def create_coordinate(sequence):
    index = 0
    puzzle_matrix = [[0]*3 for i in range(3)]
    for i in range(len (puzzle_matrix) ):
        for j in range( len ( puzzle_matrix[0]) ):
            puzzle_matrix[i][j] = sequence[index] 
            index += 1

    return puzzle_matrix

def create_goal_state():
    number = 0
    puzzle_matrix = [[0]*3 for i in range(3)]
    for i in range(len (puzzle_matrix) ):
        for j in range( len ( puzzle_matrix[0]) ):
            puzzle_matrix[i][j] = number
            number += 1
    return puzzle_matrix

def is_legal_postition( point, puzzle_matrix, move_direction ):

        if(move_direction == 'up'):

            if(point[0] - 1 < 0 ):
                return False
            else : return True
        elif(move_direction == 'down'):
            if(point[0] + 1 >= len ( puzzle_matrix ) ) :
                return False
            else : return True
        elif(move_direction == 'left'):
            if(point[1] - 1 < 0 ):
                return False
            else : return True
        elif(move_direction == 'right'):
            if(point[1] + 1 >= len ( puzzle_matrix[0] ) ) :
                return False
            else : return True

def swap_points_coordinates(puzzle_matrix , sequence , number , move_direction):
    
    # print("sequence: %s" % sequence)

    point = find_point(sequence, number) # get coordinate (x,y) of point before a move
    new_point = point.copy() # the point's destination is called "new_point"

#  Calculate the coordinate of point(called new_point in the following) in a move_direction.
    if(move_direction == 'up'):
        # print('up')
        new_point[0] -= 1
    elif(move_direction == 'down'):
        new_point[0] += 1
    elif(move_direction == 'left'):
        new_point[1] -= 1
    elif(move_direction == 'right'):
        new_point[1] += 1

    #Two points swap their coordinate in the puzzle matrix.
    puzzle_matrix[ new_point[0] ] [ new_point[1] ] , puzzle_matrix[ point[0] ] [point[1] ] \
    = puzzle_matrix[ point[0] ] [ point[1] ] , puzzle_matrix[ new_point[0] ] [ new_point[1] ]

    # print_matrix(puzzle_matrix)
    # print_matrix_to_sequence(puzzle_matrix)

    return puzzle_matrix
"""
This function will calculate the Manhattan distance between current state
(it can be imagined to a puzzle matrix) & goal state 
(it can be imagined to a puzzle matrix as well)
// 3 : row 
% 3 : column
"""
def cal_Manhattan_distance(current_sequence):
    sum = 0
    for i , value in enumerate(current_sequence):
        if value == '0' or value == '\r':
            continue
        current_state_row , current_state_column = i // 3 , i % 3
        #To calculate the coordinate of the sequence[0,1,2,3,4,5,6,7,8]
        goal_state_row , goal_state_column = int(value) // 3 , int(value) % 3   
        sum += abs(current_state_row - goal_state_row) + \
        abs(current_state_column - goal_state_column)
    
    return sum

def print_matrix(puzzle_matrix):
    print('current - coordinate system:')
    for i in range( len ( puzzle_matrix ) ):
        for j in range( len ( puzzle_matrix[0] ) ):
            print(puzzle_matrix[i][j] , end = ',')
        print("")

def print_matrix_to_sequence(puzzle_matrix):
    print("[" , end = '')
    for i in range( len ( puzzle_matrix ) ):
        for j in range( len ( puzzle_matrix[0] ) ):
            if (i == ( len(puzzle_matrix) -1 ) and j == ( len(puzzle_matrix) -1 ) ) :
                print(puzzle_matrix[i][j] , end = ']\n')
            else:
                print(puzzle_matrix[i][j] , end = ' ')

def matrix_to_sequence(puzzle_matrix):
    sequence = []
    for i in range( len ( puzzle_matrix ) ):
        for j in range( len ( puzzle_matrix[0] ) ):
                sequence.append( puzzle_matrix[i][j] )
    return sequence

def print_sequence(sequence):
    print("current sequence: ")
    print("[" , end = '')
    for i in range( len ( sequence ) ):
        if i != len(sequence -1):
            print(sequence[i] , end = ' ')
        else : 
            print(sequence[i] , end = '')
    print("]")

if __name__ == "__main__" : 
    main()