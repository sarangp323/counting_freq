
def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    cost=0
    c=0
    for i in prices:
        if cost+i<=k:
            cost+=i
            c+=1
    return c
            
        



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

prices = list(map(int, input().rstrip().split()))

result = maximumToys(prices, k)
print(result)
