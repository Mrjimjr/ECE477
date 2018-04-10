from random import randrange
from board import *

class Player():

	def __init__(self, playerNumber, currPos, color):
		self.playerNumber = playerNumber
		self.currPos = currPos
		self.color = color
		self.money = 0
		self.properties = []
		self.numProperties = 0

	def pay(self, amount):
		self.money = self.money + amount

	def charge(self, amount):
		if self.mone - amount < 0:
			raise(Exception("Player" + self.playerNumber +" has no more money."))
			
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
		if prop is not Property:
			print("Could not set current location on board in setLocation. Argument not of type Property")

		self.currPos = prop

	def move(self, num):
		if self.currPos + num <= NUM_SPACES:
			self.currPos = self.currPos + num
		else:
			self.currPos = (num - (NUM_SPACES - self.currPos))

	# def takeTurn(self):
	# 	roll = self.roll()
	# 	self.move(roll[0] + roll[1])

	def __str__(self):
		return """Player Object: 
		Number: {}
		Postition: {}
		Color: {}
		Money: {}
		Num Prop: {}""".format(self.playerNumber, self.currPos, self.color, self.money, self.numProperties)