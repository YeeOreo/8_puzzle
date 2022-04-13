"""
This is an Artificial Intelligence for the 8-puzzle proglem.
This system can be separated to four part.
They are:
1. Solvability.py
2. Successor.py
3. Manhattan_distance.py
4. Priority_queue.py
I made this system step by step as above.
Test data from : http://cjlin.nlplab.tw/AI1102_assignments.html#prj1_5
Note:
**************************************************************************************
1. This puzzle is only be distinguished by it's number value on itself not for 
image puzzle.
2. This puzzle project is only for 3*3 Dimension puzzle.
**************************************************************************************
Using A* algorithm to find the most cheapest state and choose.
The heuristic function is separated to two part.
The heuristic function can be written to be f(n) = g(n) + h(n), n is a state. 
---------------------------------------------------------------------------------------
g(n) is the real cost from start state to the goal state, so far. 
h(n) is the cheapest evaluated cost from n state to the goal state.
And in conclusion, f(n) can be viewed as the cheapest evaluated cost plus real cost so far-
from start state pass the n state to the goal state.
---------------------------------------------------------------------------------------
the evaluated costs are calculated by using Manhattan Distance between-
current state to the goal state, in the A* algorithm.

P.S.
The cal_Manhattan_distance function reference:https://www.796t.com/post/N2l4NjY=.html
"""

"""
Usage:input one sequence like:[X X X X X X X X X]
Parameter:
X is the number between 0 ~ 8, those presens the sequence of a puzzle state.
"""

"""
The following Data Structure are for the 8-puzzle's Priority Queue.
These Data Structure can store every state and it's cost.
"""
import copy
import sys

