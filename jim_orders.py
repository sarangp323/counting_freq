
def jimOrders(orders):
    # Write your code here
    ordered = sorted(enumerate(orders,1))
    #return ordered
    j=[]
    for order in ordered:
        time = sum(order[1])
        j.append((time,str(order[0])))
    j.sort()
  
        
    
    serve,cust = map(list,zip(*j))
    return " ".join(cust)
        
    



n = int(input().strip())

orders = []

for _ in range(n):
    orders.append(list(map(int, input().rstrip().split())))

result = jimOrders(orders)

print(result)
