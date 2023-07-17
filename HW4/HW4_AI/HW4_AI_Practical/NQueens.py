from random import randrange

class NQueens:
    def __init__(self, N):
        self.N = N

    def initial(self):
        ''' Returns a random initial state '''
        a=tuple(randrange(self.N) for i in range(self.N))
        return a

    def goal_test(self, state):
        ''' Returns True if the given state is a goal state '''
        n=len(state)
        for i in range(n-1):
            for j in range(i+1,n):
                if state[i]==state[j]:
                    return False
                elif state[i]+i==state[j]+j:
                    return False
                elif state[j]-state[i]==j-i:
                    return False  
        return True
    def value(self, state):
        ''' Returns the value of a state. The higher the value, the closest to a goal state '''
        value1=0
        n=len(state)
        for i in range(n-1):
            for j in range(i+1,n):
                if state[i]!=state[j] and state[i]+i!=state[j]+j and state[j]-state[i]!=j-i:
                    value1+=1
        return value1                
                

    def neighbors(self, state):
        ''' Returns all possible neighbors (next states) of a state '''
        ans=[]
        n=len(state)
        for i in range(n):
            for j in range(n):
                y=list(state)
                if j!=state[i]:
                    y[i]=j
                    ans.append(y)
        return ans                