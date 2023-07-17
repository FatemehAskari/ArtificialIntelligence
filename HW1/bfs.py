from collections import defaultdict
from pickle import TRUE
import queue 
class Graph:
    def __init__(self,number):
        self.graph=defaultdict(list)
        self.number=number
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,s,g):
        visited=[False]*(self.number)        
        queue=[]
        queue.append(s)
        visited[ord(s)-65]=True
        t=False
        while queue and t==False:
            if t==TRUE:
                break
            s=queue.pop(0)
            print(s,end =" ")
            
            for i in self.graph[s] :
                if visited[ord(i)-65] ==False:
                    queue.append(i)
                    visited[ord(i)-65]=True           
                    if i==g:
                        t=True
                        break;
        if t==True:
             print(g,end =" ")
        else:
            print('masiri yaft nashod')                
g=Graph(7)
g.addedge('A','B')
g.addedge('A','C')
g.addedge('B','D')
g.addedge('C','D')
g.addedge('B','C')
g.addedge('D','E')
g.addedge('D','F')
g.addedge('D','G')
g.addedge('E','G')
g.addedge('F','G')
g.BFS('A','G')
                
                    