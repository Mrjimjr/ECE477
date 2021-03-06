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
	def __init__(self,position,name,action,price,rent,upRent,upCost,LEDs, description,rentText, upText):
		self.position = int(position)
		self.name = name
		self.price = int(price)
		self.rent = int(rent)
		self.upRent = int(upRent)
		try:
			self.upCost = int(upCost)
		except:
			pass			
		self.upgraded = False
		self.description = description
		self.rentText = rentText
		self.upText = upText
		# self.LEDs = []
		self.LEDs = LEDs
		self.image = "images/tiles/{}.png".format(self.position + 1)
		self.spotImage = "images/spotImages/{}.png".format(self.position + 1)
		
		
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
		return """Name: {}\nPrice: {}\nRent: {}""".format(self.name, self.price, self.rent)

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
                with open("Properties.tsv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines[1:]:
                        LEDs = []
                        line = line.split("\t")
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
			LEDs = line[7].split(",")
			description = line[8]
			rentText = line[9]
			upText = line[10]
			self.properties.append(Property(position,name,action,price,rent,upRent,upCost,LEDs,description,rentText, upText))
		with open("Cards - ChanceTest.tsv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines:
                        line = line.split("\t")
                        text = line[0]
			location = line[1]
			description = line[2]
			
			self.chanceCards.append(ChanceCards(text,location, description))
		with open("Cards - CommunityChest Test.tsv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines:
                        line = line.split("\t")
                        text = line[0]
			amount = line[1]
			description = line[2]
			self.communityChestCards.append(CommunityChestCards(text,amount, description))


class ChanceCards():
        def __init__(self, text, location, description):
                self.text = text
                self.location = location
                self.description = description
                
class CommunityChestCards():
        def __init__(self, text, amount, description):
                self.text = text
                self.amount = amount
                self.description = description
                
if __name__ == "__main__":
        board = Board()
        prop = board.properties[0]
        print(prop.owner)
