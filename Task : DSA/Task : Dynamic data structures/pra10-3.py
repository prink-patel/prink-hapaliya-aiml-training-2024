'''You are given an array A of size N. In one operation, you can do the following:
Select indices i and j (i≠j) and set Ai =Aj.
Find the minimum number of operations required to make all elements of the array equal.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N — the size of the array.
The next line contains N space-separated integers, denoting the array A.

Output Format
For each test case, output on a new line, the minimum number of operations required to make all elements of the array equal.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 2.105
1 ≤ Ai ≤ N
'''
from statistics import mode
t = int(input())

while t != 0:
    n = int(input())
    d = list(map(int, input().split()))
    t-=1
    a=mode(d)
    print(n - d.count(a))