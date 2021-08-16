
def gamingArray(arr):
    # Write your code here
	# first way
    i=0
    bob=False
    k=max(arr)
    k_index=arr.index(k)
    while(k_index>=0):
        
        if i%2==0:
            arr=arr[:k_index]
            
            if len(arr)==0:
                return "BOB"
            k=max(arr)
            k_index=arr.index(k)
        else:
            arr=arr[:k_index]
            
            if len(arr)==0:
                return "ANDY"
            k=max(arr)
            k_index=arr.index(k)
        i+=1
	#second way
    c=0
    while(len(arr)>0):
        k=max(arr)
        k_index=arr.index(k)
        arr=arr[:k_index]
        c+=1
    return "ANDY" if c%2==0 else "BOB"
	#third way

    cnt=0
    mx=0
    for i in arr:
        if i>mx:
            mx=i
            cnt+=1
    return "ANDY" if cnt%2==0 else "BOB"
        
                
            
        


g = int(input().strip())

for g_itr in range(g):
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = gamingArray(arr)

    print(result)
