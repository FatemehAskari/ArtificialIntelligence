# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
        # print(successorGameState)
        # print("****")
        # print(newPos)
        # print("******")
        # print(newGhostStates)
        # print("****")
        # print(newScaredTimes)
        
        score=0
        gosdis=[]
        fooddis=[]
        food=newFood.asList()
        oldfood=currentGameState.getFood().asList()
        for i in newGhostStates:
            gosdis.append(manhattanDistance(newPos,i.getPosition()))
        for i in food:
            fooddis.append(manhattanDistance(newPos,i))
            
        mindisghos=float("inf")    
        if len(gosdis)>0:
            mindisghos=min(gosdis)
        if len(food)==0 and mindisghos>2:
            return float("inf") #we win forever
        score+=mindisghos
        if len(oldfood)>len(food) and mindisghos>2:
            score+=1000 #mitoonim ba aramesh felan ghaza bokhorim            
        minfood=float("inf")
        if len(fooddis)>0:
            minfood=min(fooddis)
        score-=minfood*2
        if mindisghos<4:
            score-=500
        score+=sum(newScaredTimes)/len(newScaredTimes)    
        return score                                   
            
def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.nodesCount = 0


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """  
    count=[0]
    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state        
        """           
        f1=self.minimax(gameState, 0, 0,self.count)[1] 
        # print(self.count[0])
        # self.nodesCount=self.count[0]
        # print(self.nodesCount)                              
        with open('MinimaxAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
        "*** YOUR CODE HERE ***"
        return f1
        util.raiseNotDefined()

    """
    tabe minimax 3 voroodi darad state hamoon vazeyati k hastim hast
    depth omghe ke oon state hast va agent yani alan nobat packman hast
    ya ghostha         
    """         
    def minimax(self,state,depth,agent,count):        
        #age dar in state bazi agent borde ya bakhte ya harkati nemitoone bokone
        #ya dar depth mojaz hastim evalatefuncytion va agent ke none bar migardoonim
        count[0]+=1
        self.nodesCount+=1
        # print(self.nodesCount)
        #print(count)
        if state.isWin() or state.isLose() or depth>=self.depth or  state.getLegalActions(agent)==0:
            return(self.evaluationFunction(state),None)
        #aghar nobat ghostha bood taban bayad kamtarin score mohasebe konim
        if agent>0:
            scoreghost=float("inf")
            act=state.getLegalActions(agent)[0]
            for i in state.getLegalActions(agent):
                #aghar nafar badi packman nist:
                if (agent+1)%(state.getNumAgents())>0:
                    (s1,ag)=self.minimax(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()),count)                    
                    #age harkat badi packmane:
                else:
                    (s1,ag)=self.minimax(state.generateSuccessor(agent, i),depth+1,0,count)
                      
                if s1<scoreghost:
                    scoreghost=s1
                    act=i
            if scoreghost is not float("inf"):
                return(scoreghost,act)
        else:                
            scorepack=float("-inf")
            act1=state.getLegalActions(agent)[0]                
            for i in state.getLegalActions(agent):
                (s1,ag)=self.minimax(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()),count)
                if s1>scorepack:
                    scorepack=s1
                    act1=i
            if scorepack is not  float("-inf"):
                return(scorepack,act1)    
                                                  
            
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    count=[0]
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        f1=self.alphabeta(gameState, 0, 0,float("-inf"), float("inf"))[1]
        with open('AlphaBetaAgent.txt', 'a') as f:
            f.write(f"\n {self.nodesCount}")
        "*** YOUR CODE HERE ***"
        return f1        
        util.raiseNotDefined()
        
    def alphabeta(self,state,depth,agent,alpha,beta):                                                               
        #age dar in state bazi agent borde ya bakhte ya harkati nemitoone bokone
        #ya dar depth mojaz hastim evalatefuncytion va agent ke none bar migardoonim
        self.nodesCount+=1
        # print(self.nodesCount)
        if state.isWin() or state.isLose() or depth>=self.depth or  state.getLegalActions(agent)==0:
            return(self.evaluationFunction(state),None)
        #aghar nobat ghostha bood taban bayad kamtarin score mohasebe konim
        if agent>0:
            hadbala=float("inf")
            act=state.getLegalActions(agent)[0]
            for i in state.getLegalActions(agent):
                #aghar nafar badi packman nist:
                if (agent+1)%(state.getNumAgents())>0:
                    (s1,ag)=self.alphabeta(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()),alpha,beta)                    
                    #age harkat badi packmane:
                else:
                    (s1,ag)=self.alphabeta(state.generateSuccessor(agent, i),depth+1,0,alpha,beta)
                      
                if s1<hadbala:
                    hadbala=s1
                    act=i
                if hadbala<alpha:
                   return(hadbala,act)
                beta=min(hadbala,beta)    
            if hadbala is not float("inf"):
                return(hadbala,act)
        else:                
            hadpayeen=float("-inf")
            act1=state.getLegalActions(agent)[0]                
            for i in state.getLegalActions(agent):
                (s1,ag)=self.alphabeta(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()),alpha,beta)
                if s1>hadpayeen:
                    hadpayeen=s1
                    act1=i
                if hadpayeen>beta:
                    return(hadpayeen,act1)
                alpha=max(hadpayeen,alpha)                    
            if hadpayeen is not  float("-inf"):
                return(hadpayeen,act1)             


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.expectimax(gameState, 0, 0)[1]
        util.raiseNotDefined()
    def expectimax(self,state,depth,agent):
        if state.isWin() or state.isLose() or depth==self.depth or  state.getLegalActions(agent)==0:
            return(self.evaluationFunction(state),None)
        
        if agent==0:
            scorepack=float("-inf")
            act1=state.getLegalActions(agent)[0]                
            for i in state.getLegalActions(agent):
                (s1,ag)=self.expectimax(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()))
                if s1>scorepack:
                    scorepack=s1
                    act1=i
            if scorepack is not  float("-inf"):
                return(scorepack,act1)
        else:
            scoreghostsum=0
            act=state.getLegalActions(agent)[0]
            for i in state.getLegalActions(agent):
                #aghar nafar badi packman nist:
                if (agent+1)%(state.getNumAgents())>0:
                    scoreghostsum+=(self.expectimax(state.generateSuccessor(agent, i),depth,(agent+1)%(state.getNumAgents()))[0])*(1/(len(state.getLegalActions(agent))))                   
                    #age harkat badi packmane:
                else:
                    scoreghostsum+=(self.expectimax(state.generateSuccessor(agent, i),depth+1,0)[0])*(1/(len(state.getLegalActions(agent))))
                act=i   
            return (scoreghostsum,act)
                                
def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    score=0
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    capsules=currentGameState.getCapsules()
    Walls=currentGameState.getWalls()
    
    fooddis=[]
    capsuldis=[]
    for g in newGhostStates:
        ghostdis=manhattanDistance(newPos,g.getPosition())
        if ghostdis<2:
            if g.scaredTimer!=0:
                score+=1000/(ghostdis+1)
            else:
                score-=1000/(ghostdis+1)
    for f in newFood.asList():
        fooddis.append(manhattanDistance(newPos,f))
    for c in capsules:
        capsuldis.append(manhattanDistance(c,newPos))
    
    if min(capsuldis +[float(100)])<5:
        score +=500/ (min(capsuldis))

    for cap in capsules:
        if cap[0] == newPos[0] and cap[1]==newPos[1]:
            score += 600
    
    minfood=min(fooddis+[float(100)])
    return score + 1/minfood - len(fooddis)*10     
                                             
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction


