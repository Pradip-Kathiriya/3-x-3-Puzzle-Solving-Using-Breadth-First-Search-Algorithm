import numpy as np
from collections import deque
import time


###############################################
######### function defination #################
###############################################


# Define a data structure to store information about each node
# Data structure will store three information about node: Node array(3x3 matrix), its index and its parent's index
class Node:
    def __init__(self, node_array, node_index, parent_index):
        self.node_array = node_array
        self.node_index = node_index
        self.parent_index = parent_index

# function to find the index of 0 element in given array        
def zero_index (node_array):
    for i in range(len(node_array)):
        for j in range(len(node_array)):
            if node_array[i][j] == 0 :
               return i,j 

# function to move 0 in up direction
# if the zero is located in first row, it will return false as a boolean 
def moveUp(node_array,i,j):
    if i==0:
        return False, node_array
    else:
        node_temp = [row[:] for row in node_array]
        temp = node_temp[i-1][j]
        node_temp[i-1][j] = node_temp[i][j]
        node_temp[i][j] = temp
        return True, node_temp

# function to move 0 in down direction
# if the zero is located in third row, it will return false as a boolean 
def moveDown(node_array,i,j):
    if i==2:
        return False, node_array
    else: 
        node_temp = [row[:] for row in node_array]
        temp = node_temp[i+1][j]
        node_temp[i+1][j] = node_temp[i][j]
        node_temp[i][j] = temp
        return True, node_temp

# function to move 0 in left direction
# if the zero is located in first column, it will return false as a boolean 
def moveLeft(node_array,i,j):
    if j==0:
        return False, node_array
    else:
        node_temp = [row[:] for row in node_array]
        temp = node_temp[i][j-1]
        node_temp[i][j-1] = node_temp[i][j]
        node_temp[i][j] = temp
        return True, node_temp

# function to move 0 in right direction
# if the zero is located in third row, it will return false as a boolean 
def moveRight(node_array,i,j):
    if j==2:
        return False, node_array
    else:
        node_temp = [row[:] for row in node_array]
        temp = node_temp[i][j+1]
        node_temp[i][j+1] = node_temp[i][j]
        node_temp[i][j] = temp
        return True, node_temp

###############################################
######### initilize variables  ################
###############################################


node_index = 1                  # to store the index of the current node. initialize as 1 for first node
parent_index = 0                # to store the index of the parent of the current node. initialize as 0 for first node
visited_node = []               # array to store Node object(array, index and parent index) of each visited node
visited_node_array = []         # array to store node array (3x3 matrix) of each visited node
visited_node_index = []         # array to store node index of each visited node
visited_node_parent_index = []  # array to store parent index of each visited node
not_visited_node = deque([])    # array to store Node object(array, index and parent index) of each yet to visited node
goal_parent_index = 0           # initialize the parent index of goal node
initial_state = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]   # initialize the 3x3 matrix to store initial state of the puzzle
goal_state = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]      # initialize the 3x3 matrix to store goal state of the puzzle
final_path = []                 # array to store the final optimum path



####################################################################################
######### Taking input from user for initial state and goal state  #################
####################################################################################


# take input from user for initial state and store it in a variable initial_state
print("Enter initial state row-wise, Please press Enter key after adding each elements: ")    

for i in range(3):
    for j in range(3):
     initial_state[i][j] = int(input())

# take input from user for goal state and store it in a variable goal_state
print("Enter goal state row-wise, please press Enter key after adding each elements: ")

for i in range(3):
    for j in range(3):
     goal_state[i][j] = int(input())

start = time.time() 

#create node object for the fist node
n = Node(initial_state, node_index, parent_index)
not_visited_node.append(n) # append the first node object into yet to visited node list
node_index += 1 #increase the node index after creating node


################################################################
######### BFS implmentation for sudoku solving #################
################################################################


