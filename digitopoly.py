import sys

from PySide.QtGui import *
from PySide.QtCore import *

from ui_window import Ui_MainWindow

from player import Player
from board import Board

class MainGame(QMainWindow, Ui_MainWindow):
	"""This is the Main Game Object"""
	def __init__(self, parent=None):
		super(MainGame, self).__init__(parent)
		self.setupUi(self)
		self.connect_setupUi()
		
		# Actions

		# Vars
		self.players = []
		self.board = None

	def connect_setupUi(self):
		self.fourPlayerStart.clicked.connect(self.startGame)

	# def connect_gameUi(self):
	# 	self.mainMenu.clicked.connect(self.returnToMain)

	def startGame(self):
		# self.gameUi(self)
		# self.connect_gameUi();
		numPlayers = 4
		for x in range(0, numPlayers):
			player = Player(x, 0, "255 255 255")
			self.players.append(player)

		self.board = Board()

		self.gameLoop()

	def returnToMain(self):
		self.setupUi(self)
		self.connect_setupUi()

	def gameLoop(self):
		pass
		# i = 0
		# while self.run:
		# 	player = self.players[i]
		# 	self.takeTurn(player)
		# 	i = i + 1
		# 	if i > 3:
		# 		i = 0

	def takeTurn(self, player):
		print "Player" + str(player) + " Taking Turn..."


			


if __name__ == '__main__':
    currentApp = QApplication(sys.argv)
    currentForm = MainGame()

    currentForm.showFullScreen()
    currentApp.exec_()