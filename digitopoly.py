import sys

from PySide.QtGui import *
from PySide.QtCore import *

import random
from multiprocessing import Process
import os
import time
import random
import serial

from ui_window import Ui_MainWindow
from ui_propertyView import Ui_propertyView
from ui_detailView import Ui_detailView
from ui_mainMenu import Ui_mainMenu

from player import Player
from board import *

# 				Red 		Orange 		Yellow 		Green 		Teal 		Blue 		Purple		Pink
# RGB
COLOR_PRESETS_RGB = ["rgb(255,0,0)", "rgb(255,90,0)", "rgb(255,255,0)", "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,0,255)", "rgb(120,0,255)", "rgb(255,0,191)"]
# GRB
COLOR_PRESETS_GRB = set(["grb(0,255,0)", "grb(90,255,0)", "grb(255,255,0)", "grb(255,0,0)", "grb(255,0,255)", "grb(0,0,255)", "grb(0,120,255)", "grb(0,255,191)"])
# Player Pieces
PLAYER_PIECES = ["images/pieces/1.png", "images/pieces/2.png", "images/pieces/3.png", "images/pieces/4.png", "images/pieces/5.png", "images/pieces/6.png", "images/pieces/7.png", "images/pieces/8.png"]

class DetailView(QMainWindow, Ui_detailView):
	"""This is the Property Viewer Object"""
	def __init__(self, property, player, parent=None):
		super(DetailView, self).__init__(parent)

		self.setAttribute(Qt.WA_TranslucentBackground, True)

		# canvas = QPixmap(self.rect())

		# canvas.fill(Qt.transparent) # fill transparent (makes alpha channel available)

		# p = QPainter((canvas))
		# p.setOpacity(0.3)
		# p.setBrush(QBrush(Qt.white)) # use the color you like
		# p.setPen(QPen(Qt.transparen))

		# p.drawRect(Qrect()) # draws the canvas with desired opacity

		# p.start(self)      # now draw on the window itself
		# p.drawPixmap(self.rect(), canvas)

		# Vars
		self.property = property
		self.player = player

		# Update UI
		self.setupUi(self)
		self.displayDetail()

		# Connect Buttons
		reconnect(self.button_closeDetail.clicked, self.close)
		if not (self.property.upgraded):
			reconnect(self.button_upgrade.clicked, self.upgrade)
			self.button_upgrade.setEnabled(True)
			self.button_upgrade.setVisible(True)
		else:
			self.button_upgrade.setEnabled(False)
			self.button_upgrade.setVisible(True)
		if (self.property.action == RAILROAD_SPACE) or (self.property.owner == None):
                        self.button_upgrade.setVisible(False)


	def updatePlayerUI(self):
		player = self.player
		self.label_currPlayerName_2.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo_2.setText(player.dispStr()[0])
		self.button_closeDetail.setEnabled(True)
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))

	def displayDetail(self):
		prop = self.property
		self.propIcon.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(prop.image))
		self.label_propName.setText(str(prop.name))
		print prop.name
		self.label_propCost.setText("Cost to Buy: ${}.00".format(prop.price))
		print prop.price
		self.label_propText.setText(str(prop.upText))
		print prop.upText
		self.label_propRent.setText("Cost to Visit: ${}.00".format(prop.rent))
		print prop.rent
		self.label_propUpCost.setText("Cost to Upgrade: ${}.00".format(prop.upCost))
		print prop.upCost
		self.label_propUpRent.setText("Cost to Visit after Upgrade: ${}.00".format(prop.upRent))
		print prop.upRent
		self.label_propUpText.setText("")
		#print prop.upText
		try:
                    self.label_propOwner.setText("Current Owner: Player {}".format(prop.owner.playerNumber))
                except:
                    self.button_upgrade.setEnabled(False)
                    self.label_propOwner.setText("Current Owner: No owner yet.")
		#print prop.owner

	def upgrade(self):
		self.property.upgraded = True
		self.property.rent = self.property.upRent
		self.player.charge(self.property.upCost)
		self.button_upgrade.setEnabled(False)
		self.displayDetail()

		

