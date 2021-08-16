def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i)==1:
            return i



n = int(input().strip())

a = list(map(int, input().rstrip().split()))

result = lonelyinteger(a)
print(result)