while True:

    n = not_visited_node.popleft() #pop out the first element from the yet to visited node list in FIFO order.
    
    visited_node.append(n)    # append the node object into visited node list
    
    visited_node_array.append(n.node_array)  # append the node array (3x3) into visited node array list
    visited_node_index.append(n.node_index)  # append the node index into visited node index array list
    visited_node_parent_index.append(n.parent_index)  # append the parent node index inot visited node parent index array list
    
    current_state = n.node_array
    print(current_state)
    
    # if current state is goal state,then goal state is found. Break out of the loop
    if current_state == goal_state:
        goal_parent_index = n.parent_index
        break
    
    # update the index of parents
    parent_index = n.node_index
    
    #find the index of 0 element in the current node
    i, j = zero_index(n.node_array)
    
    # call move left function to explore the next possible node
    bool, n_new = moveLeft(n.node_array,i,j)
    # if left movement is possible(bool is true) and new node is not visited yet, append new node in the yet to visit list        
    if (not n_new in visited_node_array) & (bool) :
        n_temp = Node(n_new, node_index, parent_index)
        not_visited_node.append(n_temp)
        node_index += 1
    
    # call move up function to explore the next possible node   
    bool, n_new = moveUp(n.node_array,i,j)
    # if up movement is possible(bool is true) and new node is not visited yet, append new node in the yet to visit list          
    if (not n_new in visited_node_array) & (bool) :
        n_temp = Node(n_new, node_index, parent_index)
        not_visited_node.append(n_temp)
        node_index += 1
        
    # call move right function to explore the next possible node 
    bool, n_new = moveRight(n.node_array,i,j)
    # if right movement is possible(bool is true) and new node is not visited yet, append new node in the yet to visit list          
    if (not n_new in visited_node_array) & (bool) :
        n_temp = Node(n_new, node_index, parent_index)
        not_visited_node.append(n_temp)
        node_index += 1
        
    # call move down function to explore the next possible node     
    bool, n_new = moveDown(n.node_array,i,j)
    # if down movement is possible(bool is true) and new node is not visited yet, append new node in the yet to visit list  
    if (not n_new in visited_node_array) & (bool) :
        n_temp = Node(n_new, node_index, parent_index)
        not_visited_node.append(n_temp)
        node_index += 1
        
        
#############################################################
######### Back tracking to find opimal path #################
#############################################################


# insert the goal position array(3x3 matrix) into final path array
final_path.insert(0,n.node_array)
index = np.inf #initilise the index variable to store the index of array used during back tracking
            
while True:

    #break the loop when you reach to initial state in back tracking
    if goal_parent_index == 0: 
        print("Path is found")
        break
    
    for i in range(len(visited_node)):
        if visited_node[i].node_index == goal_parent_index:
            index = i
            break
      
    # insert each parent into the final path 
    final_path.insert(0, visited_node[index].node_array)
    # update the goal parent index
    goal_parent_index = visited_node[index].parent_index          

end = time.time()
print('time taken:' + ' ' + str((end-start)) + ' ' + 'Seconds')  


################################################
######### Generating text file #################
################################################


# generate .txt file of optimal path
fh = open('nodePath.txt','w')
for i in range(len(final_path)):
    A = final_path[i]
    for j in range(3):
        for k in range(3):
            fh.write(str(A[k][j]) + ' ')
    fh.write('\n')

fh.close()

# generate .txt file of all the visited node
fh = open ('Nodes.txt', 'w')
for i in range(len(visited_node_array)):
    A = visited_node_array[i]
    for j in range(3):
        for k in range(3):
            fh.write(str(A[k][j]) + ' ')
    fh.write('\n')

fh.close()

# generate .txt file of node index and parent index of all the visited node
fh = open ('NodesInfo.txt', 'w')
fh.write('visited_node_index' + '  ' + 'visited_node_parent_index')
fh.write('\n')
for i in range(len(visited_node_index)):
        fh.write(str(visited_node_index[i]) + '                              ' + str(visited_node_parent_index[i]))
        fh.write('\n')

fh.close()
     





    