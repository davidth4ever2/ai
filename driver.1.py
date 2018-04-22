from collections import deque 

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
		
		self.nodeList.append(inputNode)
		self.nodeSet= set(self.nodeList)



class Frontier:
	
	queue = deque() 
	numberOfNodes = 0

        def new(self,initNode):
		self.numberOfNodes = self.numberOfNodes + 1
		self.queue.append(initNode)

	def pop(self):

		self.numberOfNodes = self.numberOfNodes-1
		return self.queue.popleft()
		
        def append(self,nodeToAdd):

		self.queue=deque.append(nodeToAdd)
		self.numberOfNodes = self.numberOfNodes + 1

	def isEmpty(self):
		
		returnValue = False

		if(self.numberOfNodes==0):

			returnValue =  True
		else:
			returnValue =  False
		
		return returnValue

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
	
	actions = ["Up","Down","Left","Right"]
	nodeList = list()
	frontier = Frontier()
        initialNode = InitialNode()
	frontier.new(initialNode)
        
	print(frontier.numberOfNodes)
	print(str(frontier.isEmpty()))

	while not(frontier.isEmpty()):
                 
		startNode = frontier.pop() # add to fringe

		print("expanding " + str(startNode.state))
		print("comparing to " + str(TargetNode().state))

		explored = Explored()
                explored.add(startNode)

		if(startNode.state == TargetNode().state):

			print("solution found")
			print(startNode.pathCost)
			return startNode.state

		for action in actions:
			print(action)
			node       = Node(startNode)
			returnNode = node.childNode(node.parentState,action)

			print(str( type(returnNode.state)) + action)
			frontier.new(returnNode)
				

#		print(frontier.numberOfNodes)

bfs()

#startNodeTwo = InitialNode()
#nodetwo = Node(startNodeTwo)
#returnNodeTwo = nodetwo.childNode(nodetwo.parentState,"Down")
#startNodeThree = InitialNode()
#nodethree = Node(startNodeThree)
#returnNodeThree = nodethree.childNode(nodethree.parentState,"Left")