class PropertyViewer(QMainWindow, Ui_propertyView):
	"""This is the Property Viewer Object"""
	def __init__(self, player, parent=None):
		super(PropertyViewer, self).__init__(parent)

		# Vars
		self.player = player
		self.parent = parent

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
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))
		self.button_closeProperties.setEnabled(True)

	def displayProps(self):
		player = self.player
		props = player.properties

		for btn in self.propButtons:
			btn.setEnabled(False)
			btn.setText("")

		for btn in self.rrButtons:
			btn.setEnabled(False)
			btn.setText("")

		btnCnt = 0
		rrCnt = 0
		for prop in props:
			if prop.action == RAILROAD_SPACE:
				btn = self.rrButtons[rrCnt]
				
				btn.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(prop.image))
				btn.setText(prop.name)
				btn.setEnabled(True)
				reconnect(btn.clicked, (lambda: self.propDetailOpen(prop, player)))
				rrCnt = rrCnt + 1
			else:
				btn = self.propButtons[btnCnt]
				
				btn.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(prop.image))
				btn.setText(prop.name)
				btn.setEnabled(True)
				reconnect(btn.clicked, (lambda: self.propDetailOpen(prop, player)))
				btnCnt = btnCnt + 1


	def propDetailOpen(self, prop, player):
		self.detail_window = DetailView(prop, player, self)
		self.detail_window.showFullScreen()
		self.detail_window.button_closeDetail.clicked.connect(self.updatePlayerUI)

