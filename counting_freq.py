print("counting freq. of element in list")
print(" Different Ways:")
print("Taking list as input:")
s = list(map(int, input().split(" ")))
print("Using Dictionary")
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for k,v in freq.items():
    print(k,v)

counter = {}
for i in s:
    counter[i] = counter.get(0,1) +1
print(counter)

print("Using Counter")
f=[]
for v in sorted(counter.items()):
    for i in range(v):
        f.append(k)
print(f)
        
        
    
