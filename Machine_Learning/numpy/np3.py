# Array Indexing & Selection

import numpy as np
print("Creating 2d-array :-")
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print("***************************")
print("\n")

print("Printing element 5 using indexing:-")
print(arr_2d[0][0]) # using indexing we can get element 5
print("Printing element 35 using indexing:-")
print(arr_2d[2,0])  # 2nd row 1st element
print("***************************")
print("\n")

print("Printing a matrix from arr_2d :-")
print(arr_2d[:2,1:]) # using slicing we can slice matrix 
print("***************************")
print("\n")

print("Creating 1-d array:-")
arr= np.arange(0,11)
print(arr)

print("Checking element of arr greater than 5:-")
bool_arr = arr>5
print(bool_arr)# it will print bool values
print("Displaying element of bool_arr:-")
print(arr[bool_arr])

