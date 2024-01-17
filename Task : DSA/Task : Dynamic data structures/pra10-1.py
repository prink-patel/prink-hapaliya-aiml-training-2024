"""Chef is fan of pairs and he likes all things that come in pairs.
 He even has a doll collection in which the dolls come in pairs.
 One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!!

Help chef find which type of doll is missing..

Input
The first line contains an integer T, the number of test cases.
The first line of each test case contains an integer N, the number of dolls.
The next N lines are the types of dolls that are left.

Output
For each test case, display the type of doll that doesn't have a pair, in a new line.

Constraints
1<=T<=10
1<=N<=100000 (10^5)
0<=type<=100000"""
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