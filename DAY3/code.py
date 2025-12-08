import sys,os
from collections import defaultdict,Counter

# base= os.path.dirname(os.path.abspath(__file__))
# path= os.path.join(base,"input.txt")

# print(path)
# with open("./input.txt",'r') as f:
#     ranges= f.read()
# print(ranges)
# for i in ranges:
    # print(i)
base= os.path.dirname(os.path.abspath(__file__))
path= os.path.join(base,"..","inputs","input3.txt")

# print (base, path)

def val(c):
    q=0
    for i in range(0,len(c)-1):
        for j in range(i+1,len(c)):
            p=int(c[i])*10+int(c[j])
            if p>q:
                q=p
    # print("for ",c, " value ",q)
    return q
a=[]
with open(path,'r') as f:
    ids=f.read().splitlines()
x=0
for i in ids:
    x+=val(i)
print(x)