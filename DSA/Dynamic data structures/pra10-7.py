# A Little Elephant and his friends from the Zoo of Lviv like candies very much.
# There are N elephants in the Zoo. The elephant with number K (1 ≤ K ≤ N) will be
# happy if he receives at least AK candies. There are C candies in all in the Zoo.
# The Zoo staff is interested in knowing whether it is possible to make all
# the N elephants happy by giving each elephant at least as many candies as
# he wants, that is, the Kth elephant should receive at least AK candies. Each
# candy can be given to only one elephant. Print Yes if it is possible and No otherwise.

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