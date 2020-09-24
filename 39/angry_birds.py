from os import system, name
import random
import sys

class Bird:
    def __init__(self):
        self.icon = '🐥'
        self.x_loc = random.randint(0, 9)
        self.y_loc = random.randint(0, 9)

    def move(self, input):
        move = input.lower()
        if(move == 'w'):
            self.x_loc -= 1
        elif(move == 'a'):
            self.y_loc -= 1
        elif(move == 's'):
            self.x_loc += 1
        elif(move == 'd'):
            self.y_loc += 1

class Pig:
    def __init__(self):
        self.icon = '🐷'
        self.x_loc = random.randint(0, 9)
        self.y_loc = random.randint(0, 9)

class BoardPiece:
    def __init__(self):
        self.icon = '🌱'

class Board:

    def __init__(self, bird, pig):
        self.bird = bird
        self.pig = pig
        self.boardArray = []

    def initBoard(self):
        self.boardArray = []
        for i in range(0,10):
            temp = []
            for j in range(0,10):
                temp.append(BoardPiece().icon)
            self.boardArray.append(temp)

    def printBoard(self):
        boardString = ''
        for p in self.boardArray:
            for pp in p:
                boardString = boardString + ' ' +  pp
            boardString = boardString + '\n'
        print(boardString)

    def updateBoard(self):
        self.initBoard()
        self.boardArray[self.pig.x_loc][self.pig.y_loc] = self.pig.icon
        self.boardArray[self.bird.x_loc][self.bird.y_loc] = self.bird.icon
        if(self.gameWon()):
            print('Game won!')
            sys.exit(1)
        self.clear()
        self.printBoard()

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def gameWon(self):
        return self.pig.x_loc == self.bird.x_loc and self.pig.y_loc == self.bird.y_loc

#sometimes start with bird and pig in same local - auto win
#can crash game by moving beyond board

b = Bird()
p = Pig()

board = Board(b, p)

while(True):
    board.updateBoard()
    move = input()
    b.move(move)
