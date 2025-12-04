import os


base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "..", "inputs", "input1.txt")

print (base, path)
with open(path,'r') as f:
    lines = f.read().splitlines()
# print(lines)

i=0
for l in lines:
    if l[0]=='L':
        i+=1

print(i)