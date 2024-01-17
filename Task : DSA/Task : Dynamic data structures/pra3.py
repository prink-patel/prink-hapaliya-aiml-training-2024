"""
You are given an array A of N integers.
Find the maximum sum of two distinct integers in the array.

Note: It is guaranteed that there exist at least two distinct integers in the array.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains single integer N — the size of the array.
The next line contains N space-separated integers, denoting the array A.

Output Format
For each test case, output on a new line, the maximum sum of two distinct integers in the array.

Constraints
1≤T≤1000
2≤N≤10^5
1≤Ai≤1000
The sum of N over all test cases does not exceed 2⋅10^5.
"""

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
# Your code goes here
    a.sort()
    max1=a[-1]
    for i in range(len(a)-1,0,-1):
        if max1 != a[i]:
            max1+=a[i]
            break
    print(max1)
