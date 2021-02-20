import matrix_generation2
import numpy as np



class PointSearchProblem:
	"""
	A search problem defines the state space, start state, goal test, successor
	function and cost function.  This search problem can be used to find paths
	to a particular point on the n dimensional matrix.

	The state space consists of (a1,a2,a3....an) positions in a n dimensional matrix.
	"""
	#d = int(input("\n\tThe dimension of your world : \t"))
	
	def __init__(self,dimension =3,shape=(3,3,3), costFn = lambda x,y : 1, goal = None, start=None) :
		"""
		Stores the start and goal.

		costFn: A function from a current state to nextstate(tuple) to a non-negative number
		goal: A position in the n dimensional matrix
		"""
#self.walls = gameState.getWalls()
		self.dimension = dimension
		self.matrixWorld = matrix_generation2.generateDynamicMatrix(dimension,shape)
		#print(self.matrixWorld)
		self.startState = start
		if start == None or len(start)!= dimension: self.startState = tuple([1]*dimension)
		self.goal = goal
		if goal == None or len(goal)!= dimension: self.goal = tuple([dimension]*dimension)
		self.matrixWorld[self.startState] = False
		self.matrixWorld[self.goal] = False
		self.costFn = costFn
		print(self.goal)
	def getMatrixWorld (self):
		return self.matrixWorld
	def getStartState(self) :
		return self.startState

	def isGoalState(self, state):
		isGoal = state == self.goal
		return isGoal

	def getSuccessors(self,state):
		successors = []
		for _dimension in range(self.dimension-1,-1,-1):
			nextStateUp = list(state)#As tuples are immutable
			nextStateDown = list(state)
			nextStateUp[_dimension] += 1
			nextStateDown[_dimension] -= 1
			
			if not self.matrixWorld[tuple(nextStateUp)]: 
				successors.append([tuple(nextStateUp),str(self.dimension - _dimension)+"+",self.costFn(state,nextStateUp)])#change in 1D is change in 6th index of state tuple
			if not self.matrixWorld[tuple(nextStateDown)]: 
				successors.append([tuple(nextStateDown),str(self.dimension -_dimension)+"-",self.costFn(state,nextStateDown)])

		return successors




