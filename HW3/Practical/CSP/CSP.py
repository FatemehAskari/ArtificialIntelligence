class Sudoko_CSP:   
    def __init__(self,dim,fileDir) :       
        self.dim=dim
        self.expandedNodes=0 
        file=open(fileDir,'r')
        f=file.readlines()
        self.board=[]
        for i in f:            
            self.board.append(list(map(int,i.split()))) 
        self.rv=self.getRemainingValues()
    def  getDomain(self,row,col):
        RVcell=[int(i) for i in range(1,self.dim+1)]         
        #row
        for i in range(self.dim):
            if self.board[row][i]!=0:
                if self.board[row][i] in RVcell:
                    RVcell.remove(self.board[row][i])
        #column
        for i in range(self.dim):
            if self.board[i][col]!=0:
                if self.board[i][col] in RVcell:
                    RVcell.remove(self.board[i][col])
        #region
        boxRow=row-row%3
        boxCol=col-col%3
        for i in range(3):
            for j in range(3):
                if self.board[boxRow+i][boxCol+j] in RVcell:
                    RVcell.remove(self.board[boxRow+i][boxCol+j])
        return RVcell
    def getRemainingValues(self):
        RV=[]
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col]!=0:
                    RV.append(['x'])
                else:
                    RV.append(self.getDomain(row,col))
        return RV
                                                        
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
    
    def algocsp(self):        
        location=self.getNextLocation()
        if location[0]==-1:
            return True
        else:
            for i in range(len(self.rv[location[0]*9+location[1]])):
                ch=self.rv[location[0]*9+location[1]][i]
                f1=self.removech(location[0],location[1],ch)                            
                self.board[location[0]][location[1]]=ch
                if f1==False:
                    k1=self.board[location[0]][location[1]]
                    self.board[location[0]][location[1]]=0
                    self.restore(location[0],location[1],k1)                                 
                elif self.algocsp() :
                    return True;
                else:                    
                   k=self.board[location[0]][location[1]]
                   self.board[location[0]][location[1]]=0
                   self.restore(location[0],location[1],k)                
            return False    
    
    def removech(self,posi,posj,choise):
        #row
        for i in range(9):
            if  posj!=i and self.board[posi][i]==0 and choise in self.rv[9*posi+i]:
                self.rv[9*posi+i].remove(choise)
                if len(self.rv[9*posi+i])==0:
                    return False                           
        #column
        for i in range(9):
            if  posi!=i and self.board[i][posj]==0 and choise in self.rv[9*i+posj]:
                self.rv[9*i+posj].remove(choise)
                if len(self.rv[9*i+posj])==0:
                    return False
        
        #check region
        bi=posi-(posi%3)
        bj=posj-(posj%3)
        for i in range(bi,bi+3):
            for j in range(bj,bj+3):
                if  i!=posi and j!=posj and self.board[i][j]==0 and choise in self.rv[9*i+j]:
                    self.rv[9*i+j].remove(choise)
                    if len(self.rv[9*i+j])==0:
                        return False
        return True
    def restore(self,posi,posj,choise):
        #row
        for i in range(9):
            if  choise not in self.rv[9*posi+i] and self.board[posi][i]==0 and self.isSafe(posi,i,choise):
                self.rv[9*posi+i].append(choise)                           
        #column
        for i in range(9):
            if  choise not in self.rv[9*i+posj] and self.board[i][posj]==0 and self.isSafe(i,posj,choise):
                self.rv[9*i+posj].append(choise)
        
        #check region
        bi=posi-(posi%3)
        bj=posj-(posj%3)
        for i in range(bi,bi+3):
            for j in range(bj,bj+3):
                if  choise not in self.rv[9*i+j] and self.board[i][j]==0 and self.isSafe(i,j,choise):
                    self.rv[9*i+j].append(choise)
    
                            
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
                             
    def printrv(self):
        for i in range(81):
            print(self.rv[i])
                          
# board=[
#     [0,1,6,3,0,8,4,2,0],
#     [8,4,0,0,0,7,3,0,0],
#     [3,0,0,0,0,0,0,0,0],
#     [0,6,0,9,4,0,8,0,2],
#     [0,8,1,0,3,0,7,9,0],
#     [9,0,3,0,7,6,0,4,0],
#     [0,0,0,0,0,0,0,0,3],
#     [0,0,5,7,0,0,0,6,8],
#     [0,7,8,1,0,3,2,5,0]
# ]
a=Sudoko_CSP(9,'board.txt')
a.print_board()
print("_____________________________")
a.algocsp()
a.print_board()
  
    