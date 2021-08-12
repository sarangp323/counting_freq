print("counting freq. of element in list")
print(" Different Ways:")
print("Taking list as input:")
s = list(map(int, input().split(" ")))
print("Using Dictionary")
# using traditional way
freq = {}
for i in s: #loop
    if i in freq: #checking element in dict
        freq[i]+=1 # if yes count +=1
    else:
        freq[i]=1
for k,v in freq.items():
    print(k,v)

# using short way
counter = {} #creating dict
for i in s:
    counter[i] = counter.get(0,1) +1
print(counter)

print("Using Counter")
f=[]
for v in sorted(counter.items()): #using counter 
    for i in range(v):
        f.append(k)
print(f)
        
        
    
