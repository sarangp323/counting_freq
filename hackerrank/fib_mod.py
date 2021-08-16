def fibonacciModified(t1, t2, n):
    # Write your code here
	#creating list 
    k=[t1,t2]
    for i in range(2,n):
        k.append(k[-2]+(k[-1]**2)) #appending result to list
    return k[-1]




first_multiple_input = input().rstrip().split()

t1 = int(first_multiple_input[0])

t2 = int(first_multiple_input[1])

n = int(first_multiple_input[2])

result = fibonacciModified(t1, t2, n
print(result)