class MainMenu(QMainWindow, Ui_mainMenu):
	"""docstring for MainMenu"""
	def __init__(self, parent=None):
		super(MainMenu, self).__init__(parent)
			    
		self.setupUi(self)
		self.button_startGame.clicked.connect(self.hide)
                self.button_resumeGame.clicked.connect(self.hide)
                
		self.button_createNewGame.clicked.connect(self.createGame)
		self.button_startGame.clicked.connect(lambda: self.button_addPlayer.setEnabled(False))
		self.button_addPlayer.clicked.connect(self.addPlayer)
		# Player Create Window
		self.frame_newPlayer.setVisible(False)
		self.frame_colorPicker.setVisible(False)
		self.frame_piecePicker.setVisible(False)
		
		self.playerColors = []
		self.playerPieces = []
		self.numPlayers = 0
		
		# Player Buttons
		self.playerLabels = [self.label_player1, self.label_player2, self.label_player3, self.label_player4]
		self.playerColorButtons = [self.button_player1Color, self.button_player2Color, self.button_player3Color, self.button_player4Color]
		self.playerPieceButtons = [self.button_player1Piece, self.button_player2Piece, self.button_player3Piece, self.button_player4Piece]
		self.colorPickerButtons = [self.button_color_1, self.button_color_2, self.button_color_3, self.button_color_4, self.button_color_5, self.button_color_6, self.button_color_7, self.button_color_8]
		self.piecePickerButtons = [self.button_piecePicker_1, self.button_piecePicker_2, self.button_piecePicker_3, self.button_piecePicker_4, self.button_piecePicker_5, self.button_piecePicker_6, self.button_piecePicker_7, self.button_piecePicker_8]

		# for button in self.playerColorButtons:
		# 	reconnect(button.clicked, self.colorPicker)

		self.playerColorButtons[0].clicked.connect(lambda x = 0: self.colorPicker(x))
		self.playerColorButtons[1].clicked.connect(lambda x = 1: self.colorPicker(x))
		self.playerColorButtons[2].clicked.connect(lambda x = 2: self.colorPicker(x))
		self.playerColorButtons[3].clicked.connect(lambda x = 3: self.colorPicker(x))

		self.playerPieceButtons[0].clicked.connect(lambda x = 0: self.piecePicker(x))
		self.playerPieceButtons[1].clicked.connect(lambda x = 1: self.piecePicker(x))
		self.playerPieceButtons[2].clicked.connect(lambda x = 2: self.piecePicker(x))
		self.playerPieceButtons[3].clicked.connect(lambda x = 3: self.piecePicker(x))

		x = 0
		for btn in self.colorPickerButtons:
			btn.setStyleSheet("background-color:{};".format(COLOR_PRESETS_RGB[x]))
			x = x + 1

		x = 0
		for btn in self.piecePickerButtons:
			btn.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(PLAYER_PIECES[x]))
			x = x + 1


	def colorPicker(self, playerNum):
		self.frame_colorPicker.setVisible(True)
		for x in range(0, len(self.colorPickerButtons)):
			if COLOR_PRESETS_RGB[x] in self.playerColors:
				self.colorPickerButtons[x].setVisible(False)
			else:
				self.colorPickerButtons[x].setVisible(True)
				# print "Connecting {} to {}".format(self.colorPickerButtons[x].clicked, (lambda: self.setColor(playerNum, x)))
				reconnect(self.colorPickerButtons[x].clicked, (lambda pnum=playerNum, inp=x: self.setColor(pnum, inp)))

	def setColor(self, playerNum, colorNum):
		print "Setting Player {} Color to {}".format(playerNum, colorNum)
		self.frame_colorPicker.setVisible(False)
		old_color = self.playerColors[playerNum]
		self.colors.append(old_color)
		color = COLOR_PRESETS_RGB[colorNum]		
		self.colors.remove(color)
		self.playerColors[playerNum] = color
		self.playerColorButtons[playerNum].setStyleSheet("background-color:{};".format(color))

	def piecePicker(self, playerNum):
		self.frame_piecePicker.setVisible(True)
		print PLAYER_PIECES
		print self.pieces
		print self.playerPieces
		for x in range(0, len(self.piecePickerButtons)):
			if PLAYER_PIECES[x] in self.playerPieces:
				self.piecePickerButtons[x].setVisible(False)
			else:
				self.piecePickerButtons[x].setVisible(True)
				# print "Connecting {} to {}".format(self.colorPickerButtons[x].clicked, (lambda: self.setColor(playerNum, x)))
				reconnect(self.piecePickerButtons[x].clicked, (lambda pnum=playerNum, inp=x: self.setPiece(pnum, inp)))

	def setPiece(self, playerNum, pieceNum):
		print "Setting Player {} Piece to {}".format(playerNum, pieceNum)
		self.frame_piecePicker.setVisible(False)
		old_piece = self.playerPieces[playerNum]
		self.pieces.append(old_piece)
		piece = PLAYER_PIECES[pieceNum]		
		self.pieces.remove(piece)
		self.playerPieces[playerNum] = piece
		self.playerPieceButtons[playerNum].setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(piece))

	def createGame(self):
		self.frame_newPlayer.setVisible(True)
		self.numPlayers = 0
		self.button_addPlayer.setEnabled(True)
		self.button_startGame.setEnabled(False)
		self.button_resumeGame.setEnabled(True)

		self.playerColors = []
		self.playerPieces = []		
		self.colors = list(COLOR_PRESETS_RGB)
		self.pieces = list(PLAYER_PIECES)
		for x in range(0, 4):
			self.playerLabels[x].setVisible(False)
			self.playerColorButtons[x].setVisible(False)
			self.playerPieceButtons[x].setVisible(False)

	def addPlayer(self):
		self.numPlayers = self.numPlayers + 1
		if self.numPlayers >= 2:
			self.button_startGame.setEnabled(True)
		if self.numPlayers == 4:
			self.button_addPlayer.setEnabled(False)

		self.playerLabels[self.numPlayers - 1].setVisible(True)
		self.playerColorButtons[self.numPlayers - 1].setVisible(True)
		self.playerPieceButtons[self.numPlayers - 1].setVisible(True)

		# Select a Color at Random From the Color Pool
		color = random.sample(self.colors, 1)[0]
		self.colors.remove(color)
		self.playerColors.append(color)
		self.playerColorButtons[self.numPlayers - 1].setStyleSheet("background-color:{};".format(color))

		# Select a Piece at Random From the Color Pool
		piece = random.sample(self.pieces, 1)[0]
		print piece
		self.pieces.remove(piece)
		self.playerPieces.append(piece)
		self.playerPieceButtons[self.numPlayers - 1].setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(piece))


