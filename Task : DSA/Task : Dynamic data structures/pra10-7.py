'''Problem
Little Elephant likes lemonade.

When Little Elephant visits any room, he finds the bottle of the lemonade in that
room that contains the greatest number of litres of lemonade and drinks it all.

There are n rooms (numbered from 0 to n-1), each contains Ci bottles. Each bottle
has a volume (in litres). The first room visited by Little Elephant was P0-th,
 the second - P1-th, ..., the m-th - Pm-1-th room. Note that Little Elephant may visit a room more than once.

Find for Little Elephant the total volume of lemonade he has drunk.

Input
First line of the input contains single integer T - the number of test cases.
T test cases follow. First line of each test case contains pair of integers n and 
m. Second line contains m integers separated by a single space - array P. Next n 
lines describe bottles in each room in such format: Ci V0 V1 ... VCi-1,
where V is the list of volumes (in liters) of all bottles in i-th room.

Output
In T lines print T integers - the answers for the corresponding test cases.

'''
def total(n, m, P, rooms):
    total_volume = 0
    
    for i in range(m):
        room_ind = P[i]
        bottles = rooms[room_ind][1:]
        if len(bottles)>=1:
            max_volume = max(bottles)
            rooms[room_ind].remove(max_volume)
            total_volume += max_volume
    
    return total_volume

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    P = list(map(int, input().split()))
    
    rooms = [list(map(int, input().split())) for _ in range(n)]
    
    result = total(n, m, P, rooms)
    print(result)