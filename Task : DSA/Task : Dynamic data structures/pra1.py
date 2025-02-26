"""
Our Chef has some students in his coding class who are practicing problems. 
Given the difficulty of the problems that the students have solved in order, 
help the Chef identify if they are solving them in non-decreasing order of difficulty. 
That is, the students should not solve a problem with difficulty d1, and then later a 
problem with difficulty d2, where d1>d2.

Output “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
Each test case consists of 2 lines of input.
The first line contains a single integer N, the number of problems solved by the students
The second line contains N space-separate integers, the difficulty ratings of the problems attempted by the students in order.

Output Format
For each test case, output in a new line “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not. The output should be printed without the quotes.
Each letter of the output may be printed in either lowercase or uppercase. For example, the strings yes, YeS, and YES will all be treated as equivalent.

Constraints
1≤T≤100
2≤N≤100
1 ≤ difficulty of each problem ≤ 5000
"""
t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    t -= 1
    a=-1
    for i in range(n-1):
        different = d[0]
        if (d[i+1] - d[i]) < 0 :
            a=0
            break
    if a==0:
        print("No")
    else:
        print("Yes")

