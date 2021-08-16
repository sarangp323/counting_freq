def toys(w):
    # Write your code here
    w.sort()
    k=w[0]
    container=1
    for i in w:
        if i>k+4:
            k=i
            container+=1
    return container
        



n = int(input().strip())

w = list(map(int, input().rstrip().split()))

result = toys(w)
print(result)

