from Algorithm import Algorithm


class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        self.frontier=[]
        self.explored_set=[]
        self.path=[]
        final=self.get_initstate_and_goalstate(snake)[1]
        self.frontier.append(self.get_initstate_and_goalstate(snake)[0])
        
        while self.frontier:
            min=9999999
            l=0
            for i in range(len(self.frontier)):
                if self.frontier[i].f<min:
                    min=self.frontier[i].f
                    l=i
            nodel=self.frontier.pop(l)
            if nodel.x==final.x and nodel.y==final.y:
                return self.get_path(nodel)
            
            self.explored_set.append(nodel)
            for i in self.get_neighbors(nodel):
                if (i not in self.explored_set or self.manhattan_distance(final,i)+nodel.g+1<=i.f ) and self.outside_boundary(i)==False and self.inside_body(snake,i)==False:
                    if i not in self.frontier:
                        self.frontier.append(i)
                        i.h=self.manhattan_distance(final,i)
                        i.g=nodel.g+1
                        i.f=i.h+i.g
                        i.parent=nodel
                    elif nodel.g<i.g:
                        i.g=nodel.g+1
                        i.f=i.h+i.g
                        i.parent=nodel                                                                                   
        return None
