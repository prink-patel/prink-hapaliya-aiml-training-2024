'''Devu has n weird friends. Its his birthday today, so they thought that this is the best
occasion for testing their friendship with him. They put up conditions before Devu that 
they will break the friendship unless he gives them a grand party on their chosen day.
Formally, ith friend will break his friendship if he does not receive a grand party on dith day.

Devu despite being as rich as Gatsby, is quite frugal and can give at most one grand party daily.
Also, he wants to invite only one person in a party. So he just wonders what is the maximum number
of friendships he can save. Please help Devu in this tough task !!

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
First line will contain a single integer denoting n.
Second line will contain n space separated integers where ith integer corresponds to the day dith as given in the problem.
Output
Print a single line corresponding to the answer of the problem.

Constraints
1 ≤ T ≤ 104
1 ≤ n ≤ 50
1 ≤ di ≤ 100'''
t = int(input())

while t != 0:
    n = int(input())
    d = list(map(int, input().split()))
    t-=1
    a=set(d)
    print(len(a))