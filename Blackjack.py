'''
Goal: Make a text-based game of blackjack using Python
'''

'''
Needs:
	deck of cards
	player's pot
'''


#1: Create a deck of 52 cards

#create a card class
class Card:
	def __init__(self,suit,face,value):
		
		self.suit = suit
		self.face = face
		self.value = value
	
	def __repr__(self):
		return f"{self.face} of {self.suit} is worth {self.value} points."


#create the identifiers of cards
suits = ['Spades','Clubs','Diamonds','Hearts']
faces = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


#create a deck to hold all 52 cards
deck = []

#populate the deck with the 52 cards
for suit in suits:
	for face in faces:
		card = Card(suit,face,values[face])
		#print to check
		#print(card)
		deck.append(card)

#print deck to check
#print(deck)


#2: Shuffle the deck
from random import shuffle
shuffle(deck)
print(deck)
#3: Ask the player for their bet

#4: Check player's bet against their pot

#5: Deal two cards to the dealer and two to the player

#6: Show only one of the dealer's cards

#7: Show both of the player's cards

#8: Ask the player to hit or stay

#9: if the player does not bust, would they like to hit again?

#10: Once the player stands, play the dealer's hand. Dealer hits until they beat the player or bust

#11: Determine the winner and adjust the player's pot accordingly

#12: ask the player if they'd like to play again