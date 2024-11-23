import itertools

# Exercises
# 1. Write a generator that generates prime numbers in a specified range. You can make use of your solution to exercise 3 from day 8 as a starting point.

# 2. Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.

# names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)

# 3. Write a small program to deal cards for a game of Texas Hold'em. The order of the deal is as follows:

# The deck is shuffled.
# One card is handed to each player in order.
# A second card is handed to each player order.
# Then comes the more complicated part of the deal.

# First, the top card of the deck is discarded. This is called the burn.
# Three cards are then placed in the centre of the table, which is called the flop.
# Another card is burned, meaning we discard another card from the top of the deck.
# We add another card to the centre, which is called the turn.
# We burn another card.
# Finally, there's the river, where a fifth and final card is added to the centre.
# The desired output for the program is something like this:

# How many players are there? 2

# Player 1 was dealt: (4, hearts), (4, clubs)
# Player 2 was dealt: (9, clubs), (jack, diamonds)

# The flop: (jack, clubs), (4, diamonds), (king, spades)
# The turn: (8, hearts)
# The river: (ace, hearts)

# As the example would indicate, the program should accept a variable number of players. There must be at least 2 players, and no more than 10.

# After the flop, the turn, and the river there's usually a round of betting, so if you want to extend this exercise, you may want to give the user the option to pause at each of these points.

# Hint: We can shuffle cards using the random.shuffle method. This shuffles a sequence in-place, which means it modifies the original sequence. We can then create an iterator from that sequence using iter to make is easy for us to retrieve cards one at a time.

# You can find documentation for random.shufflehere.

# 1.

c = itertools.cycle(range(1, 101))
print(next(c))
print(next(c))
print(next(c))

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
g_names = (name.title().strip() for name in names)

print(next(g_names))

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = ((rank, suit) for rank in ranks for suit in suits)


