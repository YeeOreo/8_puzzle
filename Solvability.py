"""
This is a 8-puzzle problem which seperated to 4 part
It's first part for following code
The first part is to check if this input value in the puzzle are solvable
The way is to count the disorder pair of all the input 
If the disorder pair is even, then this problem is solvable
Else this problem is not solvable

Usage:
Input the test times, first.
Then, input a string like:[X X X X X X X X X]
Parameter:
X is the number between 0 ~ 8, those presens the sequence of a puzzle state.
"""
def main():
    test_amount = int(input())       # The times for test
    for i in range(test_amount):
        sequence = input()  #The value for the 8-puzzle.
        new_sequence = string_handle(sequence) 
        # print(sequence)
        if isSolvable(new_sequence) == True:
            print("YES")
        else :
            print("NO")

# The String input will be like [X X X X X X X X X] 
# This function will eliminate the inputs like "[" , "]" , " " and "0". 
def string_handle(sequence):
    sequence = sequence.replace("[","")
    sequence = sequence.replace("]","")
    sequence = sequence.replace(" ","")
    sequence = sequence.replace("0","")
    return sequence

# If the problem is N-puzzle,and the N is not an even(is an odd)
# Then the disorder_count must plus the row of the empty tile(input likes "0") Before check if resovable
def empty_tile_index(sequence):
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

#To check this N-puzzle if solvable for the N is an even(Odd version not be written)
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

if __name__ == "__main__" : 
    main()