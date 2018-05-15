import re

n=int(input())
l=[]
ans=[]
for i in range(n):
    l.append(input())
reg1=re.compile(r'#([a-f0-9]{6}|[a-f0-9]{3})', re.IGNORECASE)
for j in l:
    if len(reg1.findall(j)) == 1:
        p=reg1.findall(j)
        length=len(p[0])+1
        length2=len(p[0])+3
        linelen=len(j)
        # print(linelen)
        if linelen != length and linelen != length2:
           ans+=reg1.findall(j)
    else:
        ans+=reg1.findall(j)
for k in ans:
    print('#' + k)