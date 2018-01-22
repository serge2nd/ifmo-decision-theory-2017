from tkinter import *
from Lab3.Assets import Assets



class GridItem:
    X='X'
    O='O'
    DEF='DEF'
    def __init__(self,grid,row,column,state=DEF):
        self.state = state
        self.row = row
        self.column = column
        self.grid= grid
    def attachButton(self,button):
        self.button = button
    def pressed(self):
        newstate = self.grid.pressFunc(self.row, self.column)
        self.setState(newstate)
    def setState(self,state):
        image = Assets.getDefault()
        if (state==self.X):
            image = Assets.getX()
        if (state == self.O):
            image = Assets.getO()
        self.button.config(state=DISABLED, image=image, width='145', height='155', text='o')
        self.state = state


class Grid:
    def __init__(self,window,pressFunc, size=3):
        self.pressFunc = pressFunc
        self.window = window
        self.gritObjects = []
        for i in range(0, size):
            row=[]
            for j in range(0, size):
                item = GridItem(self, i, j)
                button = Button(self.window, command=item.pressed)
                button.grid(row=4+i, column=j)
                button.config(image=Assets.getDefault(), width='145', height='155')
                item.attachButton(button)
                row.append(item)
            self.gritObjects.append(row)
    def setStateToItem(self,row,column,state):
        self.gritObjects[row][column].setState(state);
