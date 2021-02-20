import searchAgents
import search
import view3D
import random
#import matplotlibAnimation
'''
dimensionInput = int(input("\n\tDimension : \t"))
worldShapeInput = tuple(map(int,input("\t Enter World Shape nd,n-1d,n-2d,with delimeter comma  :\t").split(",")))
startInput = tuple(map(int,input("\t Enter Start State nd,n-1d,n-2d with delimeter comma  :\t").split(",")))
goalInput = tuple(map(int,input("\t Enter Target State nd,n-1d,n-2d with delimeter comma  :\t").split(",")))
'''
def costFunctionRandom(currentState,nextState):
	return random.randint(1,10)

def costFunction(currentState,nextState):
	for i in range(len(currentState)):
		if currentState[i] != nextState[i]:
			return 2**i
	return 1
def heuristicFunction(currentState,problem):
	"This is general purpose manhatten distance heuristic"
	goalConfiguration = problem.goal
	heuristicValue = 0
	for i in range(len(currentState)):
		heuristicValue += abs(currentState[i] - goalConfiguration[i])
	return heuristicValue
#start = (z,y,x)
#getMatrixWorld
def getDirections(dimension = 3,worldShape = (3,3,3),start = (1,1,1),goal = (3,3,3),algoIndex = 0):
	problem = search.PointSearchProblem(dimension = dimension ,shape = worldShape, start = start ,goal = goal,costFn = costFunctionRandom)
	directionList = []
	if algoIndex == 0:
		directionList = searchAgents.breadthFirstSearch(problem)
	elif algoIndex ==1 :
		directionList = searchAgents.uniformCostSearch(problem)
	elif algoIndex ==2 :
		directionList = searchAgents.aStarSearch(problem,heuristic = heuristicFunction)
	elif algoIndex == 3:
		directionList = searchAgents.depthFirstSearch(problem)
	#print("FF",directionList)
	getDirections.directionList_ =directionList
	getDirections.problem_ = problem
	return [directionList,problem.getMatrixWorld()]

def visualIt():
	view3D.visualize3D(matrixWorld = getDirections.problem_.getMatrixWorld() , start = getDirections.problem_.getStartState(),goal = getDirections.problem_.goal,directionList = getDirections.directionList_) 

#directionList2 = searchAgents.depthFirstSearch(problem)
'''
directionList3 = searchAgents.uniformCostSearch(problem)
directionList4 = searchAgents.aStarSearch(problem,heuristic = heuristicFunction)


print("BFS returned :" ,len(directionList))
#print("DFS returned :",len(directionList2))
print("UCS returned :",len(directionList3))
print("A* returned :" ,len(directionList4))

print("BFS returnedList :" ,directionList)
print("UCS returnedList :",directionList3)
print("A* returnedList :" ,directionList4)
view3D.visualize3D(matrixWorld = problem.getMatrixWorld() , start = problem.getStartState(),goal = problem.goal,directionList = directionList4) 
'''