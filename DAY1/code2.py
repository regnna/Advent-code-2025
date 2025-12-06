import sys
from collections import defaultdict,Counter

# D=sys.stdin.read()
# moves=D.splitlines()

import os


base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "..", "inputs", "input1.txt")

print (base, path)
with open(path,'r') as f:
    moves = f.read().splitlines()

m=50
p1=0
p2=0  # p1=0

for i in moves:
    z=int(i[1:len(i)])
    # print(i,m)
    s=i[0]
    for _ in range(z):
        if s=='L':
            m=(m-1+100)%100
        else:
            m=(m+1)%100
        if m==0:
            p2+=1
    if m==0:
        p1+=1
    # reset(z,i[0])
    
# print(d)
print(p1,p2)
