from player import Player

NUM_SPACES = 39

class Property():
	"""Represents one property"""
	def __init__(self, name, position, cost, owner, rent):
		self.name = name
		self.position = position
		self.cost = cost
		self.owner = owner
		self.rent = rent

	def setOwner(self, owner):
		if property is Player:
			self.owner = property
		else:
			print("Could not add owner to property in setOwner. Argument not of type Player")
		

class Board():
	"""Board Object"""
	def __init__(self):
		# with open():
		for x in xrange(1, NUM_SPACES):
			pass
			
		