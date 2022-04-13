"""
This is a 8-puzzle problem which separated to 4 part.
It's forth part for the following code.
"""

"""
The following Data Structure are for the 8-puzzle forth part 
These Data Structure can implement priority queue which will be used when
solving 8-puzzle problem

Usage:
Instruction 1. enqueue [X X X X X X X X X] (int , int)
Parameter:
X is the number between 0 ~ 8, those presens the sequence of a puzzle state.
(int , int) is (cost , heuristic function output)
The cost means the move step from initial state to current state.
The heuristic function has not been implemented yet.
It will show in the next part for "Manhattan_distance.py"
"""
import copy

class Node:
    # The count is the order of being push into the priority Queue.
    # And The min heap priority Queue will maintain FIFO principle when the two-
    # Node's Scores equal to each other, pop the smaller "count" first.
    def __init__(self , sequence =[] , cost = 0 , heuristic = 0 , count = -1):
        self.Scores = int(cost) + int(heuristic)
        self.Sequence = sequence
        self.count = count

"""
The root index is "0"
Parent node = (n - 1) // 2
Left Child node = 2 * n + 1
Right Child node = 2 * n + 2
"""
class min_heap:
    def __init__(self):
        self.heap = []
    def __len__(self):
        return len(self.heap)
    def insert(self, Node ):
        self.heap.append(Node)
        # Pass the last node's index to the function heapify.
        self.__bubble_up(len(self.heap) - 1)
        print("Insert OK!")
    # The function pop has already been implemented in the python. 
    # But in heap, it also have to heapify after pop the top value.
    # The function pop in the heap called "delete" in the following code.
    def delete(self):
        if len(self.heap) == 0 :
            return 0
        top_value = self.heap[0].Sequence
        # swap the top value and the bottom value
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__siftdown(0)
        print("Got [" , end = '')
        for i , number in enumerate(top_value):
            if i < ( len(top_value) - 1 ):
                print(number , end = ' ')
            else:
                print(number , end = '') 
        print("]")
        return 1
        # return top_value

    def __bubble_up(self, n):        
        while n > 0 and self.heap[(n - 1) // 2].Scores > self.heap[n].Scores:         
            parent_node = (( n-1 ) // 2)
            self.heap[n] , self.heap[parent_node] = \
            self.heap[parent_node] , self.heap[n]
            n = parent_node 
            # remember the count of Node will be used to maintain FIFO principle of the min heap(Priority Queue)
            self.__check_count(0) 
    def __siftdown(self , n):
        while (2 * n + 1 ) < len(self.heap):
            smaller_index = 2 * n + 1
            # remember the count of Node will be used to maintain FIFO principle of the min heap(Priority Queue)
            if (2 * n + 2) < len(self.heap) and self.heap[2 * n + 2 ].Scores < self.heap[ 2 * n + 1 ].Scores:
                smaller_index = 2 * n + 2  
            if self.heap[smaller_index].Scores > self.heap[n].Scores:
                return
            # swap
            self.heap[smaller_index], self.heap[n] = \
            self.heap[n], self.heap[smaller_index]
            n = smaller_index
            # remember the count of Node will be used to maintain FIFO principle of the min heap(Priority Queue)
            self.__check_count(0)

    def __check_count(self , n):
        while (2 * n + 1 ) < len(self.heap):
            smaller_index = 2 * n + 1
            if(2 * n + 2) < len(self.heap) and self.heap[2 * n + 2 ].Scores == self.heap[ 2 * n + 1 ].Scores:
                if self.heap[(2 * n + 2)].count < self.heap[(2 * n + 1)].count:
                    smaller_index = 2 * n + 2
            if self.heap[smaller_index].Scores != self.heap[n].Scores \
            or self.heap[smaller_index].count > self.heap[n].count:
                return
            # swap
            self.heap[smaller_index], self.heap[n] = \
            self.heap[n], self.heap[smaller_index]
            n = smaller_index
        
    def __print_whole_heap(self):
        print("The whole tree is :[" , end = '')
        for i , number in enumerate(self.heap):
            if i < ( len(self.heap) - 1 ):
                print('({0},{1},{2})'.format(number.Sequence,number.Scores,number.count), end = ' ')
            else:
                print('({0},{1},{2})'.format(number.Sequence,number.Scores,number.count) , end = '')
        print("]")

def main():
    score_heap = min_heap() # Initialize the min heap 
    count = 0 # To maintain the FIFO principle of the Priority Queue.
    try:
        while(True):
            instruction = input()
            # DOMjudge's input will ending with "\r\n"
            # And general python program only contain "\n" to distinguish every line command."
            instruction = instruction.replace('\r','')           
            if(instruction == 'enqueue'):
                sequence_string = input()
                count += 1
                sequence = sequence_string_handle(sequence_string , 'empty tile')
                score_list = create_score_list(sequence_string)
                # pass the sequence , cost , heuristic and count into the constructor of "Node" class.
                score_heap.insert(Node(sequence, score_list[0] , score_list[1] , count))
                
            elif(instruction == 'dequeue'):
                if len(score_heap.heap) == 0:
                    print("Queue is empty!!")
                else: 
                    score_heap.delete()
                    # print(delete_top_sequence)
    except EOFError: # When DOMjudge gives a EOF input
        return 

# The String input will be like [X X X X X X X X X] (X, X) (The input form is [sequence](cost,heuristic))
# This function will eliminate the inputs like "[" , "]" , " " , "(X, X)" and "0" except reserve operator.
def sequence_string_handle(sequence,reserve_operator):
    if(reserve_operator == 'none'):
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
        sequence = sequence.replace("0","")
        sequence = sequence.replace("(","") 
        sequence = sequence.replace(")","")
        sequence = sequence.replace(",","")
    else:  # reserve_operator == "empty tile"
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
    
    # extract the two part at "(" from sequence
    sequence_list = sequence.split('(')
    
    # only take sequence part
    return str(sequence_list[0])

def create_score_list(sequence):
    sequence_list = sequence.split('(')
    score_list = sequence_list[1].split(', ')
    score_list[1] = score_list[1].replace(')','')
    return score_list 

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

    if( is_legal_postition( point , puzzle_matrix , 'down' ) ) :     
        print("move %s to down" % number)
        swap_points_coordinates( puzzle_matrix , sequence , number , 'down')
        sequence = matrix_to_sequence(puzzle_matrix)
        print(sequence)

    if( is_legal_postition( point , puzzle_matrix , 'left' ) ) :
        print("move %s to left" % number)
        swap_points_coordinates(puzzle_matrix , sequence , number , 'left')
        sequence = matrix_to_sequence(puzzle_matrix)
        print(sequence)
        
    if( is_legal_postition( point , puzzle_matrix , 'right' ) ) :
        pass
        print("move %s to right" % number)
        swap_points_coordinates( puzzle_matrix , sequence , number , 'right')
        sequence = matrix_to_sequence(puzzle_matrix)

    else :
        pass
        # print("illegal")
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
        if i != len(sequence) - 1:
            print(sequence[i] , end = ' ')
        else : 
            print(sequence[i] , end = '')
    print("]")

if __name__ == "__main__" : 
    main()