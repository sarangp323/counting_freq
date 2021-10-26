# Array Indexing
import numpy as np

print("Creating array:-")
arr = np.arange(0,11)

print("***********************")
print("Printing Element at specific index e.g index(8):-")
print(arr[8])
print("\n")

print("***********************")
print("Slicing at from index 1 to 5 :-")
print(arr[1:5])
print("\n")

print("***********************")
print("changing value of arr from index 0 to 5 to 100:-")
arr[0:5]=100
print(arr)
print("\n")

print("***********************")
print("Creating another array:-")
arr = np.arange(0,11)
slice_of_array = arr[0:6]
print("changing value of slice_of_array to 99 but this will affect original array:-")
slice_of_array[:] = 99
print("Slice of array :-",slice_of_array)
print("Original array :-",arr)
print("***********************")
print("\n")

# To overcome this we will create copy of arr
arr = np.arange(0,11)
print("Original array:-",arr)
print("Create a copy of arr:-")
arr_copy = arr.copy()
arr_copy[:]=100
print("After changing value off arr_copy:-")
print("Slice of array :-",arr_copy)
print("Original array :-",arr)


      
