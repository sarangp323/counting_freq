# Numpy Operations
import numpy as np
print("Creating array:-")
arr=np.arange(0,11)
print("Array is:- ", arr)

print("**************************")
print("\n")

print("Adding array:-")
print(arr+arr)
print("**************************")
print("\n")

print("Subtracting array:-")
print(arr-arr)
print("**************************")
print("\n")

print("Multiplying array:-")
print(arr*arr)

print("**************************")
print("\n")

print("Adding 100 to every element of arr:-")
print(arr+100)

print("**************************")
print("\n")

print("Subtracting 100 from every element of arr:-")
print(arr-100)

print("**************************")
print("\n")

print("Square Root of arr using sqrt():-")
print(np.sqrt(arr))
print("**************************")
print("\n")

print("Exponential of arr using exp():-")
print(np.exp(arr))

print("**************************")
print("\n")

print("Sin of arr using sin():-")
print(np.sin(arr))
print("**************************")
print("\n")

print("Cos of arr using cos():-")
print(np.cos(arr))

print("**************************")
print("\n")
print("Creating array:-")
arr1=np.arange(0,10)
arr2 = np.arange(11,21)
arr3=np.arange(22,32)
print("Array 1 is:- ", arr1)
print("Array 2 is:- ", arr2)

print("Joining arr1 and arr2:-")
print(np.concatenate((arr1,arr2)))

print("**************************")
print("\n")
print("Stacking:-")
print("Stacking along Column:-")
print(np.vstack((arr1,arr2)))

print("**************************")
print("\n")
print("Stacking:-")
print("Stacking along Depth:-")
print(np.dstack((arr1,arr2,arr3)))





