"""
This is a 8-puzzle problem which separated to 4 part.
It's second part for following code.
In this part,it will calculate how many steps can be moved at a given state.
Before calculating, the given sequence will be transformed to a matrix with 9 tiles
By the 9-matrix, every tiles has a number on it, and the 0 is presents the empty tiles(total 8 tiles can be moved).
The Successor function will calculate the total amount of 0 tile that steps it can move
(it called the Number of successors of test data). 
The move direction in the order of "up, down, left, right".
I.g. give a sequence [3 1 2 4 5 0 6 8 7] 
The matrix will be:
3|1|2|
4|5|7|
6|8|0|
This function will output:
2(Number of successors of test data)
move 0 to up
[3 1 2 4 5 0 6 8 7]
move 0 to left
[3 1 2 4 5 7 6 0 8]

Usage:
Input the test times, first.
Then, input a string like:[X X X X X X X X X]
Parameter:
X is the number between 0 ~ 8, those presens the sequence of a puzzle state.

Output:
line 1. Number of successors(the move steps can be moved) of test sequence
line 2. The move action.
line 3. The state sequence after moveing.
"""
import copy
def main():
    test_amount = int(input())       #The times for test
    for i in range(test_amount):
        sequence = input()  #The value for the 8-puzzle.
        new_sequence = string_handle(sequence,'none') 
        if isSolvable(new_sequence) == True:
            puzzle_matrix = create_coordinate( string_handle(sequence,'empty tile') )
        
            count = 0
            count = count_action(puzzle_matrix,sequence)
            print(count)

            if( is_legal_postition( copy.deepcopy( puzzle_matrix) , sequence , 'up' ) ):
                print("move 0 to up")
                swap_points_coordinates( copy.deepcopy( puzzle_matrix) , sequence , 'up')
                
            if( is_legal_postition( copy.deepcopy( puzzle_matrix) , sequence , 'down' ) ) :     
                print("move 0 to down")
                swap_points_coordinates( copy.deepcopy( puzzle_matrix) , sequence , 'down')
                
            if( is_legal_postition( copy.deepcopy( puzzle_matrix) , sequence , 'left' ) ) :
                print("move 0 to left")
                swap_points_coordinates(copy.deepcopy( puzzle_matrix) , sequence , 'left')
                
            if( is_legal_postition( copy.deepcopy( puzzle_matrix) , sequence , 'right' ) ) :
                print("move 0 to right")
                swap_points_coordinates( copy.deepcopy( puzzle_matrix) , sequence , 'right')
                
            else :
                pass
                # print("illegal")
                # successor(sequence)
                pass
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
# Then the disorder_count must plus the row of the empty tile(input likes "0") Before check if resovable
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

def empty_tile_point_index(sequence):
    sequence = string_handle(sequence,'empty tile')
    row = 0
    column = 0
    for i in range(len(sequence)):
        if sequence[i] == "0":
            if i // 3 == 0:
                row = 0
                column = (i % 3)
            elif i // 3 == 1:
                row = 1
                column = (i % 3)
            else :
                row = 2
                column = (i % 3)
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

def create_coordinate(sequence):
    empty_tile = 0
    index = 0
    puzzle_matrix = [[0]*3 for i in range(3)]
    for i in range(len (puzzle_matrix) ):
        for j in range( len ( puzzle_matrix[0]) ):
            puzzle_matrix[i][j] = sequence[index] 
            index += 1

    return puzzle_matrix

def is_legal_postition( puzzle_matrix , sequence , move_direction ):
        empty_tile = 0
        point = empty_tile_point_index(sequence)

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

def swap_points_coordinates(puzzle_matrix , sequence , move_direction):
    
    empty_tile = 0
    empty_point = empty_tile_point_index(sequence)
    new_point = empty_point.copy()

    if(move_direction == 'up'):
        new_point[0] -= 1
    elif(move_direction == 'down'):
        new_point[0] += 1
    elif(move_direction == 'left'):
        new_point[1] -= 1
    elif(move_direction == 'right'):
        new_point[1] += 1

    puzzle_matrix[ new_point[0] ] [ new_point[1] ] , puzzle_matrix[ empty_point[0] ] [empty_point[1] ] \
    = puzzle_matrix[ empty_point[0] ] [ empty_point[1] ] , puzzle_matrix[ new_point[0] ] [ new_point[1] ]

    print_matrix_to_sequence(copy.deepcopy( puzzle_matrix))

def print_matrix(puzzle_matrix):
    print('before move - coordinate system:')
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

def count_action(puzzle_matrix , sequence):
    count = 0
    if( is_legal_postition( puzzle_matrix , sequence , 'up' ) ):
        count += 1
    if( is_legal_postition( puzzle_matrix , sequence , 'down' ) ):
        count += 1
    if( is_legal_postition( puzzle_matrix , sequence , 'left' ) ):
        count += 1
    if( is_legal_postition( puzzle_matrix , sequence , 'right' ) ):
        count += 1
    return count

if __name__ == "__main__" : 
    main()