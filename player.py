from random import randrange
from board import *

class Player():

	def __init__(self, playerNumber, currPos, currPlace, color):
		self.playerNumber = playerNumber
		self.currPos = currPos
		self.currPlace = currPlace
		self.color = color
		self.money = 500
		self.properties = []
		self.numProperties = 0
		self.doublCount = 0

	def pay(self, amount):
		self.money = self.money + amount

	def charge(self, amount):
		if self.money - amount < 0:
			raise(Exception("Player" + str(self.playerNumber) +" has no more money."))
			
		self.money = self.money - amount

	def addProperty(self, property):
		""" USAGE: Property Object """
		if prop is not Property:
			print("Could not add property to player in addProperty. Argument not of type Property")

		self.properties.append(prop)

	def takeProperty(self, property):
		if prop is not Property:
			print("Could not remove property to player in takeProperty. Argument not of type Property")

		self.properties.remove(prop)

	def roll(self):
		return [randrange(1, 6), randrange(1, 6)]

	def setLocation(self, property):
		if property is not Property:
			print("Could not set current location on board in setLocation. Argument not of type Property")
			
                self.move(int(property.position))

	def move(self, num):
                print(self.currPos)
		if self.currPos + num <= NUM_SPACES:
			self.currPos = self.currPos + num
		else:
			self.currPos = (num - (NUM_SPACES - self.currPos))

	# def takeTurn(self):
	# 	roll = self.roll()
	# 	self.move(roll[0] + roll[1])

	def dispStr(self):
		st1 = """Position: {}\nMoney: {}\nProperties Owned: {}
		""".format(self.currPlace.name, self.money, self.numProperties)
		st2 = ""
		for prop in self.properties:
			st2 = st2 + prop.getInfo()

		st2 = st2 + "\n\n"

		return [st1, st2]

	def __str__(self):
		return """Player Object: 
		Number: {}
		Postition: {}
		Color: {}
		Money: {}
		Num Prop: {}\n""".format(self.playerNumber, self.currPos, self.color, self.money, self.numProperties)