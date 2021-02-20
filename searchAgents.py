#import search
#import sys
#import inspect
import heapq, random
#import cStringIO
"Utility codes"
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

"From here the search algorithm code starts : "
#def costFn(currentState,nextState):
#    return 1

def getThefirstPAth(dictVisited ,startState, goalState):
    ''' This function backtracks a path from goal state to start state '''
    pathInReverse = []
    currentState = goalState # Current State varies to make the path go closer to the start state
    while True :
        parentState,directionFromParent = dictVisited[currentState]
        pathInReverse.append(directionFromParent)
        currentState = parentState
        if (parentState==startState):
            break
       
    return pathInReverse[::-1]

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    returnListOfPath = [] # Stores directions
    dictVisited = {} # key : the state , value : [parentState , direction from parent state]
    startState = problem.getStartState()#Initializing Data structure from util.py
    queueFringe = Queue()
    queueFringe.push([startState,'Unknown',0]) #appending with unknown for uniformity.
    dictVisited[startState] = 1
    # currentState = startState
    
    # If start state is itself a goal state then we return null list
    if problem.isGoalState(startState):
        return returnListOfPath
    # Break the loop if Fringe is empty or goal state reached
    while (not queueFringe.isEmpty()):
        firstState = queueFringe.pop()
        #print(topState)
        currentState,directionFromParent,costOfPath = firstState #The Split
        if(problem.isGoalState(currentState)):
            returnListOfPath = getThefirstPAth(dictVisited,startState,currentState) # Backtracks the path to reach goal state
            return returnListOfPath
        nextSuccessors = problem.getSuccessors(currentState)
        for iSuccessor in nextSuccessors:# can be done in reverse too
            nextState,directionToReach,costToPath = iSuccessor
            if(not dictVisited.__contains__(nextState)):# Avoiding cycles in graph
                queueFringe.push(iSuccessor)
                #print("pushed",nextState)
                dictVisited[nextState] = [currentState,directionToReach]
            if(problem.isGoalState(nextState)):
            		returnListOfPath = getThefirstPAth(dictVisited,startState,nextState) # Backtracks the path to reach goal state
            		return returnListOfPath
            		
        
    return returnListOfPath #Null return
    

