import re
N=input()
def min(N):
    arr=re.split("[-]", N)
    li=[]
    for i in arr:
        arr2=re.split("[+]",i)
        li.append(sum(map(int,arr2)))
    tot=0
    tot+=li[0]
    for i in range(1, len(li)):
        tot-=li[i]
    return tot
print(min(N))