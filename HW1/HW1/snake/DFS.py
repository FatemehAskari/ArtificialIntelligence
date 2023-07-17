from tkinter import NONE
from tkinter.messagebox import NO
from unittest import result
from Utility import Node
from Algorithm import Algorithm



class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)
        
    def run_algorithm(self, snake):
        if len(self.path) > 0:
            # print(len(self.path))
            # print(self.path[len(self.path)-1].x,' ',self.path[len(self.path)-1].y)        
            path = self.path.pop()                       
            if self.inside_body(snake, path):
                self.path = []
            else:                
                return path   
        self.frontier = []
        self.explored_set = []
        self.path = []     
        final=self.get_initstate_and_goalstate(snake)[1]
        s=self.get_initstate_and_goalstate(snake)[0]
        return self.DFS(s,final,snake)
        
    def DFS(self,s,final,snake):
        if s.x==final.x and s.y==final.y:                       
            return self.get_path(s)
        if s in self.explored_set:
            return None
        self.explored_set.append(s)              
        for i in self.get_neighbors(s):            
            if i not in self.explored_set and self.outside_boundary(i)==False and self.inside_body(snake,i)==False:
                i.parent=s
                result=self.DFS(i,final,snake)
                if result is not None:
                    return result
        return None



