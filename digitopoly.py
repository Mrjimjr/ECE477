import sys

from PySide.QtGui import *
from PySide.QtCore import *

import random
from multiprocessing import Process
import os
import time
import random
import serial
import re

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
COLOR_PRESETS_GRB = ["000 255 000", "165 255 000", "255 255 000", "255 000 000", "255 000 255", "000 000 255", "000 190 255", "000 255 191"]
# Player Pieces
PLAYER_PIECES = ["images/pieces/1.png", "images/pieces/2.png", "images/pieces/3.png", "images/pieces/4.png", "images/pieces/5.png", "images/pieces/6.png", "images/pieces/7.png", "images/pieces/8.png"]
# RGB Color Array
RGB_COLOR = []
# RGB Mode Array
RGB_MODE = []
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
		self.label_currPlayerName_2.setText("Player {}:".format(player.playerNumber + 1))
		self.label_playerInfo_2.setText(player.dispStr()[0])
		self.button_closeDetail.setEnabled(True)
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))
                
                
	def displayDetail(self):
		prop = self.property
		effect = QGraphicsOpacityEffect(self.frame_background)
		effect.setOpacity(.5)
		self.frame_background.setStyleSheet("border-image: url('{}')".format(prop.spotImage))
		self.frame_background.setGraphicsEffect(effect)
		self.propIcon.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(prop.image))
		self.label_propName.setText(str(prop.name))
		#print prop.name
		self.label_propCost.setText("Cost to Buy: ${}.00".format(prop.price))
		#print prop.price
		self.label_propText.setText(str(prop.upText))
		#print prop.upText
		self.label_propRent.setText("Cost to Visit: ${}.00".format(prop.rent))
		#print prop.rent
		self.label_propUpCost.setText("Cost to Upgrade: ${}.00".format(prop.upCost))
		#print prop.upCost
		self.label_propUpRent.setText("Cost to Visit after Upgrade: ${}.00".format(prop.upRent))
		#print prop.upRent
		self.label_propUpText.setText("")
		#print prop.upText
		try:
                    self.label_propOwner.setText("Current Owner: Player {}".format(prop.owner.playerNumber + 1))
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
		effect = QGraphicsOpacityEffect(self.frame_brickImage)
		effect.setOpacity(.4)
		self.frame_brickImage.setGraphicsEffect(effect)
		self.frame_brickImage.setStyleSheet("border-image: url('brickWall.jpg') 0 0 0 0 stretch stretch;")
		

		# Connect Buttons
		reconnect(self.button_closeProperties.clicked, self.close)

	def updatePlayerUI(self):
		player = self.player
		self.label_currPlayerName_2.setText("Player {}:".format(player.playerNumber + 1))
		self.label_playerInfo_2.setText(player.dispStr()[0])
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))
		self.button_closeProperties.setEnabled(True)

	def displayProps(self):
		player = self.player
		props = player.properties

		for btn in self.propButtons:
			btn.setEnabled(False)
                        btn.setStyleSheet("background-color: rgb(0,0,0,0)")
			btn.setText("")

		for btn in self.rrButtons:
			btn.setEnabled(False)
			btn.setStyleSheet("background-color: rgb(0,0,0,0)")
			btn.setText("")

		btnCnt = 0
		rrCnt = 0
		for prop in props:
			if prop.action == RAILROAD_SPACE:
				btn = self.rrButtons[rrCnt]
				rrCnt = rrCnt + 1
			else:
				btn = self.propButtons[btnCnt]
				btnCnt = btnCnt + 1
                        btn.setText("")
                        #effect = QGraphicsOpacityEffect(btn)
                        #effect.setOpacity(.1)
                        #self.btn.setGraphicsEffect(effect)
                        btn.setAutoFillBackground(True)
			btn.setStyleSheet("border-image: url('{}'); border-color: rgb(0,0,0,0)".format(prop.image))
                        btn.setEnabled(True)

                        reconnect(btn.clicked, (lambda property=prop: self.propDetailOpen(property, player)))
                


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
		
		for i in range(0, 50):
                    RGB_COLOR.append("000 000 000")
                    RGB_MODE.append(0)
                print(len(RGB_COLOR))
                
                with open("LEDs", "w") as f:
                    f.write(str(RGB_COLOR) + "\n")
                    f.write(str(RGB_MODE))
                            
                self.roation = 0


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
		self.label_currPlayerName.setText("Player {}:".format(player.playerNumber + 1))
		self.label_playerInfo.setText(player.dispStr()[0])
		self.button_playerColorInd.setStyleSheet("background-color:{};".format(player.color))
		self.button_button_playerPieceInd.setStyleSheet("border-image: url('{}') 0 0 0 0 stretch stretch;".format(player.piece))
                self.frame_border.setStyleSheet("border: 15px solid {}".format(player.color))

		if len(player.properties) > 0:
			self.button_showProperties.setEnabled(True)
		else:
			self.button_showProperties.setEnabled(False)

	def openPropertyViewer(self):
		player = self.players[self.currPlayerNum]
		#print "Request to open Property Viewer from Player " + str(player)
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
		self.frame_boardImage.setStyleSheet("")
		self.frame_black.setStyleSheet("")
                self.frame_gold.setStyleSheet("")
		effect = QGraphicsOpacityEffect(self.frame_mainImage)
		effect.setOpacity(.1)
		self.frame_mainImage.setGraphicsEffect(effect)
		self.frame_mainImage.setStyleSheet("border-image: url('boardBackgroundMainGame.png') 0 0 0 0 stretch stretch;")
                self.frame_black.setStyleSheet("")
                self.frame_gold.setStyleSheet("")
                self.button_locationLogo.setVisible(True)
                
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

                try:
                    for prop in self.board.properties:
                        for led in prop.LEDs:
                            RGB_MODE[int(led)] = 0
                            if isinstance(prop.owner, Player):
                                RGB_COLOR[int(led)] = COLOR_PRESETS_GRB[COLOR_PRESETS_RGB.index(prop.owner.color)]
                            else:
                                RGB_COLOR[int(led)] = "000 000 000"
                except Exception as e:
                    print e
                    pass
		
                with open("LEDs", "w") as f:
                    f.write(str(RGB_COLOR) + "\n")
                    f.write(str(RGB_MODE))
                    
		
		print(RGB_COLOR)
		print(RGB_MODE)
		# Update UI
		self.button_nextPlayer.setEnabled(False)
		self.button_spotImage.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		self.button_playerAction.setEnabled(True)
		self.button_playerAction.setText("Roll Dice")
		reconnect(self.button_playerAction.clicked, self.takeTurn)
		self.frame_diceResult.setVisible(False)
		

		# self.button_button_playerPieceInd.
                
                    
		# Update Player UI
		player = self.players[self.currPlayerNum]
		self.chanceCard.setStyleSheet("")
                self.chanceCard.setText("")
		currentPlace = self.board.properties[player.currPos]
		if player.numProperties == 0:
                    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                    self.locationName.setText("{}".format(currentPlace.name))
                    self.spotText.setText("It's Player {}'s turn!".format(player.playerNumber + 1))
                    self.actionText.setText("Roll the dice to take your turn!")
                else:
                    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                    self.locationName.setText("{}".format(currentPlace.name))
                    self.spotText.setText("It's Player {}'s turn!".format(player.playerNumber + 1))
                    self.actionText.setText("You may roll the dice or browse through your properties to upgrade them.")
                self.button_spotImage.setStyleSheet("border-image: url('images/spotImages/{}.png') 0 0 0 0 stretch stretch;".format(player.currPos + 1))
		print("Color:", player.color)
		self.updatePlayerUI()


        def UpdateOrientation(self):
            
            if self.currPlayerNum == 0:
                self.roation = 0
                self.button_playerAction.setGeometry(QRect(740, 590, 241, 71))
                self.button_nextPlayer.setGeometry(QRect(980, 590, 241, 71))
                self.frame_currentPlayerInfo.setGeometry(QRect(0, 0, 1280, 720))
                self.button_mainMenu.setGeometry(QRect(1140, 10, 121, 31))
                self.frame_playerInfo.setGeometry(QRect(10, 10, 471, 141))
                self.label_currPlayerName.setGeometry(QRect(10, 10, 171, 17))
                self.label_playerInfo.setGeometry(QRect(10, 30, 271, 101))
                self.button_showProperties.setGeometry(QRect(290, 80, 161, 51))
                self.button_playerColorInd.setGeometry(QRect(290, 10, 71, 61))
                self.button_button_playerPieceInd.setGeometry(QRect(370, 10, 71, 61))
                self.frame_diceResult.setGeometry(QRect(740, 460, 481, 121))
                self.label_diceTitle.setGeometry(QRect(10, 10, 91, 17))
                self.label_Dice1.setGeometry(QRect(110, 100, 66, 17))
                self.label_Dice2.setGeometry(QRect(230, 100, 66, 17))
                self.label_diceTotal.setGeometry(QRect(360, 100, 66, 17))
                self.label_diceTotalImage.setGeometry(QRect(350, 10, 81, 71))
                self.button_dice1Image.setGeometry(QRect(100, 10, 81, 81))
                self.button_dice2Image.setGeometry(QRect(220, 10, 81, 81))
                self.button_spotImage.setGeometry(QRect(120, 225, 430, 380))
                self.spotText.setGeometry(QRect(685, 80, 520, 320))
            elif self.currPlayerNum== 1:
                self.rotation = 1
                
                self.button_playerAction.setGeometry(QRect(1175, 255, 71, 241))
                self.button_nextPlayer.setGeometry(QRect(1175, 10, 71, 241))
                #self.frame_currentPlayerInfo.setGeometry(QRect(0, 580, 120, 428))
                self.button_mainMenu.setGeometry(QRect(10, 10, 31, 121))
                self.frame_playerInfo.setGeometry(QRect(10, 190, 141, 471))
                self.label_currPlayerName.setGeometry(QRect(10, 200, 20, 265))
                self.label_currPlayerName.setStyleSheet("background-color: rgb(0, 255, 255)")
                self.label_playerInfo.setGeometry(QRect(35, 200, 95, 265))
                self.label_playerInfo.setStyleSheet("background-color: rgb(255, 0, 255)")
                self.button_showProperties.setGeometry(QRect(80, 25, 51, 161))
                self.button_playerColorInd.setGeometry(QRect(10, 110, 61, 71))
                self.button_button_playerPieceInd.setGeometry(QRect(10, 30, 61, 71))
                self.frame_diceResult.setGeometry(QRect(1040, 10, 121, 481))
                self.label_diceTitle.setGeometry(QRect(10, 385, 17, 91))
                self.label_diceTitle.setStyleSheet("background-color: rgb(0, 255, 255)")
                self.label_Dice1.setGeometry(QRect(100, 180, 17, 66))
                self.label_Dice1.setStyleSheet("background-color: rgb(255, 0, 255)")
                self.label_Dice2.setGeometry(QRect(100, 280, 17, 66))
                self.label_Dice2.setStyleSheet("background-color: rgb(255, 0, 255)")
                self.label_diceTotal.setGeometry(QRect(100, 75, 17, 66))
                self.label_diceTotal.setStyleSheet("background-color: rgb(255, 0, 255)")
                self.label_diceTotalImage.setGeometry(QRect(10, 70, 71, 81))
                self.label_diceTotalImage.setStyleSheet("background-color: rgb(255, 255, 0)")
                self.button_dice1Image.setGeometry(QRect(10, 180, 81, 81))
                self.button_dice2Image.setGeometry(QRect(10, 280, 81, 81))
                self.button_spotImage.setGeometry(QRect(225, 245, 380, 430))
                self.button_spotImage.setStyleSheet("background-color: rgb(255, 0, 255)")
                self.spotText.setGeometry(QRect(665, 70, 320, 520))
                self.spotText.setStyleSheet("background-color: rgb(0, 255, 255)")
            elif self.currPlayerNum == 2:
                self.button_playerAction.setGeometry(QRect(10, 10, 241, 71))
            else:
                self.button_playerAction.setGeometry(QRect(10, 590, 241, 71))
                    
                    
	def returnToMain(self):
		self.setupUi(self)
		self.connect_setupUi()

	def takeTurn(self):
		player = self.players[self.currPlayerNum]
		roll = player.roll()
		currentPlace = self.board.properties[player.currPos]
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
                    print "Player {} moved to index {}.".format(player.playerNumber + 1, player.currPos)
		
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

                RGBindex = COLOR_PRESETS_RGB.index(player.color)
		for LED in player.currPlace.LEDs:
                    RGB_COLOR[int(LED)] = COLOR_PRESETS_GRB[RGBindex]
                    RGB_MODE[int(LED)] = 2
                    
                with open("LEDs", "w") as f:
                    f.write(str(RGB_COLOR) + "\n")
                    f.write(str(RGB_MODE))
                    
                
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
			self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                        self.locationName.setText("{}".format(currentPlace.name))
                        self.spotText.setText("{}".format(currentPlace.description))
                        self.actionText.setText("Price to Buy: ${}.00\nClick the image for more information about buying this property!".format(currentPlace.price))

		elif currentPlace.owner != player:
			print "Player Needs to pay Rent"
			player.charge(currentPlace.rent)
			currentPlace.owner.pay(currentPlace.rent)
			self.button_nextPlayer.setText("Next Player")
			self.button_playerAction.setEnabled(False)
			self.button_nextPlayer.setEnabled(True)
			print(currentPlace.rentText)
			newRentText = str(currentPlace.rentText.format(currentPlace.rent))
			self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
			self.locationName.setText("{}".format(currentPlace.name))
			self.spotText.setText("{}".format(currentPlace.description))
			self.actionText.setText("{}".format(newRentText))

			#self.spotText.setText("Player {} paid {} to Player {} for rent.".format(player.playerNumber, currentPlace.rent, currentPlace.owner.playerNumber))

                elif currentPlace.owner == player:
                    self.button_nextPlayer.setText("Next Player")
		    self.button_playerAction.setEnabled(False)
		    self.button_nextPlayer.setEnabled(True)
		    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image)) 
		    self.locationName.setText("{}".format(currentPlace.name))
		    self.spotText.setText("{}".format(currentPlace.description))
                    self.actionText.setText("You already own this property!")
		self.updatePlayerUI()

        
	def buyProperty(self, player, currentPlace):
		print "Player {} buying {}".format(str(player.playerNumber + 1), str(currentPlace.name))
		currentPlace.owner = player
		player.properties.append(currentPlace)
		player.numProperties = player.numProperties + 1
		player.charge(currentPlace.price)
		RGBindex = COLOR_PRESETS_RGB.index(player.color)
		print("index", RGBindex)
		for LED in currentPlace.LEDs:
                    RGB_COLOR[int(LED)] = COLOR_PRESETS_GRB[RGBindex]
                    RGB_MODE[int(LED)] = 1

                with open("LEDs", "w") as f:
                    f.write(str(RGB_COLOR) + "\n")
                    f.write(str(RGB_MODE))
                    
		# Update UI
		self.updatePlayerUI()
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setEnabled(True)
		self.button_nextPlayer.setText("Next Player")
		reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)		

	def chanceHandle(self, player):
		i = random.randint(0,len(self.board.chanceCards)-1)
		card = self.board.chanceCards[i]
		prevlocation = player.currPos
		currentPlace = self.board.properties[player.currPos]
		#self.button_playerAction.setText(card.text)
		#player.setLocation(self.board.properties[int(card.location)])
		player.currPos = int(card.location)
                player.currPlace = self.board.properties[player.currPos]
                print("currPlace for chance {} Curr Pos for chance{}\n".format(player.currPlace.position, player.currPos))
		self.button_playerAction.setEnabled(True)
		self.button_nextPlayer.setEnabled(False)
		#reconnect(self.button_nextPlayer.clicked, self.getNextPlayer)
		self.button_playerAction.setText("Advance")
		self.locationName.setText("Chance!")
		self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
		self.chanceCard.setStyleSheet("border-image: url('chanceCard.png'); font: italic 14pt Serif")
		cardText = ""
		textCount = len(card.description)
		j = 0
		while textCount >= 25:
                    prevj = j
                    j = 0
                    while ((textCount-j > 0) and ((j < 25) or (card.description[len(card.description) - textCount + j] != " "))):
                        print(j)
                        print(card.description[len(card.description) - textCount + j])
                        j += 1
                    cardText = cardText + "\n       {}".format(card.description[len(card.description) - textCount:(len(card.description) - textCount+ j)])
                    textCount -= j
                cardText = cardText + "\n      {}".format(card.description[len(card.description) - textCount:])
 		self.chanceCard.setText("{}".format(cardText))
		self.actionText.setText("{}".format(card.text))
		self.spotText.setText("")
		self.updatePlayerUI()
		reconnect(self.button_playerAction.clicked, (lambda prevLoc=prevlocation: self.takeAction(player, prevLoc)))
	
                
        def takeAction(self, player, prevLoc):
                self.chanceCard.setStyleSheet("")
                self.chanceCard.setText("")
                self.button_spotImage.setStyleSheet("border-image: url('images/spotImages/{}.png') 0 0 0 0 stretch stretch;".format(player.currPos + 1))
                
                prevLoc = self.board.properties[prevLoc]
		for LED in prevLoc.LEDs:
                    RGB_COLOR[int(LED)] = "000 000 000"
                    RGB_MODE[int(LED)] = 1           
                
                RGBindex = COLOR_PRESETS_RGB.index(player.color)
		for LED in player.currPlace.LEDs:
                    RGB_COLOR[int(LED)] = COLOR_PRESETS_GRB[RGBindex]
                    RGB_MODE[int(LED)] = 2
                    
                with open("LEDs", "w") as f:
                    f.write(str(RGB_COLOR) + "\n")
                    f.write(str(RGB_MODE))
                
                if player.currPlace.action == PROPERTY_SPACE:
                        print str(player.currPlace)
                        self.button_spotImage.setEnabled(True)
                        self.propertyHandle(player)
                        #if player.currPos < prevLoc:
                        #    player.money = player.money + 200
                        #    print("Chance Card Sent Past Go\n")
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
                        #if player.currPos < prevLoc:
                        #    player.money = player.money + 200
                        #    print("Chance Card Sent Past Go\n")
                elif player.currPlace.action == NOOP_SPACE:
                        self.button_spotImage.setEnabled(False)
                        self.noopHandle(player)
                        
	def communityChestHandle(self, player):
		i = random.randint(0,len(self.board.communityChestCards)-1)
		card = self.board.communityChestCards[i]
		player.pay(int(card.amount))
		currentPlace = self.board.properties[player.currPos]
		# Update UI
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		self.button_nextPlayer.setEnabled(True)
		cardText = ""
		textCount = len(card.description)
		j = 0
		while textCount >= 25:
                    prevj = j
                    j = 0
                    while ((textCount-j > 0) and ((j < 25) or (card.description[len(card.description) - textCount + j] != " "))):
                        print(j)
                        print(card.description[len(card.description) - textCount + j])
                        j += 1
                    cardText = cardText + "\n       {}".format(card.description[len(card.description) - textCount:(len(card.description) - textCount+ j)])
                    textCount -= j
                cardText = cardText + "\n      {}".format(card.description[len(card.description) - textCount:])
                self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
		self.locationName.setText("Community Chest!")
		self.chanceCard.setStyleSheet("border-image: url('communityChest.png'); font: italic 14pt Serif")
		self.chanceCard.setText("{}".format(cardText))
		self.spotText.setText("")
		self.actionText.setText("{}".format(card.text))
		self.updatePlayerUI()

	def bankHandle(self, player):
		property = self.board.properties[player.currPos]
		player.charge(property.price)
		# Update UI
		self.updatePlayerUI()
		self.button_playerAction.setEnabled(False)
		self.button_nextPlayer.setText("Next Player")
		self.button_nextPlayer.setEnabled(True)
		self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(property.image))
		self.locationName.setText("{}".format(property.name))
		self.spotText.setText("{}".format(property.description))
		self.actionText.setText("")
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
						self.button_nextPlayer.setEnabled(True)
				self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                                self.locationName.setText("{}".format(currentPlace.name))
                                self.spotText.setText("{}".format(currentPlace.description))
                                self.actionText.setText("Price to Buy: $200.00\nClick the image for more information about buying this property!")


		elif currentPlace.owner != player:
			print "Player must pay rent to railroad"
			owner = currentPlace.owner
			print(owner)
			currentPlace.rent = float(25.0/2.0)
			for property in owner.properties:
                            if property.action == RAILROAD_SPACE:
                                currentPlace.rent = float(currentPlace.rent * 2.0)
                        newRentText = (currentPlace.rentText).format(int(currentPlace.rent))
                        self.button_nextPlayer.setText("Next Player")
                        self.button_playerAction.setEnabled(False)
                        self.button_nextPlayer.setEnabled(True)
                        self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                        self.locationName.setText("{}".format(currentPlace.name))
                        self.spotText.setText("{}".format(currentPlace.description))
                        self.actionText.setText("{}".format(newRentText))
                else:
                    self.button_nextPlayer.setText("Next Player")
		    self.button_playerAction.setEnabled(False)
		    self.button_nextPlayer.setEnabled(True)
		    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
		    self.locationName.setText("{}".format(currentPlace.name))
		    self.spotText.setText("{}".format(currentPlace.description))
                    self.actionText.setText("You already own this property!")
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
                    self.spotText.setText("You are in Open Lab! \n\nTurns in Open Lab: {}".format(player.jailRolls))
                    self.actionText.setText("To get out of jail you must roll doubles or wait 3 turns.")
                    self.locationName.setText("Open Lab")
                    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                elif player.jailRolls == -1:
                    self.spotText.setText("Congrats! You got out of Open Lab!")
                    self.actionText.setText("Wait until next turn to move your piece... let the next player go.")
                    player.jailRolls = 0
                else:
                    self.button_locationLogo.setStyleSheet("border-image: url('{}')".format(currentPlace.image))
                    self.locationName.setText("{}".format(property.name))
                    self.spotText.setText("{}".format(property.description))
                    self.actionText.setText("Nothing else to do here.... let the next player go.")
            
                    
                    
        def jailHandle(self, player, roll):
                if player.jailRolls < 2:
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

