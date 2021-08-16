
def luckBalance(k, contests):
    # Write your code here
    contests.sort(reverse=True)
    luck=0
    for i in contests:
        if i[1]==0:
            luck+=i[0]
        elif k>0:
            luck += i[0]
            k-=1
        else:
            luck-=i[0]
    return luck
        
    




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

contests = []

for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))

result = luckBalance(k, contests)

print(result)
