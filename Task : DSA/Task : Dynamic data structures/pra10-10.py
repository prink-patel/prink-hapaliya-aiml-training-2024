'''
You are given a positive integer N and an array A of size N. There are N lists L1,L2…LN. Initially, Li=[Ai].

You can perform the following operation any number of times as long as there are at least 2 lists:
Select 2 (non-empty) lists Li and Lj (i≠j)
Append Lj to Li and remove the list Lj. Note that this means Lj cannot be chosen in any future operation.
Find the minimum number of operations required to obtain a set of lists that satisfies the following conditions:

The first element and last element of each list are equal.
The first element of all the lists is the same.
Print -1 if it is not possible to achieve this via any sequence of operations.
'''
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