def updateLED():
# def updateLED(led, mode, red = "", green = "", blue = ""):
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
	port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

	while True:
                with open("LEDs", "r") as f:
                    RGB_COLOR = re.findall(r'\'([^\']*)\'', f.readline())
                    RGB_MODE = re.findall(r'\d', f.readline())
                    
                
		for x in range(0,49):
			string = "S {:02d} {} x".format(x, RGB_COLOR[x])
			#print "writing " + string
			port.write(string)
			time.sleep(0.01)
		
		# Blink LEDs
		for x in range(0,49):
			if RGB_MODE[x] == '2':
				string = "S {:02d} 000 000 000 x".format(x)
				# print "writing " + string
				port.write(string)
			time.sleep(0.01)
		
		rcv = port.readline().rstrip()
		#print rcv
		try:
			xLoc = re.search(r'X([^X]*)', rcv).group(1)
			xLocInt = round(int(xLoc)) / 4
			cmd = "xdotool mousemove {} {}".format(xLocInt, 300)
			#print rcv
			#print cmd
			# print cmd
			# Move mouse to x y location
			os.system(cmd)
			# Left Click
			# os.system("xdotool click 1")
		except:
                        pass



if __name__ == '__main__':
	print "Starting Game pid={}".format(os.getpid())
	# Start Mouse Emulation 
	p = Process(target=updateLED)
	p.start()

	currentApp = QApplication(sys.argv)
	currentForm = MainGame()

	currentForm.showFullScreen()
	currentApp.exec_()
	
	p.terminate()
