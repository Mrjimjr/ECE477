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
		self.currPlayerNum = -1
		self.board = None

	def connect_setupUi(self):
		self.button_fourPlayerStart.clicked.connect(self.startGame)
		self.frame_currentPlayerInfo.setVisible(0)


		# Actually in gameUi:
		self.button_nextPlayer.clicked.connect(self.getNextPlayer)
		self.button_movePlayer.clicked.connect(self.takeTurn)
		

	# def connect_gameUi(self):
	# 	self.mainMenu.clicked.connect(self.returnToMain)

	def startGame(self):
		# self.gameUi(self)
		# self.connect_gameUi();
		self.frame_currentPlayerInfo.setVisible(1)
		self.button_fourPlayerStart.setVisible(0)


		numPlayers = 4
		for x in range(0, numPlayers):
			player = Player(x, 0, "255 255 255")
			self.players.append(player)

		self.board = Board()

		self.getNextPlayer()

	def getNextPlayer(self):
		self.currPlayerNum = self.currPlayerNum + 1
		if self.currPlayerNum == len(self.players):
			self.currPlayerNum = 0

		# Update UI


	def returnToMain(self):
		self.setupUi(self)
		self.connect_setupUi()

	def takeTurn(self):
		player = self.players[self.currPlayerNum]
		self.label_currPlayerName.setText("Player {}:".format(player.playerNumber))
		roll = player.roll()
		print roll

		print str(player)




if __name__ == '__main__':
    currentApp = QApplication(sys.argv)
    currentForm = MainGame()

    currentForm.showFullScreen()
    currentApp.exec_()