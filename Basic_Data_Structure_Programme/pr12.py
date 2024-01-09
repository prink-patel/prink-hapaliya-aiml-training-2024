# 12. Create a simulation program for the Hot Potato Game. You can develop with your ideas. Just take care of the following things:
# - At least one person must be removed from each round.
# - Display name in the console that the user has a hot potato.
# - Each user holds a potato for random seconds between 0.1 to 3.0.

# - Each round starts after 3 seconds of the previous elimination.
# - Each round stops at random seconds between 5 to 20.

# - Display the name of the winner.

import random
import time

def play_hot_potato(players):
    while len(players) > 1:
        print("Round starts!")
        time.sleep(3) 

        random_time = random.uniform(5, 20)  
        end_time = time.time() + random_time

        while time.time() < end_time and len(players) > 1:
            potato_player = random.choice(players)
            print(f"{potato_player} has the hot potato!")
            time = random.uniform(0.1, 3.0)
            time.sleep(time)
            remaining_players = players[:]
            remaining_players.remove(potato_player)
            players = remaining_players
            print(f"{potato_player} is out!")

        print("Round ends!")

    print(f"The winner is: {players[0]}")

players = ["ya", "se", "je", "le", "me"]

play_hot_potato(players)
