import os
from copy import deepcopy
import math
import random


player, opponent = 'X', 'O'
turn=[0]

class Node():
    def __init__(self, board, parent):        
        if  not isMovesLeft(board) or checkWin(board):
            self.terminal = True
        else:
            self.terminal = False
        self.utility = 0
        self.children = []    
        self.fullexpand = False
        self.parent = parent
        self.visits = 0
        self.board = board

class mcts():
    def search(self, initistate):
        r = Node(initistate, None)
        for i in range(600):
            node = self.select(r)            
            score = self.randommoveter(node.board)
            self.update(node, score)
        return self.whichnodebettertoexpand(r, 0)         
    def select(self, node):
        while not node.terminal:
            if node.fullexpand:
                node = self.whichnodebettertoexpand(node, math.sqrt(2))
            else:
                return self.expandnode(node)       
        return node
    def whichnodebettertoexpand(self, node, c):
        best = float('-inf')
        bestnodetoexpand = []
        x=con(node.board)
        if x==1:
            currentp=1
        elif x==0:
            currentp=-1
        for child_node in node.children:
            exploit = ((currentp * child_node.utility) / child_node.visits) 
            explore=(c * math.sqrt(math.log(node.visits / child_node.visits)))
            ai=exploit+explore
            if ai > best:
                best = ai
                bestnodetoexpand = [child_node]
            elif ai == best:
                bestnodetoexpand.append(child_node)
        return random.choice(bestnodetoexpand)     

    def expandnode(self, node):
        halatha = generateaction(node.board)
        for state in halatha:
            if check(node,state):
                newnode = Node(state, node)
                node.children.append(newnode)
                if len(halatha) == len(node.children):
                    node.fullexpand = True
                return newnode
    def randommoveter(self,board1):
        while not checkWin(board1):
            if not isMovesLeft(board1):
                return 0
            else:                                                                             
               board1=random.choice(generateaction(board1))          
        if con(board1)==0:
            return 1
        elif con(board1)==1:
            return -1
                
    def update(self, node, score):
        while node is not None:
            node.utility += score
            node.visits += 1
            node = node.parent
                                                                                                            
def equal(board1,board2):
    for i in range(3):
        for j in range(3):
            if board1[i][j]!=board2[i][j]:
                return False                    
    return True

def check(node,state):
    for child in node.children:
        if equal(child.board,state):
            return False
    return True    
        
    
def generateaction(board1):
    action=[]
    for i in range(3):
        for j in range(3):
            if board1[i][j]=='_':
                action.append(move(board1,i,j))
    return action            
                              
def move(board1,row,column):
    b=deepcopy(board1)
    x=con(b)
    if x==0:
        b[row][column]=player
    else:
        b[row][column]=opponent  
    return b        
def con(board):
    xx,xo=0,0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                xx+=1
            elif board[i][j]=='O':
                xo+=1
    if xx==xo:
        return 0
    else:
        return 1                
                
        
def findBestMove(board):  
    mcts1 = mcts()
    bestmove = mcts1.search(board)
    ini,inj=0,0
    b=bestmove.board
    for i in range(3):
        for j in range(3):
            if board[i][j]!=b[i][j]:
                ini=i
                inj=j
                break
    return [ini,inj]


def findRandom(board):
    empty_spots = [i*3+j for i in range(3)
                   for j in range(3) if board[i][j] == "_"]
    idx =random.choice(empty_spots)
    return[int(idx/3), idx % 3]


def isMovesLeft(board):
    return ('_' in board[0] or '_' in board[1] or '_' in board[2])


def checkWin(board):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and not board[row][0] == '_'):
            return True
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and not board[0][col] == '_'):
            return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and not board[0][0] == '_'):
        return True

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and not board[0][2] == '_'):
        return True

    return False


def printBoard(board):
    #os.system('cls||clear')
    print("\n Player : X , Agent: O \n")
    for i in range(3):
        print(" ", end=" ")
        for j in range(3):
            if(board[i][j] == '_'):
                print(f"[{i*3+j+1}]", end=" ")
            else:
                print(f" {board[i][j]} ", end=" ")

        print()
    print()


if __name__ == "__main__":
    board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
    ]



    while isMovesLeft(board) and not checkWin(board):
        if(turn[0] == 0):
            printBoard(board)
            print(" Select Your Move :", end=" ")
            tmp = int(input())-1
            userMove = [int(tmp/3),  tmp % 3]
            while((userMove[0] < 0 or userMove[0] > 2) or (userMove[1] < 0 or userMove[1] > 2) or board[userMove[0]][userMove[1]] != "_"):
                print('\n \x1b[0;33;91m' + ' Invalid move ' + '\x1b[0m \n')
                print("Select Your Move :", end=" ")
                tmp = int(input())-1
                userMove = [int(tmp/3),  tmp % 3]
            board[userMove[0]][userMove[1]] = player
            print("Player Move:")
            printBoard(board)
            turn[0] = 1
        else:
            bestMove = findBestMove(board)
            board[bestMove[0]][bestMove[1]] = opponent
            print("Agent Move:")
            printBoard(board)
            turn [0]= 0

    if(checkWin(board)):
        if(turn[0] == 1):
            print('\n \x1b[6;30;42m' + ' Player Wins! ' + '\x1b[0m')

        else:
            print('\n \x1b[6;30;42m' + ' Agent Wins! ' + '\x1b[0m')
    else:
        print('\n \x1b[0;33;96m' + ' Draw! ' + '\x1b[0m')

    input('\n Press Enter to Exit... \n')
