#program to check whether a given number is a valid floating point number or not
import re

n=int(input())
l=[]
for i in range(n):
    l.append(input())
#compiling the regex
regdot=re.compile(r'^[+-]{0,1}[0-9]*\.[0-9]+$')
#loop for checking if the length of the floating point input is equal to the length of the output got from regex
#if yes then it is valid otherwise not
for j in l:
    ans=regdot.search(j)
    if ans == None:
        print("False")
    elif len(ans.group())==len(j):
        print("True")
    else:
        print("False")