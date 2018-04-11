import sys

from PySide.QtGui import *
from PySide.QtCore import *
import random

from ui_window import Ui_MainWindow
from ui_propertyView import Ui_propertyView
from ui_detailView import Ui_detailView

from player import Player
from board import *

class DetailView(QMainWindow, Ui_detailView):
	"""This is the Property Viewer Object"""
	def __init__(self, property, player, parent=None):
		super(DetailView, self).__init__(parent)

		# Vars
		self.property = property
		self.player = player

		# Update UI
		self.setupUi(self)
		self.displayDetail()

		# Connect Buttons
		reconnect(self.button_closeDetail.clicked, self.close)

	def updatePlayerUI(self):
		player = self.player
		self.label_currPlayerName_2.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo_2.setText(player.dispStr()[0])
		self.button_closeDetail.setEnabled(True)

	def displayDetail(self):
		pass

class PropertyViewer(QMainWindow, Ui_propertyView):
	"""This is the Property Viewer Object"""
	def __init__(self, player, parent=None):
		super(PropertyViewer, self).__init__(parent)

		# Vars
		self.player = player

		self.detail_window = None
		
		# Update UI
		self.setupUi(self)
		self.updatePlayerUI()

		self.propButtons = [self.button_pro_1, self.button_pro_2, self.button_pro_3, self.button_pro_4, self.button_pro_5, self.button_pro_6, self.button_pro_7, self.button_pro_8, self.button_pro_9, self.button_pro_10, self.button_pro_11, self.button_pro_12, self.button_pro_13, self.button_pro_14, self.button_pro_15, self.button_pro_16, self.button_pro_17, self.button_pro_18, self.button_pro_19, self.button_pro_20, self.button_pro_21, self.button_pro_22, self.button_pro_23, self.button_pro_24]
		self.rrButtons = [self.button_rr_1, self.button_rr_2, self.button_rr_3, self.button_rr_4]
		
		self.displayProps()

		# Connect Buttons
		reconnect(self.button_closeProperties.clicked, self.close)

	def updatePlayerUI(self):
		player = self.player
		self.label_currPlayerName_2.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo_2.setText(player.dispStr()[0])
		self.button_closeProperties.setEnabled(True)

	def displayProps(self):
		player = self.player
		props = player.properties

		for btn in self.propButtons:
			btn.setVisible(True)
			btn.setEnabled(False)

		for btn in self.rrButtons:
			btn.setVisible(True)
			btn.setEnabled(False)

		btnCnt = 0
		rrCnt = 0
		for prop in props:
			if prop.action == RAILROAD_SPACE:
				btnCnt = btnCnt + 1
				btn = self.propButtons[btnCnt]
				
				icon = QPixmap(prop.image);
				btn.setIcon(QIcon(icon))
				btn.setText(prop.name)
				btn.setEnabled(True)
				btn.setVisible(True)
				reconnect(btn.clicked, (lambda: self.propDetailOpen(prop, player)))
			else:
				print "RAILROAD"
				rrCnt = rrCnt + 1
				btn = self.rrButtons[rrCnt]

				icon = QPixmap(prop.image);
				btn.setIcon(QIcon(icon))
				btn.setText(prop.name)
				btn.setEnabled(True)
				btn.setVisible(True)
				reconnect(btn.clicked, (lambda: self.propDetailOpen(prop, player)))

	def propDetailOpen(self, prop, player):
		self.detail_window = DetailView(prop, self)
		self.detail_window.showFullScreen()


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

		# Property UI
		self.property_window = None

	def connect_setupUi(self):
		self.button_fourPlayerStart.clicked.connect(self.startGame)
		self.frame_currentPlayerInfo.setVisible(0)


		# Actually in gameUi:
		# self.button_nextPlayer.clicked.connect(self.getNextPlayer)
		# self.button_playerAction.clicked.connect(self.takeTurn)
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		reconnect(self.button_playerAction.clicked, self.takeTurn)
		reconnect(self.button_showProperties.clicked, self.openPropertyViewer)
		
		
	def updatePlayerUI(self):
		player = self.players[self.currPlayerNum]
		self.label_currPlayerName.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo.setText(player.dispStr()[0])
		if len(player.properties) > 0:
			self.button_showProperties.setEnabled(True)
		else:
			self.button_showProperties.setEnabled(False)

	def openPropertyViewer(self):
		player = self.players[self.currPlayerNum]
		print "Request to open Property Viewer from Player " + str(player)
		self.property_window = PropertyViewer(player, self)
		self.property_window.showFullScreen()



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
		elif player.currPlace.action == COMMUNITY_CHEST_SPACE:
			self.communityChestHandle(player)
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

	def chanceHandle(self, player):
		i = random.randint(0,len(self.board.chanceCards)-1)
		card = self.board.chanceCards[i]
		#self.button_playerAction.setText(card.text)
		player.setLocation(self.board.properties[int(card.location)])
		#print(player.currPosition)
	def communityChestHandle(self, player):
		i = random.randint(0,len(self.board.communityChestCards)-1)
		card = self.board.communityChestCards[i]
		player.pay(int(card.amount))
		

	def bankHandle(self, player):
		property = self.board.properties[player.currPos]
		player.pay(property.price)


	def railroadHandle(self, player):
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
            else:
                owner = currPlace.owner
                print(owner)


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