from player import *

NUM_SPACES = 39

class Property():
	"""Represents one property"""
	def __init__(self, name, position, cost, owner, rent):
		self.name = name
		self.position = position
		self.cost = cost
		self.rent = rent
		self.owner = owner

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
		# with open():
		for x in range(1, NUM_SPACES):
			name = "name"
			position = x
			cost = None
			rent = None
			owner = None
			self.properties.append(Property(name, position, cost, owner, rent))
			
		