class MainGame(QMainWindow, Ui_MainWindow):
	"""This is the Main Game Object"""
	def __init__(self, parent=None):
		super(MainGame, self).__init__(parent)
		self.setupUi(self)
		
		self.connect_setupUi()
		
		# Create Main Menu Object
		self.menu_window = MainMenu(self)
		self.button_newGame.clicked.connect(self.mainMenu)
		# self.menu_window.showFullScreen()


		# Main Menu Signals
		self.button_mainMenu.clicked.connect(self.pauseGame)
		self.menu_window.button_startGame.clicked.connect(self.startGame)
		self.menu_window.button_resumeGame.clicked.connect(self.updatePlayerInfo)
		
		# self.button_startGame.clicked.connect


		# Vars
		self.players = []
		self.currPlayerNum = -1
		self.board = None

		# Property UI
		self.property_window = None

	def connect_setupUi(self):

		# self.button_fourPlayerStart.clicked.connect(self.startGame)
		self.frame_currentPlayerInfo.setVisible(0)

		# Actually in gameUi:
		# self.button_nextPlayer.clicked.connect(self.getNextPlayer)
		# self.button_playerAction.clicked.connect(self.takeTurn)
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		reconnect(self.button_playerAction.clicked, self.takeTurn)
		reconnect(self.button_showProperties.clicked, self.openPropertyViewer)
		reconnect(self.button_spotImage.clicked, self.propDetailOpen)

		
	def pauseGame(self):
                print(self.players[self.currPlayerNum].color)
                self.menu_window.showFullScreen()
                self.menu_window.button_startGame.setVisible(False)
                self.menu_window.button_resumeGame.setText("Resume Game")
                self.menu_window.button_resumeGame.setVisible(True)
                
	def mainMenu(self):
		self.menu_window.showFullScreen()
		
	def updatePlayerUI(self):
		player = self.players[self.currPlayerNum]
		self.label_currPlayerName.setText("Player {}:".format(player.playerNumber))
		self.label_playerInfo.setText(player.dispStr()[0])
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))
		# self.button_button_playerPieceInd.

		if len(player.properties) > 0:
			self.button_showProperties.setEnabled(True)
		else:
			self.button_showProperties.setEnabled(False)

	def openPropertyViewer(self):
		player = self.players[self.currPlayerNum]
		print "Request to open Property Viewer from Player " + str(player)
		self.property_window = PropertyViewer(player, self)
		self.property_window.showFullScreen()
		self.property_window.button_closeProperties.clicked.connect(self.updatePlayerUI)
		
	def propDetailOpen(self):
                player = self.players[self.currPlayerNum]
                prop = self.board.properties[player.currPos]
                print(prop)
		self.detail_window = DetailView(prop, player, self)
		self.detail_window.showFullScreen()
		self.detail_window.button_closeDetail.clicked.connect(self.updatePlayerUI)


	def startGame(self):
		# self.gameUi(self)
		# self.connect_gameUi();
		print "Setting Up Game"
		self.frame_currentPlayerInfo.setVisible(False)
		self.button_newGame.setVisible(False)
		self.frame_currentPlayerInfo.setVisible(True)

		self.board = Board()
		self.players = []

		self.menu_window.playerColors
		numPlayers = len(self.menu_window.playerColors)

		for x in range(0, numPlayers):
			player = Player(x, 0, self.board.properties[0], self.menu_window.playerColors[x], self.menu_window.playerPieces[x])
			self.players.append(player)
                
                self.button_spotImage.setStyleSheet("border-image: url('images/spotImages/1.png')")
		self.getNextPlayer()

        def updatePlayerInfo(self):
                for x in range(0, self.menu_window.numPlayers):
			self.players[x].color = self.menu_window.playerColors[x]
			self.players[x].piece = self.menu_window.playerPieces[x]

			
	def getNextPlayer(self):
		self.currPlayerNum = self.currPlayerNum + 1
		if self.currPlayerNum == len(self.players):
			self.currPlayerNum = 0
		# Update UI
		self.button_nextPlayer.setEnabled(False)
		self.button_spotImage.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		self.button_playerAction.setEnabled(True)
		self.button_playerAction.setText("Roll Dice")
		reconnect(self.button_playerAction.clicked, self.takeTurn)
		self.frame_diceResult.setVisible(False)
		


		# Update Player UI
		player = self.players[self.currPlayerNum]
		if player.numProperties == 0:
                   self.spotText.setText("It's Player {}'s turn!\n\nRoll the dice to take your turn!".format(player.playerNumber)) 
                else:
                    self.spotText.setText("It's Player {}'s turn!\n\nYou may roll the dice or browse through your properties to upgrade them.".format(player.playerNumber))
                self.button_spotImage.setStyleSheet("border-image: url('images/spotImages/{}.png') 0 0 0 0 stretch stretch;".format(player.currPos + 1))
		
		self.updatePlayerUI()


	def returnToMain(self):
		self.setupUi(self)
		self.connect_setupUi()

	def takeTurn(self):
		player = self.players[self.currPlayerNum]
		roll = player.roll()
		if player.inJail == True:
                    		# Update Player UI after Move
                    self.frame_diceResult.setVisible(True)
                    self.button_dice1Image.setText("")
                    self.button_dice1Image.setStyleSheet("border-image: url('images/dice/{}.png') 0 0 0 0 stretch stretch;".format(str(roll[0])))
                    self.button_dice2Image.setText("")
                    self.button_dice2Image.setStyleSheet("border-image: url('images/dice/{}.png') 0 0 0 0 stretch stretch;".format(str(roll[1])))
                    self.label_diceTotalImage.setText(str(roll[0] + roll[1]))
                    self.button_spotImage.setVisible(True)
                    print("Player Location: {}\n".format(player.currPos))
                    self.jailHandle(player, roll)
                else:
                    # Add In double counts self.doublCount = 0
                    player.move(roll[0] + roll[1])
                    player.currPlace = self.board.properties[player.currPos]
                    print "Player {} moved to index {}.".format(player.playerNumber, player.currPos)

                    # Update Player UI after Move
                    self.frame_diceResult.setVisible(True)
                    self.button_dice1Image.setText("")
                    self.button_dice1Image.setStyleSheet("border-image: url('images/dice/{}.png') 0 0 0 0 stretch stretch;".format(str(roll[0])))
                    self.button_dice2Image.setText("")
                    self.button_dice2Image.setStyleSheet("border-image: url('images/dice/{}.png') 0 0 0 0 stretch stretch;".format(str(roll[1])))
                    self.label_diceTotalImage.setText(str(roll[0] + roll[1]))
                    self.button_spotImage.setVisible(True)
                    # Update background
                    self.button_spotImage.setStyleSheet("border-image: url('images/spotImages/{}.png') 0 0 0 0 stretch stretch;".format(player.currPos + 1))
                    #self.spotText.setText("Hello World")
                    #self.spotText.setText("Player {} moved to index {}: {}.".format(player.playerNumber, player.currPos, self.board.properties[player.currPos]))
                    #self.spotText.setText("Player {} moved to Board Location {}: {} \n\n{}.".format(player.playerNumber, player.currPos, self.board.properties[player.currPos].name,self.board.properties[player.currPos].text))
                    #self.spotText.setText(self.spotText.text + "\n\n {}".format(self.board.properties[player.currPos].text))

                self.updatePlayerUI()
		
		if player.currPlace.action == PROPERTY_SPACE:
			print str(player.currPlace)
                        self.button_spotImage.setEnabled(True)
			self.propertyHandle(player)
		elif player.currPlace.action == CHANCE_SPACE:
			self.chanceHandle(player)
			self.button_spotImage.setEnabled(False)
		elif player.currPlace.action == COMMUNITY_CHEST_SPACE:
			self.communityChestHandle(player)
			self.button_spotImage.setEnabled(False)
		elif player.currPlace.action == BANK_SPACE:
			self.bankHandle(player)
		elif player.currPlace.action == RAILROAD_SPACE:
                        self.button_spotImage.setEnabled(True)
			self.railroadHandle(player)
		elif player.currPlace.action == NOOP_SPACE:
                        self.button_spotImage.setEnabled(False)
                        self.noopHandle(player)
                        
		print("Roll: {}\n".format(roll))


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

                        self.spotText.setText("You landed on {}! \n\n{} \n\nClick the image for more information on buying this property!".format(currentPlace.name, currentPlace.description))

		elif currentPlace.owner != player:
			print "Player Needs to pay Rent"
			player.charge(currentPlace.rent)
			currentPlace.owner.pay(currentPlace.rent)
			self.button_nextPlayer.setText("Next Player")
			self.button_playerAction.setEnabled(False)
			self.button_nextPlayer.setEnabled(True)
			print(currentPlace.rentText)
			self.spotText.setText("You landed on {}! \n\n{} \n\n{}".format(currentPlace.name, currentPlace.description, currentPlace.rentText))

			#self.spotText.setText("Player {} paid {} to Player {} for rent.".format(player.playerNumber, currentPlace.rent, currentPlace.owner.playerNumber))

                elif currentPlace.owner == player:
                    self.button_nextPlayer.setText("Next Player")
		    self.button_playerAction.setEnabled(False)
		    self.button_nextPlayer.setEnabled(True)
		    self.spotText.setText("You landed on {}! \n\n{} \n\nYou already own this property!".format(currentPlace.name, currentPlace.description))

		self.updatePlayerUI()


	def buyProperty(self, player, currentPlace):
		print "Player {} buying {}".format(str(player.playerNumber), str(currentPlace.name))
		currentPlace.owner = player
		player.properties.append(currentPlace)
		player.numProperties = player.numProperties + 1
		player.charge(currentPlace.price)

		# Update UI
		self.updatePlayerUI()
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setEnabled(True)
		self.button_nextPlayer.setText("Next Player")
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)		

	def chanceHandle(self, player):
		i = random.randint(0,len(self.board.chanceCards)-1)
		card = self.board.chanceCards[i]
		#self.button_playerAction.setText(card.text)
		player.setLocation(self.board.properties[int(card.location)])
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setEnabled(True)
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		
		self.spotText.setText("You landed on Chance\n\nYour card says:\n{}.".format(self.board.chanceCards[i].text))
		
		self.updatePlayerUI()
		
	def communityChestHandle(self, player):
		i = random.randint(0,len(self.board.communityChestCards)-1)
		card = self.board.communityChestCards[i]
		player.pay(int(card.amount))
		# Update UI
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		self.button_nextPlayer.setEnabled(True)
		
		self.spotText.setText("You landed on Community Chest!n\nYour card says:\n{}.".format(self.board.communityChestCards[i].text))
		
		self.updatePlayerUI()

	def bankHandle(self, player):
		property = self.board.properties[player.currPos]
		player.charge(property.price)
		# Update UI
		self.updatePlayerUI()
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		self.button_nextPlayer.setEnabled(True)
		
		self.spotText.setText("You landed on {}\n\n{}".format(property.name, property.description))
		
		self.updatePlayerUI()


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
                                
                                self.spotText.setText("You landed on {}! \n\n{} \n\nClick the image for more information on buying this property!".format(currentPlace.name, currentPlace.description))

		elif currentPlace.owner != player:
			print "Player must pay rent to railroad"
			owner = currentPlace.owner
			print(owner)
                        self.spotText.setText("You landed on {}! \n\n{} \n\n{}".format(currentPlace.name, currentPlace.description, currentPlace.rentText))
                
                else:
                    self.button_nextPlayer.setText("Next Player")
		    self.button_playerAction.setEnabled(False)
		    self.button_nextPlayer.setEnabled(True)
		    self.spotText.setText("You landed on {}! \n\n{} \n\nYou already own this property!".format(currentPlace.name, currentPlace.description))

		self.updatePlayerUI()

        def noopHandle(self, player):
                property = self.board.properties[player.currPos]
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setEnabled(True)
		if player.currPos == 30:
                    print("gotoLab registered")
                    player.inJail = True
                    player.setLocation(self.board.properties[10])
                if (player.jailRolls > 0):
                    self.spotText.setText("You are in Jail! To get out of jail you must roll doubles or wait 3 turns.\n\nTurns in Jail: {}".format(player.jailRolls))
                elif player.jailRolls == -1:
                    self.spotText.setText("Congrats! You got out of Open Lab!")
                    player.jailRolls = 0
                else:
                    self.spotText.setText("You landed on {}\n\n{}".format(property.name, property.description))
            
                    
                    
        def jailHandle(self, player, roll):
                if player.jailRolls < 3:
                    player.jailRolls += 1
                else:
                    player.inJail = False
                    player.jailRolls = -1
                if roll[0] == roll[1]:
                    player.inJail = False
                    player.jailRolls = -1
                if player.outOfJail == True:
                    player.inJail = False
                    player.outOfJail = False
                    player.jailRolls = -1


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

