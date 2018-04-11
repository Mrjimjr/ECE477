#from player import *

NUM_SPACES = 40
GAME_OWNED_PROPERTY = 40
PROPERTY_SPACE = 0
CHANCE_SPACE = 1
BANK_SPACE = 2
RAILROAD_SPACE = 3
NOOP_SPACE = 4

class Property():
	"""Represents one property"""
	def __init__(self,position,name,action,price,rent,upRent,upCost,text,upText):
		self.position = position
		self.name = name
		self.price = int(price)
		self.rent = int(rent)
		self.upRent = int(upRent)
		self.upCost = int(upCost)
		self.text = text
		self.upText = upText
		
		if action == "0":
                        self.action = PROPERTY_SPACE
                        self.owner = ""
                elif action == "1":
                        self.action = CHANCE_SPACE
                        self.owner = GAME_OWNED_PROPERTY
                elif action == "2":
                        self.action = BANK_SPACE
                        self.owner = GAME_OWNED_PROPERTY
                elif action == "3":
                        self.action = RAILROAD_SPACE
                        self.owner = ""
                else:
                        self.action = NOOP_SPACE
                        self.owner = GAME_OWNED_PROPERTY

	def setOwner(self, owner):
		if owner is Player:
			self.owner = owner
		else:
			print("Could not add owner to property in setOwner. Argument not of type Player")
		

class Board():
	"""Board Object
	Attributes:
		self.properties: a list containing each property object.
	"""
	def __init__(self):
		self.properties = []
		self.chanceCards = []
                with open("Properties.csv","r") as myFile:
                        lines = myFile.readlines()
                for line in lines[1:]:
                        line = line.split(",")
                        position = line[0]
			name = line[1]
			action = line[2]
			price = line[3]
			rent = line[4]
			upRent = line[5]
			upCost = line[6]
			text = line[7]
			upText = line[8]
			self.properties.append(Property(position,name,action,price,rent,upRent,upCost,text,upText))

class ChanceCards():
        def __init__(self, text, amount):
                self.text = text
                self.amount = amount
                
if __name__ == "__main__":
        board = Board()
        prop = board.properties[0]
        print(prop.owner)
