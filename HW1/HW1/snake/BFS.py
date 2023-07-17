from asyncio.windows_events import NULL
from collections import deque
from pickle import FALSE, TRUE
import queue
from Utility import Node
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)    
    def run_algorithm(self, snake):   
        self.frontier = []
        self.explored_set = []
        self.path = []      
        final=self.get_initstate_and_goalstate(snake)[1]
        self.frontier.append(self.get_initstate_and_goalstate(snake)[0])
        self.explored_set.append(self.get_initstate_and_goalstate(snake)[0])     
        while self.frontier :           
            s12=self.frontier.pop(0)             
            for i in self.get_neighbors(s12):                            
                if i not in self.explored_set and self.outside_boundary(i)==False and self.inside_body(snake,i)==False:
                    # print(i.x," ",i.y)                                                                    
                    self.explored_set.append(i)
                    self.frontier.append(i)
                    i.parent=s12
                if i.x==final.x and i.y==final.y:   
                    return self.get_path(i)


