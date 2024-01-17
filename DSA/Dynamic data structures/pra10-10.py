# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    d={}
    m=0
    l=input().split(' ')
    for j in l:
        if j in d:
            d[j]+=1
            if d[j]>=2 and d[j]>m:
                m=d[j]
        else:
            d[j]=1
            
    if len(d.keys())==1:
        print(0)
    elif m==0:
        print(-1)
    else:
        print(int(n-(m-2)-1))