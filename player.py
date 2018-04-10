import random
from board import Board, Property

class Player():

	def __init__(self):
		self.playerNumber = None
		self.money = 0
		self.properties = []
		self.numProperties = []
		self.currPos = None
		self.color = None

	def pay(self, amount):
		self.money = self.money + amount

	def charge(self, amount):
		if self.mone - amount < 0:
			raise(Exception("Player" + self.playerNumber +" has no more money."))
			
		self.money = self.money - amount

	def addProperty(self, property):
		""" USAGE: Property Object """
		if property is not Property:
			print("Could not add property to player in addProperty. Argument not of type Property")

		self.properties.append(property)

	def takeProperty(self, property):
		if property is not Property:
			print("Could not remove property to player in takeProperty. Argument not of type Property")

		self.properties.remove(property)

	def roll(self):
		return [randrange(1, 6), randrange(1, 6)]

	def setLocation(self, property):
		if property is not Property:
			print("Could not set current location on board in setLocation. Argument not of type Property")

		self.currPos = property

	def move(self, num):
		if self.currPos + num <= NUM_SPACES:
			self.currPos = self.currPos + num
		else:
			self.currPos = (num - (NUM_SPACES - self.currPos))

	def takeTurn(self):
		roll = self.roll()
		self.move(roll[0] + roll[1])


		