def depthFirstSearch(problem):
    
    "*** YOUR CODE HERE ***"
    returnListOfPath = []
    dictVisited = {}
    startState = problem.getStartState()
    stackFringe = Stack() #Initializing Data structure from util.py
    stackFringe.push([startState,'Unknown',0])
    # currentState will be the startState
    
    #if start state is itself a goal state then we return null list
    if problem.isGoalState(startState):
        return returnListOfPath

    #loops until either the fringe is empty or break function is called
    while(not stackFringe.isEmpty()):
        topState = stackFringe.pop()
        #print(topState)
        currentState,directionFromParent,costOfPath = topState #split
        if(problem.isGoalState(currentState)):
            returnListOfPath.append(directionFromParent)
            return returnListOfPath[1:] #Slicing from first element as if n nodes in a path has n-1 edges.
        if(dictVisited.__contains__(currentState)):#Avoiding Cycles in a graph
            #print(currentState)
            if len(returnListOfPath)!=0:
                returnListOfPath.pop()
        else :
            dictVisited[currentState] = True
            stackFringe.push(topState)
            nextSuccessors = problem.getSuccessors(currentState)
            flag=False
            for iSuccessor in nextSuccessors:#can be done in reverse too
                nextState,directionToReach,costToPath = iSuccessor
                if(not dictVisited.__contains__(nextState)):#check
                    stackFringe.push(iSuccessor)
                    flag =True
            if(flag):
                returnListOfPath.append(directionFromParent)
            else:
                #If no new unvisited nodes to add in stack
                stackFringe.pop()
    return returnListOfPath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #return breadthFirstSearch(problem)

    returnListOfPath = [] # Stores directions
    dictCostTillNode = {} # key : the state , value : The prefix-sum cost
    dictPopped = {}
    dictVisited = {} # key : the state , value : [parentState , direction from parent state]
    startState = problem.getStartState()#Initializing Data structure from util.py
    pqueueFringe = PriorityQueue()
    dictCostTillNode[startState] = 0
    dictVisited[startState] = 1
    pqueueFringe.push(startState,dictCostTillNode[startState]) #appending with unknown for uniformity.
    

    # If start state is itself a goal state then we return null list
    if problem.isGoalState(startState):
        return returnListOfPath
    # Break the loop if Fringe is empty or goal state reached
    while (not pqueueFringe.isEmpty()):
        firstState = pqueueFringe.pop()
        currentState = firstState
        dictPopped[currentState] = True 
        if(problem.isGoalState(currentState)):
            returnListOfPath = getThefirstPAth(dictVisited,startState,currentState) # Backtracks the path to reach goal state
            return returnListOfPath
        costTillCurrent = dictCostTillNode[currentState]
        nextSuccessors = problem.getSuccessors(currentState)
        for iSuccessor in nextSuccessors:# can be done in reverse too
            nextState,directionToReach,costToPath = iSuccessor
            if(not dictPopped.__contains__(nextState)):# Avoiding cycles in graph
                if(dictCostTillNode.__contains__(nextState)):
                    if( dictCostTillNode.get(nextState) > costToPath + costTillCurrent):
                        dictVisited[nextState] = [currentState,directionToReach]
                        dictCostTillNode[nextState] = costToPath + costTillCurrent
                else:
                    dictCostTillNode[nextState] = costToPath + costTillCurrent
                    dictVisited[nextState] = [currentState,directionToReach]
                pqueueFringe.update(nextState,dictCostTillNode[nextState])


    return returnListOfPath

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    print("\n Alert : Null heuristic called !\n")
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #heuristic(state,problem)
    returnListOfPath = [] # Stores directions
    dictCostTillNode = {} # key : the state , value : The prefix-sum cost
    dictPopped = {}
    dictVisited = {} # key : the state , value : [parentState , direction from parent state]
    startState = problem.getStartState()#Initializing Data structure from util.py
    pqueueFringe = PriorityQueue()
    dictCostTillNode[startState] = 0 
    dictVisited[startState] = 1
    pqueueFringe.push(startState,dictCostTillNode[startState]+ heuristic(startState,problem)) #appending with unknown for uniformity.
    

    # If start state is itself a goal state then we return null list
    if problem.isGoalState(startState):
        return returnListOfPath
    # Break the loop if Fringe is empty or goal state reached
    while (not pqueueFringe.isEmpty()):
        firstState = pqueueFringe.pop()
        currentState = firstState
        dictPopped[currentState] = True 
        if(problem.isGoalState(currentState)):
            returnListOfPath = getThefirstPAth(dictVisited,startState,currentState) # Backtracks the path to reach goal state
            return returnListOfPath
        costTillCurrent = dictCostTillNode[currentState]
        nextSuccessors = problem.getSuccessors(currentState)
        for iSuccessor in nextSuccessors:# can be done in reverse too
            nextState,directionToReach,costToPath = iSuccessor
            if(not dictPopped.__contains__(nextState)):# Avoiding cycles in graph
                if(dictCostTillNode.__contains__(nextState)):
                    if( dictCostTillNode.get(nextState) > costToPath + costTillCurrent):
                        dictVisited[nextState] = [currentState,directionToReach]
                        dictCostTillNode[nextState] = costToPath + costTillCurrent
                else:
                    dictCostTillNode[nextState] = costToPath + costTillCurrent
                    dictVisited[nextState] = [currentState,directionToReach]
                pqueueFringe.update(nextState,dictCostTillNode[nextState]+ heuristic(nextState,problem))


    return returnListOfPath
'''
def caller(dimension =3,start = (1,1,1),goal = (3,3,3),costFn = lambda x,y :1 ,agentAlgo = "breadthFirstSearch" ):
    problem = search.PointSearchProblem(dimension = dimension ,start = start ,goal = goal ,costFn = costFn)
    if(agentAlgo == "breadthFirstSearch"):
        return [problem.getMatrixWorld(), breadthFirstSearch(problem)]
    return None
'''
# startState = problem.getStartState()
# successorsList =  problem.getSuccessors(startState)
# print(successorsList)
# answer = breadthFirstSearch(problem)
# print(answer)