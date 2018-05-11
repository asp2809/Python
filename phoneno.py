#program to validate phone numbers
import re

n=int(input())
l=[]
for i in range(n):
    in1=input()
    l.append(in1)
#combiling the regex
reg1=re.compile(r'(9|8|7)\d{9}')
ans=[]
#loop for checking if the regex length and the length of the input value are equal or not
#if they are equal then only it is a valid mobile number otherwise not
for j in l:
    if reg1.search(j) == None:
        print("NO")
    # ans.append(reg1.search(j).group())
    elif len(reg1.search(j).group())==len(j):
        print("YES")
    else:
        print("NO")   