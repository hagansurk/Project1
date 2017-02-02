import random
import unittest

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


# Class Hand: Represents a hand of cards for a game, with basic functionality
# Functionality available: Number of cards attribute
# Methods: Can place a card out of the hand, add a card to the hand that is not a duplicate, find all suits available, find all ranks available, look for a specific card in the hand and return it if there
class Hand(object): 
	def __init__(self,deck_to_use,num_cards=5): # Constructor
		self.deck = deck_to_use # Needs a deck
		self.cards_in_hand = [] 
		for i in range(num_cards):
			self.cards_in_hand.append(self.deck.pop_card(i))

	def place_card(self,i=0):
		return self.cards_in_hand.pop(i) # Basically the same as pop_card from the deck, but referencing the HAND's cards

	def get_suits_available(self): # Returns list of all the suits that are in the hand
		suits = []
		for c in self.cards_in_hand:
			if c.suit not in suits:
				suits.append(c.suit)
		return suits

	def get_ranks_available(self): # Returns list of all the ranks that are in the hand
		ranks = []
		for c in self.cards_in_hand:
			if c.rank not in ranks:
				ranks.append(c.rank)
		return ranks

	def specific_card(self,suit,rank):
		card_strs = []
		ind = 0
		for c in self.cards_in_hand:
			if c.suit == suit and c.rank == rank:
				return self.place_card(ind) # If find the card in the hand, get rid of that card from the hand and return it from this method
			ind = ind + 1
		return None # if there is none such card in the hand, return None value
		
	def add_card(self,card): # add card to hand (if there is no identical one, assuming working with 1 deck here)
		card_strs = []
		for c in self.cards_in_hand:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards_in_hand.append(card)

	def __str__(self):
		total = []
		for card in self.cards_in_hand:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

#### Functions for games ####

# Function that plays an altered version of the game of War when invoked.
def play_war_game(testing=False):
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

## Below this line, indented beneath it, goes function invocations, any code you want to run when you run this file.
if __name__ == "__main__":

	print("Test code here!\n")
	## The following is code to try out functionality of the class Hand. Uncomment the following lines to try it out. Note that each line depends on the former lines!

	# deck_to_play = Deck() # Create a deck
	# deck_to_play.shuffle() # Shuffle the deck!
	# single_hand = Hand(deck_to_play,num_cards=5) # Deal one hand of 5 cards
	# print(single_hand) # Print the hand to view it
	# print("\n\n\n") # Print new lines, just for clarity


########### TESTS SHOULD GO BELOW THIS LINE ###########

# INCLUDE YOUR TESTS FROM HW2 HERE.
class test(unittest.TestCase):
	def test_face_card(self):
		s = Card(0, 12)
		self.assertEqual(s.rank, "Queen")
		p = Card(0, 1)
		self.assertEqual(p.rank, "Ace")
		q = Card(0, 3)
		self.assertEqual(q.rank, 3)
	def test_suit(self):
		a = Card(1)
		self.assertEqual(a.suit, "Clubs")
		b = Card(2)
		self.assertEqual(b.suit, "Hearts")
		c = Card()
		self.assertEqual(c.suit_names, ["Diamonds","Clubs","Hearts","Spades"])
	def test_card_string(self):
		c = Card(2, 7)
		self.assertEqual(c.__str__(), "7 of Hearts")
	def test_deck(self):
		c = Deck()
		self.assertEqual(len(c.cards), 52)
		d = Deck()
		e = d.pop_card(-1)
		self.assertEqual(type(e), type(Card()))
	def test_war(self):
		s = play_war_game(testing = True)
		self.assertEqual(type(s), tuple)
		self.assertEqual(len(s), 3)
		self.assertEqual(type(s[0]), str)
		p1 = Deck()
		player_1 = p1.cards
		p2 = Deck()
		player_2 = p2.cards
		self.assertEqual(len(player_1), len(player_2), "To test if the deck sizes are the same.")
	def test_rank(self):
		q = Card()
		self.assertEqual(q.rank_levels, [1,2,3,4,5,6,7,8,9,10,11,12,13], "to test if the code accesses the ranking list correctly")

## Add tests, as described in instructions.
## Here is a sample.
class HandClassTests(unittest.TestCase):
	def test_add_card(self):
		d = Deck()
		h = Hand(d) # default number of cards
		num = len(h.cards_in_hand) # length of the cards list in the hand
		new_card = d.pop_card() # pop another card off the deck
		h.add_card(new_card) # invoke add_card method with the card that we popped off the deck
		self.assertEqual(len(h.cards_in_hand),num+1) # Testing that the new number of cards in the hand is equal to the old number plus 1
	# Add more here!
	def test_type_suits(self):
		deck = Deck()
		hand = Hand(deck)
		hand.get_suits_available
		card = Card()
		self.assertEqual(type(hand.cards_in_hand), type(card.suit_names))
	def test_hand_constructor(self):
		deck = Deck()
		hand = Hand(deck)
		length = len(hand.cards_in_hand)
		self.assertEqual(length, 5)
		hand1 = Hand(deck, num_cards = 7)
		length1 = len(hand1.cards_in_hand)
		self.assertEqual(length1, 7)
	def test_place_card_method(self):
		deck = Deck()
		hand = Hand(deck)
		hand2 = Hand(deck)
		num = len(hand.cards_in_hand)
		hand2.place_card(i=0)
		self.assertEqual(len(hand2.cards_in_hand), num-1, "Testing the place card method of class Hand")
		new_card = Card()
		self.assertEqual(type(hand.place_card(i=0)), type(new_card), "testing the add_card method of class Hand")
	def test_specific_card(self):
		d = Deck()
		hand = Hand(d)
		e = hand.specific_card(3, 13)
		self.assertEqual(e, None)
	def test_string_hand(self): 
		d = Deck()
		hand = Hand(d)
		self.assertEqual(type(hand.__str__()), str)
	def test_type_rank(self):
		d = Deck()
		hand = Hand(d)
		hand.get_ranks_available
		c = Card()
		self.assertEqual(type(hand.cards_in_hand), type(c.rank_levels))

		
		

		# Hints to help come up with tests:
## - Create a Deck instance in each method where you want to test an instance of class Hand, because you need a Deck instance to create a Hand instance!
## - To test the Hand constructor, you may want to test that the Hand class creates a hand with 3 cards if you pass in a Deck instance to the constructor, and use the default num_cards.
## - You should also test that if you pass in a specific number of cards to the Hand class constructor, it creates an instance of class Hand with that specific number of cards! Gotta be sure that part of the Hand class constructor (__init__ method) works correctly.



#############

unittest.main(verbosity=2) 