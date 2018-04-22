from collections import deque 

class BookKeeper:

	parent_list = list()
	path_to_goal = list()
	cost_of_path = 0
	nodes_expanded = 0
	search_depth = 0
	max_search_depth = 0
	running_time = 0
	max_ran_usage = 0

	def __init__(self):

	
		parent_list      = list()
		path_to_goal     = list()
		cost_of_path     = 0
		nodes_expanded   = 0
		search_depth     = 0
		max_search_depth = 0
		running_time     = 0
		max_ran_usage    = 0
	
	def getSearchDepth(self):
		testSet = set(self.parent_list)		

		print(str(testSet))

		return len(testSet)
		

	
class Util:
	
	copiedList = list()
	def __init__(self):

		self.copiedList=list()


	def copyList(self,inputlist):
		
		
		for row in inputlist:
			
			self.copiedList.append( [x*1 for x in row] ) # use a comprehesion to insure a new list

		return self.copiedList			
	
class Explored:
	
	nodeSet  = set()
	nodeList = list() 

	def add(self,inputNode):
		
		self.nodeList.append(str(inputNode.state))
		self.nodeSet= set(self.nodeList)

	def found(self,inputNode):

		if(str(inputNode.state) in self.nodeSet):
			
			return True
		else:
			return False




class Frontier:
	
	queue = deque() 
	numberOfNodes = 0

        def new(self,initNode):
		self.numberOfNodes = self.numberOfNodes + 1
		self.queue.append(initNode.state)

	def pop(self):

		self.numberOfNodes = self.numberOfNodes-1
		
		return self.queue.popleft()
		
        def append(self,nodeToAdd):

		self.queue=deque.append(nodeToAdd.state)
		self.numberOfNodes = self.numberOfNodes + 1

	def isEmpty(self):
		
		returnValue = False

		if(self.numberOfNodes==0):

			returnValue =  True
		else:
			returnValue =  False
		
		return returnValue
	
	def found(self, inputNode):
		
		if(self.queue.count(inputNode.state) > 0):
			
			return True
		else:
			return False

	
		  

class InitialNode:

	
	parentState = None	
	state = [[1,2,5],[3,4,0],[6,7,8]]
	stepCost = 1
	action   = "NoAction"
	pathCost = 0

	

class TargetNode:
		
	state = [[0,1,2],[3,4,5],[6,7,8]]


	def goalTest(self,testNode):

		if(testNode.state==self.state):

			return True
		else:
			return False
		
class Node:

	state        = list()
	parentState  = list()
	pathCost     = 0
	action       = ""

        
	
	def __init__(self,inputNode): ## expansion mean initial a new Node from a node in the Frontier

	
		self.parentState   = inputNode.state
		self.action        = inputNode.action
		self.pathCost      = inputNode.pathCost + 1
		
			
	def childNode(self,inputState,inputAction):
		
		
		util = Util()
		currentState = util.copyList(inputState)
		currentdoor  = 0
                currentfloor = 0

		for row in inputState:
			
 			try:

				currentdoor = row.index(0)
				currentfloor = currentState.index(row)
         
			except ValueError:
			
				continue 


		if(inputAction=="Up"and currentfloor <> 0):

                        temp = currentState[currentfloor-1][currentdoor]
			currentState[currentfloor][currentdoor] = temp
			currentState[currentfloor-1][currentdoor] = 0

           		returnNode              = Node(self)
			returnNode.action       ="Up"
			returnNode.parentState  = self.parentState
			returnNode.state        = currentState
			return returnNode

		elif(inputAction=="Down" and currentfloor <> 2):
			
			temp = currentState[currentfloor+1][currentdoor]
			currentState[currentfloor][currentdoor]= temp			
			currentState[currentfloor+1][currentdoor] = 0
			 
			returnNode              = Node(self)
			returnNode.action       = "Down"
			returnNode.parentState  = self.parentState
			returnNode.state        = currentState  
			
			return returnNode
		elif(inputAction=="Left" and currentdoor <> 0):
			
			temp = currentState[currentfloor][currentdoor-1]
			currentState[currentfloor][currentdoor]=temp
			currentState[currentfloor][currentdoor-1] = 0

			returnNode              = Node(self)
			returnNode.action       = "Left"
			returnNode.parentState  = self.parentState
			returnNode.state        = currentState
		
			return returnNode

		elif(inputAction=="Right" and currentdoor <> 2):
			
			temp = currentState[currentfloor][currentdoor+1]
			currentState[currentfloor][currentdoor]=temp
			currentState[currentfloor][currentdoor+1] = 0

			returnNode              = Node(self)
			returnNode.action       = "Right"
			returnNode.parentState  = self.parentState
			returnNode.state        = currentState

			return returnNode
		else:
			returnNode = Node(self)
			returnNode.action = inputAction
			returnNode.parentState = self.parentState
			returnNode.state       = self.parentState
 

			return returnNode		


def bfs():

	testcount = 0
	bookKeeper = BookKeeper()
	actions = ["Up","Down","Left","Right"]
	nodeList = list()
	frontier = Frontier()
        initialNode = InitialNode()
	frontier.new(initialNode)
        
	print(frontier.numberOfNodes)
	print(str(frontier.isEmpty()))

	while not(frontier.isEmpty()):
		
		startNode = InitialNode()
                startNode.state = frontier.pop() # add to fringe
		explored = Explored()
                explored.add(startNode)

		if(startNode.state == TargetNode().state):

			print("nodes.expanded:" + str(bookKeeper.nodes_expanded))

			print( "path to goal " + str(parentNode.parentState))
			print( "solution" + str(startNode.state))

			return startNode.state
                 
		
                bookKeeper.nodes_expanded = bookKeeper.nodes_expanded + 1

		print(bookKeeper.nodes_expanded)
		
		
		testcount = testcount + 1
		for action in actions:
			
			node       = Node(startNode)
			returnNode = node.childNode(node.parentState,action)
			
			if( not( explored.found(returnNode) ) and not( frontier.found(returnNode) ) ):

				print("adding to the frontier" + str(returnNode.state))
		
				frontier.new(returnNode)


bfs()

#startNodeTwo = InitialNode()
#nodetwo = Node(startNodeTwo)
#returnNodeTwo = nodetwo.childNode(nodetwo.parentState,"Down")
#startNodeThree = InitialNode()
#nodethree = Node(startNodeThree)
#returnNodeThree = nodethree.childNode(nodethree.parentState,"Left")