def updateLED(led, mode, red = "", green = "", blue = ""):
	""" params: values should be strings
			led: Give the Space Number to light
			mode: (S/B/R)
				S: Solid LED Color
				B: Blinking Solid LED Color
				R: Random LED Color
			red: Red Value 0-255 of the LED for <S> and <B>
			green: Green Value 0-255 of the LED for <S> and <B>
			blue: Blue Value 0-255 of the LED for <S> and <B>
	"""
	# Build String
	string = "{}".format(led, mode, green, red, blue)
	try:
		with open("LEDs", 'w') as f:
			f.write(value)	
	except Exception as e:
		print e

def mouse():
	print "Starting Mouse Emulation pid={}".format(os.getppid())
	'''
	port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

	while True:
		# Move mouse to x y location
		os.system("xdotool mousemove {} {}".format(100, 300))
		# Left Click
		os.system("xdotool click 1")

		try:
			with open("LEDs", 'r') as f:
				led_data = f.read()	
				port.write(led_data)
		except Exception as e:
			print e
			
		time.sleep(10)
	'''


if __name__ == '__main__':
	print "Starting Game pid={}".format(os.getpid())
	# Start Mouse Emulation 
	p = Process(target=mouse)
	p.start()

	currentApp = QApplication(sys.argv)
	currentForm = MainGame()

	currentForm.showFullScreen()
	currentApp.exec_()
	
	p.terminate()
