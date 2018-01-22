import random
import time
from tkinter import *
from Lab3.Engine import Engine
from Lab3.Grid import Grid
from Lab3.Grid import GridItem
from Lab3.Setting import Setting
from Lab3.utils import delay



class TicTacToe:
    PLAYER = 'PLAYER'
    COMPUTER = 'COMPUTER'

    def start(self):
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.setting = Setting(self.window)
        # New Game Button
        self.newStartGame = Button(self.window, text='Start Game')
        self.newStartGame.bind('<Button-1>', self.startGame)
        self.newStartGame.grid(row=1, column=2, rowspan=3)
        self.currentPlayer = None
        self.engine = None
        self.window.mainloop()
    def startGame(self, event):
        self.grid = Grid(self.window, self.pressed, 3 if self.setting.getSize() == Setting.SIZE_3 else 4)
        self.currentPlayer = self.PLAYER if self.setting.getPlayer() == Setting.PLAYER_FIRST else self.COMPUTER
        self.engine = Engine(
            Engine.STRATEGY_DEFAULT if self.setting.getMod() == Setting.MOD_STANDART else Engine.STRATEGY_EXTRA,
            3 if self.setting.getSize() == Setting.SIZE_3 else 4,
            Engine.PL if self.setting.getPlayer() == Setting.PLAYER_FIRST else Engine.PC
        )
        if (self.currentPlayer == self.COMPUTER):
            self.processComputerStep()
        return 1

    def pressed(self, row, column):
        #
        self.engine.changePlayerState(row, column)
        self.currentPlayer = self.COMPUTER
        self.processComputerStep()
        return GridItem.X if self.setting.getPlayer() == Setting.PLAYER_FIRST else GridItem.O

    @delay(0.1)
    def processComputerStep(self):
        move = self.engine.getBestMove()
        if (move == None):
            return
        row,column = move
        self.engine.changeComputerState(row, column)
        self.grid.setStateToItem(row,column,GridItem.O if self.setting.getPlayer() == Setting.PLAYER_FIRST else GridItem.X)
        self.currentPlayer = self.PLAYER

