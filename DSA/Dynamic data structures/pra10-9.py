n=int(input())
for i in range(n):
    N=int(input())
    k=int(input())
    t1=(N%k)/2
    t2=(N%k+k+1)/2
    if min(t1,t2)==t1:
        print(t1)
    else:print(t2)