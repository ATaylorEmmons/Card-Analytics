import numpy as np;	

#A utility class to simulate card games

class Deck:
	
	
	#_replace = true means that a draw card is returned after beign drawn
	def __init__(self, _replace):
	
		self.cards = np.arange(1, 53);
		self.cardStack = np.arange(1, 53);
		self.replace = _replace;
		
		self.STANDARD_52 = [
			[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Hearts" ],
			[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Spades" ],
			[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Diamonds"],
			[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Clubs" ]	
		]
	
	
	def checkId(self, id):
		if id < 1 or id > 52:
			print("Id range must be 1 - 52 but id was: " + str(id));
			return False
		else:
			return True
	
	def translateId(self, id):

		if not self.checkId(id):
			return
			
		suite = "Error"
		rank = -1
		
		translated = divmod(id - 1, 13);
		
		#Suite is the string value that is last in the list
		suite = self.STANDARD_52[translated[0]][-1]
		rank = self.STANDARD_52[translated[0]][translated[1]]
		
		return (id, str(rank) + " of " + suite)
	
	def getSuite(self, id):
		if not self.checkId(id):
			return
			
		translated = divmod(id - 1, 13);
		return self.STANDARD_52[translated[0]][-1]
	
	def getRank(self, id):
		if not self.checkId(id):
			return
			
		translated = divmod(id - 1, 13);
		return self.STANDARD_52[translated[0]][translated[1]]
		
	def getColor(self, id):
		if not self.checkId(id):
			return
			
		if getRank(id) % 2 == 0:
			return (0, "Red");
		else:	
			return (1, "Black");
	
	def reset(self):
		self.cardStack = self.cards[:]
	
	def shuffle(self):
		self.cardStack = np.random.permutation(self.cards);
	
	def drawHand(self, count = 1):
		hand = []
		
		for i in range(count):
			hand.append(deck.draw())
	
	
	def draw(self, count = 1):
		
		top, self.cardStack = self.cardStack[0], self.cardStack[1:]
		return self.translateId(top);
		
	
	def print(self):
		print(self.cards)
		print(self.cardStack)
		

