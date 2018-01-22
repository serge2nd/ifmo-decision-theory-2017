from tkinter import *
import os

class Assets:
    DEFAULT=None
    X=None
    O=None
    @staticmethod
    def getDefault():
        if (Assets.DEFAULT is None):
            dir = os.getcwd()
            Assets.DEFAULT = PhotoImage(file=dir + '\\Lab2\\assets\\default.gif')
        return Assets.DEFAULT

    @staticmethod
    def getX():
        if (Assets.X is None):
            dir = os.getcwd()
            Assets.X = PhotoImage(file=dir + '\\Lab2\\assets\\x.gif')
        return Assets.X

    @staticmethod
    def getO():
        if (Assets.O is None):
            dir = os.getcwd()
            Assets.O = PhotoImage(file=dir + '\\Lab2\\assets\\o.gif')
        return Assets.O