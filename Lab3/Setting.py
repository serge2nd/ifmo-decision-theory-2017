from tkinter import *


class Setting:
    MOD_STANDART = 'MOD_STANDART'
    MOD_CRAZY = 'MOD_CRAZY'
    SIZE_3 = '3X3'
    SIZE_4 = '4X4'
    PLAYER_FIRST = 'PLAYER_FIRST'
    PLAYER_SECOND = 'PLAYER_SECOND'

    def __init__(self, window):
        self.window = window
        self.size = self.SIZE_3
        lbSize = Listbox(self.window, height=2, exportselection=0)
        lbSize.insert("end", self.SIZE_3)
        lbSize.insert("end", self.SIZE_4)
        lbSize.bind("<Double-Button-1>", self.onSize)
        lbSize.grid(row=1, column=1)
        self.mod = self.MOD_STANDART
        lbMod = Listbox(self.window, height=2, exportselection=0)
        lbMod.insert("end", self.MOD_STANDART)
        lbMod.insert("end", self.MOD_CRAZY)
        lbMod.bind("<Double-Button-1>", self.onMod)
        lbMod.grid(row=2, column=1)
        self.player = self.PLAYER_FIRST
        lbPlayer = Listbox(self.window, height=2, exportselection=0)
        lbPlayer.insert("end", self.PLAYER_FIRST)
        lbPlayer.insert("end", self.PLAYER_SECOND)
        lbPlayer.bind("<Double-Button-1>", self.onPlayer)
        lbPlayer.grid(row=3, column=1)

    def onSize(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.size = value
        print("selection size:", selection, ": '%s'" % value)

    def onMod(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.mod = value
        print("selection mod:", selection, ": '%s'" % value)

    def onPlayer(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.player = value
        print("selection player:", selection, ": '%s'" % value)
    def getSize(self):
        return self.size
    def getMod(self):
        return self.mod
    def getPlayer(self):
        return self.player