'''
find an integer X such that the value of F(X) = (X mod K) × ((N - X) mod K) is the maximum, where mod denotes the modulo operator.

Input:

The first line contains an integer T, the number of test cases.
Each test case has a single line with two integers N and K.
Output:

For each test case, print a single integer X (0 ≤ X ≤ N) such that F(X) is maximized.
If there are multiple answers, any of them can be printed.
Constraints:

1 ≤ T ≤ 10^5
0 ≤ N ≤ 10^9
1 ≤ K ≤ 10^9
'''

n=int(input())
for i in range(n):
    N=int(input())
    k=int(input())
    t1=(N%k)/2
    t2=(N%k+k+1)/2
    if min(t1,t2)==t1:
        print(t1)
    else:print(t2)