class Node:
    # The count is the order of being push into the priority Queue.
    # And The min heap priority Queue will maintain FIFO principle when the two-
    # Node's scores equal to each other, pop the smaller "count" of Node first.
    # Note:The parameter heuristic is the output of heuristic function.
    def __init__(self , sequence =[] , cost = 0 , heuristic = 0 , count = -1 \
    , move_direction = 'None' , parent_node = None):
        self.scores = int(cost) + int(heuristic)
        self.cost = cost
        self.heuristic = heuristic 
        self.state = sequence
        self.count = count
        self.action = move_direction
        self.parent_node = parent_node

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
        # Pass the last node's index to the function maintain the properties of the min heap.
        self.__bubble_up(len(self.heap) - 1)
        # Insert OK!
    # The function pop has already been implemented in the python. 
    # But in heap, it also have to heapify after pop the top value.
    # The function pop in the heap called "delete" in the following code.
    def delete(self):
        if len(self.heap) == 0 :
            return 0
        top_value = self.heap[0] # Return a Node.
        # Swap the top value and the bottom value.
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__siftdown(0)
        # print("Got [" , end = '')
        # A state is performed to be a sequence.
        # for i , number in enumerate(top_value.state):
            # if i < ( len(top_value.state) - 1 ):
                # print(number , end = ' ')
            # else:
                # print(number , end = '') 
        # print("]")
        # self.__print_whole_heap()
        return top_value
    # When insert a Node into the heap, it will uses this function to maintain properties of the min heap. 
    def __bubble_up(self, n):        
        while n > 0 and self.heap[(n - 1) // 2].scores > self.heap[n].scores:
            # swap 
            # print("swaping...")
            # print("n = %d" % n )
            # print("( n-1 ) // 2 : %d" % ((n-1) // 2))
            # print("heap[ ( n-1 ) // 2 ] = %d" % self.heap[(n - 1) // 2])
            # print("heap[n] = %d" % self.heap[n])           
            parent_node = (( n-1 ) // 2)
            self.heap[n] , self.heap[parent_node] = \
            self.heap[parent_node] , self.heap[n]
            # self.heap[n] , self.heap[(n-1) // 2] = self.heap[(n-1) // 2] , self.heap[n]
            n = parent_node 
            # Remember the count of Node will be used to maintain FIFO principle of the min heap(Priority Queue)
            self.__check_count(0)
        # print(self.heap)   
    # When delete a Node from the heap, it will uses this function to maintain properties of the min heap. 
    def __siftdown(self , n):
        while (2 * n + 1 ) < len(self.heap):
            smaller_index = 2 * n + 1
            if (2 * n + 2) < len(self.heap) and self.heap[2 * n + 2 ].scores < self.heap[ 2 * n + 1 ].scores:
                smaller_index = 2 * n + 2  
            if self.heap[smaller_index].scores > self.heap[n].scores:
                return
            # swap
            self.heap[smaller_index], self.heap[n] = \
            self.heap[n], self.heap[smaller_index]
            n = smaller_index
            # Remember the count of Node will be used to maintain FIFO principle of the min heap(Priority Queue)
            self.__check_count(0)
    # If there are two Node's scores equal, then the smaller count of the Node is putted on the upper place. 
    # (This function used to maintain the "First In First Out" principle of the Priority Queue)
    def __check_count(self , n):
        while (2 * n + 1 ) < len(self.heap):
            smaller_index = 2 * n + 1
            if(2 * n + 2) < len(self.heap) and self.heap[2 * n + 2 ].scores == self.heap[ 2 * n + 1 ].scores:
                if self.heap[(2 * n + 2)].count < self.heap[(2 * n + 1)].count:
                    smaller_index = 2 * n + 2
            if self.heap[smaller_index].scores != self.heap[n].scores \
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
                # print('id = %d' %(id(number)) , end = ' ')
                # print('{0}'.format(number.scores))
                print('({0},{1},{2})'.format(number.Sequence,number.scores,number.count), end = ' ')
            else:
                # print('id = %d' %(id(number)) , end = '')
                print('({0},{1},{2})'.format(number.Sequence,number.scores,number.count) , end = '')
        print("]")

def main():
    score_heap = min_heap() # Initialize the min heap.
    count = 0 # To maintain the FIFO principle of the Priority Queue.
    """ The Manhattan Distance calculation way will use this-
    goal state in heuristic function"""
    goal_sequence = '012345678' 
    #This AI only supports to solve the 8-puzzle(3*3 Dimension) problem.
    puzzle_string = sys.stdin.readline()
    # The end character "\r\n" will come from the DOMjudge system.
    # The end character "\n" will come from the self system input.
    if puzzle_string[-2] == '\r':
        puzzle_string = puzzle_string[:-2]
    elif puzzle_string[-1] == '\n':
        puzzle_string = puzzle_string[:-1]

    puzzle_no_zero_sequence = sequence_string_handle(puzzle_string , 'none')
    puzzle_sequence = sequence_string_handle(puzzle_string , 'empty tile')
    """Remember To cut the '0' which present empty tile in the puzzle before to check if-
    is solvable."""
    if isSolvable(puzzle_no_zero_sequence) == False:
        print("No solution!!")
    else : 
        # print("This is else!!!")
        if puzzle_sequence == goal_sequence:
            print("It is the goal state.")
        else :
            my_node = Node(sequence = puzzle_sequence , cost = 0 , \
            heuristic = cal_Manhattan_distance(puzzle_sequence) , \
            count = 0 ,move_direction = 'None' , parent_node = None)
            # print_Node_data(my_node)
            priority_queue = min_heap()
            priority_queue.insert(my_node)
            puzzle_matrix = create_coordinate(puzzle_sequence)
            # print_matrix(puzzle_matrix)
            # print_Node_data(my_node)
            A_Star( priority_queue , goal_sequence , puzzle_matrix , puzzle_sequence)
            # for i , value in enumerate( priority_queue.heap ):    
            #     print(value.state)

def A_Star( priority_queue , goal_state , puzzle_matrix , sequence):
    final = Node()
    # print("Initial puzzle matrix:")
    # print_matrix(puzzle_matrix)
    # print_Node_data(final)
    # print(len(priority_queue))

    while len(priority_queue) > 0 :
        # print("len(priority_queue): %d" % len(priority_queue))
        my_node = priority_queue.delete()   
        puzzle_matrix = create_coordinate(my_node.state)
        sequence = my_node.state
        # print_Node_data(my_node)
        if my_node.state == goal_state:
            final = my_node
            break
        """Remember The function swap_point_coordinate that in the find_successor will change-
        the passed puzzle_matrix and puzzle sequence, because it is only for checking-
        before real moving, so use copy.deepcopy instead."""
        # The "find_successor" function will returns [next state , next action]
        # number = "0" presents the empty tile in the puzzle
        # print("The puzzle matrix and the sequence in the \"find_successor\" function:")
        # print_matrix (puzzle_matrix)
        # print_sequence (sequence)
        next_state_list = find_successor(copy.deepcopy(puzzle_matrix) \
        , copy.deepcopy(sequence) , number = 0 ) 
        # value[0] = next_state, type:list; value[1] = next_action
        for i , value in enumerate(next_state_list):
            # print("the puzzle_matrix in the Priority_Queue, now:")
            next_state = sequence_string_handle(str(value[0]) , 'empty tile')
            # print_matrix( create_coordinate(next_state) )
            new_node = Node(sequence = next_state , cost = (my_node.cost + 1) , \
            heuristic = cal_Manhattan_distance(next_state) , \
            count = i , move_direction = value[1] , parent_node = my_node)
            # print_Node_data(new_node)
            priority_queue.insert(new_node) # enqueue
    if final == None:
        print("No solution!!")
    else:
        current = final
        path = []
        # print("final Node's parent_node:")
        # print_Node_data(final.parent_node)
        # print("--------------------------------------------------------------")
        # print("--------------------------------------------------------------")
        # print("--------------------------------------------------------------")
        while current.parent_node != None:
            # print("move 0 to %s" % current.action)
            # print_Node_data(current)
            # if current.action != "None":
            path.append(current.action)
            # print("current path list is:")
            # print(path)
            current = current.parent_node   
        # print("final path list:")
        # print(path) 
        path.reverse()
        for i , action in enumerate(path):
            if action != 'None':
                print("move 0 to %s" % action)

# The String input will be like [X X X X X X X X X] (X, X) (The input form is [sequence](cost,heuristic))
# This function will eliminate the inputs like "[" , "]" , " " , "(X, X)" and "0" except reserve operator.
def sequence_string_handle(sequence,reserve_operator):
    if(reserve_operator == 'none'):
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
        sequence = sequence.replace("0","")
        sequence = sequence.replace("'","")
        sequence = sequence.replace(",","")
    else:  # reserve_operator == "empty tile"
        sequence = sequence.replace("[","")
        sequence = sequence.replace("]","")
        sequence = sequence.replace(" ","")
        sequence = sequence.replace("'","")
        sequence = sequence.replace(",","")
    return sequence

def create_score_list(sequence):
    sequence_list = sequence.split('(')
    score_list = sequence_list[1].split(', ')
    # print(score_list)
    score_list[1] = score_list[1].replace(')','')
    # print(score_list)  
    return score_list 
# To find the coordinate of the passing point.
def find_point(sequence , number):
    if(sequence[0] == "["):
        sequence = sequence_string_handle(sequence,'empty tile')
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

# To check this N-puzzle if solvable for the N is an even(Odd version not be written)
# Addition Information:If the problem is N-puzzle,and the N is not an even(is an odd).
# Then the disorder_count must plus the row of the empty tile(input likes "0") Before check if resolvable
def isSolvable(sequence):
    disorder_count = 0
    for i in range( len(sequence) ):
        for j in range( i + 1 , len(sequence) ):
            a = sequence[i]
            b = sequence[j]
            if a > b :
                disorder_count += 1
            else :
                pass
    return (disorder_count % 2 == 0)

# This is a checking function before moving function for this 8-puzzle.
# This function will find legal state and return [next state, next action] as output
# The move direction in the order of {up, down, left, right}.
def find_successor(puzzle_matrix, sequence , number):
    # get coordinate (x,y) of point before a move
    point = find_point(sequence , number)
    # The output for all the legal state after doing the action.
    next_state_list = []
    if( is_legal_postition( point , puzzle_matrix , 'up' ) ):
        # copy Initial puzzle_matrix first
        future_puzzle_matrix = copy.deepcopy( puzzle_matrix )
        # Then copy return to origin sequence prevent sequence being modified during-
        # executing swap_points_coordinates because python is "pass by reference".
        sequence = matrix_to_sequence(future_puzzle_matrix) 
        swap_points_coordinates( future_puzzle_matrix ,  sequence  , number , 'up')
        # Writing into the next_state_list
        future_sequence = matrix_to_sequence(future_puzzle_matrix)
        next_action = 'up'
        next_state_list.append( [future_sequence , next_action] )

    if( is_legal_postition( point , puzzle_matrix , 'down' ) ) :     
        # copy Initial puzzle_matrix first
        future_puzzle_matrix = copy.deepcopy( puzzle_matrix )
        # Then copy return to origin sequence prevent sequence being modified during-
        # executing swap_points_coordinates because python is "pass by reference".
        sequence = matrix_to_sequence(future_puzzle_matrix) 
        swap_points_coordinates( future_puzzle_matrix ,  sequence  , number , 'down')
        # Writing into the next_state_list
        future_sequence = matrix_to_sequence(future_puzzle_matrix)
        next_action = 'down'
        next_state_list.append( [future_sequence , next_action] )
        
    if( is_legal_postition( point , puzzle_matrix , 'left' ) ) :
        # copy Initial puzzle_matrix first
        future_puzzle_matrix = copy.deepcopy( puzzle_matrix )
        # Then copy return to origin sequence prevent sequence being modified during-
        # executing swap_points_coordinates because python is "pass by reference".
        sequence = matrix_to_sequence(future_puzzle_matrix) 
        swap_points_coordinates( future_puzzle_matrix ,  sequence  , number , 'left')
        # Writing into the next_state_list
        future_sequence = matrix_to_sequence(future_puzzle_matrix)
        next_action = 'left'
        next_state_list.append( [future_sequence , next_action] )
        
    if( is_legal_postition( point , puzzle_matrix , 'right' ) ) :
        # copy Initial puzzle_matrix first
        future_puzzle_matrix = copy.deepcopy( puzzle_matrix )
        # Then copy return to origin sequence prevent sequence being modified during-
        # executing swap_points_coordinates because python is "pass by reference".
        sequence = matrix_to_sequence(future_puzzle_matrix) 
        swap_points_coordinates( future_puzzle_matrix ,  sequence  , number , 'right')
        # Writing into the next_state_list
        future_sequence = matrix_to_sequence(future_puzzle_matrix)
        next_action = 'right'
        next_state_list.append( [future_sequence , next_action] )
    else :
        pass
        # print("illegal")
        # successor(sequence)

    return next_state_list

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
        # print("up , point = (%d,%d)" % (new_point[0], new_point[1]) )
        # print("up sequence")
        # print_sequence(sequence)
        # print_matrix(puzzle_matrix)
        new_point[0] -= 1
        # print("up , new_point = (%d,%d)" % (new_point[0], new_point[1]))
    elif(move_direction == 'down'):
        # print("down , point = (%d,%d)" % (new_point[0], new_point[1]) )
        # print("down sequence")
        # print_sequence(sequence)
        # print_matrix(puzzle_matrix)
        new_point[0] += 1
        # print("down , new_point = (%d,%d)" % (new_point[0], new_point[1]))
    elif(move_direction == 'left'):
        # print("left , point = (%d,%d)" % (new_point[0], new_point[1]) )
        # print("left sequence")
        # print_sequence(sequence)
        # print_matrix(puzzle_matrix)
        new_point[1] -= 1
        # print("left , new_point = (%d,%d)" % (new_point[0], new_point[1]))
    elif(move_direction == 'right'):
        # print("right sequence")
        # print_sequence(sequence)
        # print_matrix(puzzle_matrix)
        # print("right , point = (%d,%d)" % (new_point[0], new_point[1]) )
        new_point[1] += 1
        # print("right , new_point = (%d,%d)" % (new_point[0], new_point[1]))

    #Two points swap their coordinate in the puzzle matrix.
    puzzle_matrix[ new_point[0] ] [ new_point[1] ] , puzzle_matrix[ point[0] ] [point[1] ] \
    = puzzle_matrix[ point[0] ] [ point[1] ] , puzzle_matrix[ new_point[0] ] [ new_point[1] ]

    # print_matrix(puzzle_matrix)
    # print_matrix_to_sequence(puzzle_matrix)

    return puzzle_matrix
"""
This is a "heuristic function". 
This function will calculate the Manhattan distance between current state
(it can be imagined to a puzzle matrix) & goal state 
(it can be imagined to a puzzle matrix as well)
// 3 : row 
% 3 : column
"""
def cal_Manhattan_distance(current_sequence):
    sum = 0
    for i , value in enumerate(current_sequence):
        if value == '0': 
            continue
        current_state_row , current_state_column = i // 3 , i % 3
        #To calculate the coordinate of the sequence[0,1,2,3,4,5,6,7,8]
        goal_state_row , goal_state_column = int(value) // 3 , int(value) % 3   
        sum += abs(current_state_row - goal_state_row) + \
        abs(current_state_column - goal_state_column)
    
    return sum
"""
The following function all for the convenience of my functions testing and computing-
between sequence and matrix.
"""
def matrix_to_sequence(puzzle_matrix):
    sequence = []
    for i in range( len ( puzzle_matrix ) ):
        for j in range( len ( puzzle_matrix[0] ) ):
                sequence.append( puzzle_matrix[i][j] )
    return sequence

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

def print_sequence(sequence):
    print("current sequence: ")
    print("[" , end = '')
    for i in range( len ( sequence ) ):
        if i != len(sequence) - 1:
            print(sequence[i] , end = ' ')
        else : 
            print(sequence[i] , end = '')
    print("]")

def print_Node_data(node):
    print("the node at address: %s" %(node) )
    print("The count: %d" % node.count)
    print("The state: %s" % node.state)
    print("The scores: %d" % node.scores)
    print("The heuristic: %d" % node.heuristic)
    print("The cost: %d" % node.cost)
    print("The action: %s" % node.action)
    print("The parent_node: %s" % node.parent_node)

def print_priority_queue_path(priority_queue):
    for i , value in enumerate(priority_queue):
        print("move 0 to %s" % value.action)
if __name__ == "__main__" : 
    main()