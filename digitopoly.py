import sys

from PySide.QtGui import *
from PySide.QtCore import *

from ui_window import Ui_MainWindow

from player import Player
from board import *

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
		# self.button_nextPlayer.clicked.connect(self.getNextPlayer)
		# self.button_playerAction.clicked.connect(self.takeTurn)
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		reconnect(self.button_playerAction.clicked, self.takeTurn)
		
		

	# def connect_gameUi(self):
	# 	self.mainMenu.clicked.connect(self.returnToMain)

	def startGame(self):
		# self.gameUi(self)
		# self.connect_gameUi();
		self.frame_currentPlayerInfo.setVisible(1)
		self.button_fourPlayerStart.setVisible(0)

		self.board = Board()

		numPlayers = 4
		for x in range(0, numPlayers):
			player = Player(x, 0, self.board.properties[0], "255 255 255")
			self.players.append(player)


		self.getNextPlayer()

	def getNextPlayer(self):
		self.currPlayerNum = self.currPlayerNum + 1
		if self.currPlayerNum == len(self.players):
			self.currPlayerNum = 0
		# Update UI
		self.button_nextPlayer.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		self.button_playerAction.setEnabled(True)
		self.button_playerAction.setText("Roll Dice")
		reconnect(self.button_playerAction.clicked, self.takeTurn)

		# Update Player UI
		player = self.players[self.currPlayerNum]
		self.updatePlayerUI()


	def returnToMain(self):
		self.setupUi(self)
		self.connect_setupUi()

	def takeTurn(self):
		player = self.players[self.currPlayerNum]
		roll = player.roll()
		# Add In double counts self.doublCount = 0
		player.move(roll[0] + roll[1])
		player.currPlace = self.board.properties[player.currPos]
		print "Player {} moved to index {}.".format(player.playerNumber, player.currPos)

		# Update Player UI after Move
		self.updatePlayerUI()
		
		if player.currPlace.action == PROPERTY_SPACE:
			print str(player.currPlace)
			self.propertyHandle(player)
		elif player.currPlace.action == CHANCE_SPACE:
			self.chanceHandle(player)
		elif player.currPlace.action == BANK_SPACE:
			self.bankHandle(player)
		elif player.currPlace.action == RAILROAD_SPACE:
			self.railroadHandle(player)


		print roll

		print str(player)

	def propertyHandle(self, player):
		player = self.players[self.currPlayerNum]
		currentPlace = self.board.properties[player.currPos]
		if currentPlace.owner == None:
			print "Price: {}, Money:{}".format(currentPlace.price, player.money)
			if currentPlace.price <= player.money:
				self.button_playerAction.setText("Buy!")	
				reconnect(self.button_playerAction.clicked, (lambda: self.buyProperty(player, currentPlace)))
				self.button_nextPlayer.setEnabled(True)
				self.button_nextPlayer.setText("Pass")
				reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
			else:
				print "Player doesnt have enough money"
				self.button_playerAction.setEnabled(False)
				self.button_nextPlayer.setEnabled(True)
				reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)			

	def buyProperty(self, player, currentPlace):
		currentPlace.owner = player
		player.properties.append(currentPlace)
		player.numProperties = player.numProperties + 1
		player.charge(currentPlace.price)

		# Update UI
		self.updatePlayerUI()
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")


		
	def updatePlayerUI(self):
		player = self.players[self.currPlayerNum]
		self.label_currPlayerName.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo.setText(player.dispStr()[0])
		if len(player.properties) > 0:
			self.label_playerInfo2.setText(player.dispStr()[1])
		else:
			self.label_playerInfo2.setText("")

			



	def chanceHandle(self, player):
		pass

	def bankHandle(self, player):
		pass

	def railroadHandle(self, player):
		pass

# Helper Function for Disconnecting and Reconnecting Signal Handles
def reconnect(signal, newhandler=None, oldhandler=None):
    while True:
        try:
            if oldhandler is not None:
                signal.disconnect(oldhandler)
            else:
                signal.disconnect()
        except Exception:
            break
    if newhandler is not None:
        signal.connect(newhandler)


if __name__ == '__main__':
    currentApp = QApplication(sys.argv)
    currentForm = MainGame()

    currentForm.showFullScreen()
    currentApp.exec_()