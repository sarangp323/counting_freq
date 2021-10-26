import numpy as np
import random
my_lst = [1,2,3]
print("cretaing array:")
arr = np.array(my_lst)
print(arr)
print("******************************")
print("\ncreating matrix:")
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(mat))
print("********************************")

print("\ncreating array from 1 to 10 using arange() func:-")
k=np.arange(1,10) #arange is used to return int in specific range
print(k)

print("********************************")
print("\nAdding Element to Array:-")
print("Array is:-",k)
new_arr = np.append(k,[4,5,7])
print(new_arr)
print("New Array is :-",new_arr)

print("******************************")
print("\ncreating array of zeros using zeros() func:-")
print(np.zeros(5))
print("\n",np.zeros((5,5)))
print("******************************")

print("\ncreating array of ones using ones() func:-")
print(np.ones((3,3)))
print("******************************")

print("\ncreating array using linspace:-")
print(np.linspace(0,5,10)) #Linspace is used to create array of equally spaces values
print(np.linspace(0,5,20)) # equally spaces 20 value b/w range
print("******************************")

print("\ncreating Identity matrix with eye():-")
print(np.eye(4))
print("******************************")

print("\ncreating array with random function b/w 0 and 1:-")
print(np.random.rand(5)) # create list on random value b/w 0 and 1
print(np.random.rand(5,5)) # create matrix on random value b/w 0 and 1
print("******************************")

print("\ncreating array of integer with random function b/w range using randint():-")
print(np.random.randint(1,100,10)) #create array of random 10 integers b/w range 1 to 100
print("******************************")

print("\nConverting a 1-d array to 2-d array using reshape func:-")
k=np.arange(0,25)
print(k)
print("\n")
print("2-d aaray:-")
reshape_array = k.reshape(5,5)


print(reshape_array)
print("******************************")

print("\n Max and Min function:-")
print("\ncreate random array:-")
arr = np.random.randint(1,100,10)
print(arr)

print("\nFinding max element using max():-")
print(f"Maximum element in array is {arr.max()}")

print("\n finding min element using min():-")
print(f"Minimum element in array is {arr.min()}")

print("********************************")

print("\nfinding location of max element using argmax():-")
print(f"Max element is present at {arr.argmax()} index")
print("********************************")

print("\nfinding location of min element using argmax():-")
print(f"Min element is present at {arr.argmin()} index")

print("********************************")

arr = np.array([2,5,7,8,6,5,3,2,0])
print("Array is:-",arr)

print("Finding indexes of 2 using where():-")
print(np.where(arr==2)) 



