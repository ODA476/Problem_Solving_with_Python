"""
**4.24 (Game: pick a card ) Write a program that simulates picking a card from a deck of
52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
"""
import random

# Generate the rank >> (integer between 1, 13)
rank = random.randint(1, 13)

# now, I want to give each rank his name
if rank == 1:
    rank_name = 'Ace'
elif 2 <= rank <= 10:
    rank_name = str(rank)
elif rank == 11:
    rank_name = 'Jack'
elif rank == 12:
    rank_name = 'Queen'
else:
    rank_name = 'King'

# generate the suit >> (I assume it is integer between 1, 4)
suit = random.randint(1, 4)

# give each suit his name
if suit == 1:
    suit_name = 'Clubs'
elif suit == 2:
    suit_name = 'Diamonds'
elif suit == 3:
    suit_name = 'Hearts'
else:
    suit_name = 'Spades'

# display result
print(f'The card you picked is the {rank_name} of {suit_name}')
