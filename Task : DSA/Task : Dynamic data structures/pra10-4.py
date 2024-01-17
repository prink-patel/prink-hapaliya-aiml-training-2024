"""
You are given an array A of length N. 
An element X is said to be dominant if the frequency of X in A is strictly greater than the frequency of any other element in the A.

For example, if A=[2,1,4,4,4] then 4 is a dominant element since its frequency is higher than the frequency of any other element in A.

Find if there exists any dominant element in A.

Input Format
The first line of input contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the size of the array A.
The second line of each test case contains N space-separated integers A1,A2,....AN denoting the array A.

Output Format
For each test case, output YES if there exists any dominant element in A. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

Constraints
1≤T≤500
1≤N≤1000
1≤Ai≤N
"""
t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    t-=1
    
    result={}
    for i in d:
        result[i]=d.count(i)
    min=1
    count=0
    for i in result:
        if min>1 and min==result[i]:
            count=0
        elif result[i]>min:
            min=result[i]
            count=i
    
    
    if min!=1 and count!=0:
        print("YES")
    else:
        print("NO")