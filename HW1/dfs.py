from collections import defaultdict

T=False
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFSutil(self,u,visited,v):                        
        for child in self.graph[u]:
            visited.append(u)
            if child  not in visited:                                                        
                self.DFSutil(child,visited,v)
    def DFS(self,u,v):
        visited=[]
        path=[]
        # self.DFSutil(u,visited,v)
        #print(self.printAllPathsUtil(u, v, visited, path))
        print(self.DFS1(u,v,visited,path))
        
    def printAllPathsUtil(self, u, d, visited, path):
     
        # Mark the current node as visited and store in path
        visited.append(u) 
        path.append(u)
        
        if u == d:
            print (path)
            return path
        else:
            for i in self.graph[u]:
                if i not in visited:
                    self.printAllPathsUtil(i, d, visited, path)                     
        path.pop()
    def DFS1(self,s,final,visited,path):
        path.append(s)
        visited.append(s)
        if s==final:
            return path                 
        for i in self.graph[s]:
            if i not in visited:
                result=self.DFS1(i,final,visited,path)
                if result is not None:
                    return result
        path.pop()
        return None
        
g=Graph()
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
g.DFS('A','G')

  
                




                
                 
                