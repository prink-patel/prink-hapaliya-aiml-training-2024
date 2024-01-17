t=int(input())
n=int(input())
doll=[]
for i in range(n):
    x=int(input())
    doll.append(x)
doll.sort()
for i in range(0,n):
    if doll[i]!=doll[i+1]:
        print(doll[i+1])
        i=i+1
        break