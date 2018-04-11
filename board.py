#from player import *

NUM_SPACES = 39
GAME_OWNED_PROPERTY = 40
PROPERTY_SPACE = 0
CHANCE_SPACE = 1
BANK_SPACE = 2
RAILROAD_SPACE = 3
NOOP_SPACE = 4
COMMUNITY_CHEST_SPACE = 5
RAILROADS = [5,15,25,35]

class Property():
	"""Represents one property"""
	def __init__(self,position,name,action,price,rent,upRent,upCost,text,upText):
		self.position = position
		self.name = name
		self.price = int(price)
		self.rent = int(rent)
		self.upRent = int(upRent)
		try:
			self.upCost = int(upCost)
		except:
			pass			
		self.upgraded = False
		self.text = text
		self.upText = upText
		self.image = "images/test.png"
		
		if action == "0":
			self.action = PROPERTY_SPACE
			self.owner = None
		elif action == "1":
			self.action = CHANCE_SPACE
			self.owner = GAME_OWNED_PROPERTY
		elif action == "2":
			self.action = BANK_SPACE
			self.owner = GAME_OWNED_PROPERTY
		elif action == "3":
			self.action = RAILROAD_SPACE
			self.owner = None
		elif action == "5":
			self.action = COMMUNITY_CHEST_SPACE
			self.owner = GAME_OWNED_PROPERTY
		else:
			self.action = NOOP_SPACE
			self.owner = GAME_OWNED_PROPERTY

	def setOwner(self, owner):
		if owner is Player:
			self.owner = owner
		else:
			print("Could not add owner to property in setOwner. Argument not of type Player")

	def getInfo(self):
		return """Name: {}\nPrice{}\nRent:{}""".format(self.name, self.price, self.rent)

	def __str__(self):
		return """Name: {}\nPrice: {}\nRent: {}\nOwner: {}\nAction: {}
		""".format(self.name, self.price, self.rent, self.owner, self.action)

		

class Board():
	"""Board Object
	Attributes:
		self.properties: a list containing each property object.
	"""
	def __init__(self):
		self.properties = []
		self.chanceCards = []
		self.communityChestCards = []
                with open("Properties.csv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines[1:]:
                        line = line.split(",")
                        position = line[0]
			name = line[1]
			action = line[2]
			try:
				price = int(line[3])
			except:
				price = None
			rent = line[4]
			upRent = line[5]
			upCost = line[6]
			text = line[7]
			upText = line[8]
			self.properties.append(Property(position,name,action,price,rent,upRent,upCost,text,upText))
		with open("Cards - ChanceTest.csv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines:
                        line = line.split(",")
                        text = line[0]
			location = line[1]
			self.chanceCards.append(ChanceCards(text,location))
		with open("Cards - CommunityChest Test.csv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines:
                        line = line.split(",")
                        text = line[0]
			amount = line[1]
			self.communityChestCards.append(CommunityChestCards(text,amount))


class ChanceCards():
        def __init__(self, text, location):
                self.text = text
                self.location = location
class CommunityChestCards():
        def __init__(self, text, amount):
                self.text = text
                self.amount = amount
                
if __name__ == "__main__":
        board = Board()
        prop = board.properties[0]
        print(prop.owner)
