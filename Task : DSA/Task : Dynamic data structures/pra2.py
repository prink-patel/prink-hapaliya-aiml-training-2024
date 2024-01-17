
"""
Alice and Bob recently got into running, and decided to compare how much they ran on different days.

They each ran for N days — on the ith day, Alice ran Ai meters and Bob ran Bi meters.

On each day,
Alice is unhappy if Bob ran strictly more than twice her distance, and happy otherwise.
Similarly, Bob is unhappy if Alice ran strictly more than twice his distance, and happy otherwise.
For example, on a given day

If Alice ran 200 meters and Bob ran 500, Alice would be unhappy but Bob would be happy.
If Alice ran 500 meters and Bob ran 240, Alice would be happy and Bob would be unhappy.
If Alice ran 300 meters and Bob ran 500, both Alice and Bob would be happy.
On how many of the N days were both Alice and Bob happy?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three lines of input.
The first line of each test case contains a single integer N — the number of days.
The second line of each test case contains N space-separated integers A1,A2,…,AN — the distances run by Alice on the N days.
The third line of each test case contains N space-separated integers B1,B2,…,BN — the distances run by Bob on the N days.
Output Format
For each test case, output on a new line the number of days when both Alice and Bob were happy.

Constraints
1≤T≤1000
1≤N≤100
1≤Ai,Bi≤10^5
"""
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    count=0
# Your code goes here
    for i in range(n):
        if (a[i]*2) >= b[i] and a[i] <= (b[i]*2):
            count+=1
    print(count)