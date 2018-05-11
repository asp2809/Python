import re

n=int(input())
l=[]
for i in range(n):
    l.append(input())
regdot=re.compile(r'^[+-]{0,1}[0-9]*\.[0-9]+$')
for j in l:
    ans=regdot.search(j)
    if ans == None:
        print("False")
    elif len(ans.group())==len(j):
        print("True")
    else:
        print("False")