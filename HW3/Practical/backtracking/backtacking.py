class Sudoko_backtracking:
    def __init__(self,board):
        self.board=board
        
    def print_board(self):        
        for i in range(9):            
            if i%3==0 and i!=0:                
                print("- - - - - - - - - -")
            for j in range(9):
                if j%3==0  and j!=0:                                         
                    print("|",end="")  
                if j==8:
                    print(self.board[i][j])    
                else:
                    print(str(self.board[i][j])+" ",end="")
    
    def getNextLocation(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==0:
                    return (i,j)           
        return(-1,-1)
    
    def isSafe(self,posi,posj,choise) :
        #row
        for i in range(9):
            if self.board[posi][i]==choise and posj!=i:
                return False                           
        #column
        for i in range(9):
            if self.board[i][posj]==choise and posi!=i:
                return False
        
        #check region
        bi=posi-(posi%3)
        bj=posj-(posj%3)
        for i in range(bi,bi+3):
            for j in range(bj,bj+3):
                if self.board[i][j]==choise and i!=posi and j!=posj:
                    return False    
        return True 
    
    def solveSimpleBackTracking(self):
        location=self.getNextLocation()
        if location[0]==-1:
            return True
        else:
            for choise in range(1,10):
                if self.isSafe(location[0],location[1],choise):
                    self.board[location[0]][location[1]]=choise
                    if self.solveSimpleBackTracking():
                        return True
                    self.board[location[0]][location[1]]=0
        return False            

board=[
    [0,1,6,3,0,8,4,2,0],
    [8,4,0,0,0,7,3,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,6,0,9,4,0,8,0,2],
    [0,8,1,0,3,0,7,9,0],
    [9,0,3,0,7,6,0,4,0],
    [0,0,0,0,0,0,0,0,3],
    [0,0,5,7,0,0,0,6,8],
    [0,7,8,1,0,3,2,5,0]
]
a=Sudoko_backtracking(board)
a.print_board() 
print("_____________________________")
a.solveSimpleBackTracking()
a.print_board()                  
    