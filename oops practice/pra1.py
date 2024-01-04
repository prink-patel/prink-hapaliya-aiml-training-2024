import random

class Cards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.cards = []

    def generate_deck(self):
        cards_obj = Cards()
        self.cards = [{'Suit': suit, 'Value': value} for suit in cards_obj.suits for value in cards_obj.values]

class Shuffle:
    def __init__(self, deck):
        self.deck = deck

    def shuffle_cards(self):
        random.shuffle(self.deck.cards)

    def pick_card(self):
        if not self.deck.cards:
            print("No more cards left in the deck.")
            return None
        return self.deck.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def pick_cards(self, shuffle_obj, num_cards):
        for _ in range(num_cards):
            card = shuffle_obj.pick_card()
            if card:
                self.hand.append(card)

    def calculate_points(self):
        values_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        total_points = sum(values_dict[card['Value']] for card in self.hand)
        return total_points

deck_obj = Deck()
deck_obj.generate_deck()

shuffle_obj = Shuffle(deck_obj)
shuffle_obj.shuffle_cards()

player1 = Player("Player-1")
player1.pick_cards(shuffle_obj, 5)
shuffle_obj.shuffle_cards()

player2 = Player("Player-2")
player2.pick_cards(shuffle_obj, 5)
shuffle_obj.shuffle_cards()

player3 = Player("Player-3")
player3.pick_cards(shuffle_obj, 5)
shuffle_obj.shuffle_cards()

players = [player1, player2, player3]
for player in players:
    print(f"{player.name} has cards: {[card['Value'] for card in player.hand]}")
for player in players:
    points = player.calculate_points()
    print(f"{player.name} has total points: {points}")

eligible_players = [player for player in players if any(card['Value'] in ['A', 'J', 'Q', 'K'] for card in player.hand)]

if eligible_players:
    winning_player = max(eligible_players, key=lambda player: player.calculate_points())
    print(f"\n{winning_player.name} is the winning player!")
else:
    print("\nNo eligible players. No winner.")
