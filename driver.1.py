from collections import deque
import time
import sys
import resource

class FrontierStack:

	stackSet = set()
	stack = list()
	numberOfNodes = 0
	
	def __init__(self,inputList):
		self.numberOfNodes = self.numberOfNodes + 1
		self.stack.append(inputList)

	def isEmpty(self):
	
		
		if( len(self.stack)==0):

			return True
		else:
			return False
	def pop(self):
		
		return	self.stack.pop()

	def push(self, inputNode):

		self.numberOfNodes = self.numberOfNodes + 1
		self.stack.append(inputNode)
		
		self.stackSet = set(self.stack)

	def found(self,inputNode):
		
		
		f = {inputNode.state==x.state for x in self.stackSet}
		
		if(True in f):
	
			return True
		else:
			
			return False
		
		
		
	
	
	
class BookKeeper:

	parent_list = list()
	path_to_goal = list()
	cost_of_path = len(path_to_goal)
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

	def getCostOfPath(self):
		self.cost_of_path = len(self.path_to_goal)

		return self.cost_of_path

	
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
	nodecount = 0
	def add(self,inputNode):

		self.nodecount= self.nodecount+1
		self.nodeList.append(inputNode)
		self.nodeSet= set(self.nodeList)

	def found(self,inputNode):

		a = { a.state==inputNode.state for a in self.nodeSet }
		
		if True in a:

			return True

	def getParentNode(self,inputNode):
                
	       	actions = list()
		node    = inputNode
		
		while not(node.action=="NoAction"):
			if not(node.action=="NoAction"):
				actions.append(node.action) 
				node  = [x for x in self.nodeList if x.state==node.parentState][0]
		actions.reverse()
		
		return actions
#		node = [x for x in self.nodeList if x.a[0].state == node.parentState]

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
	startTime = time.time()
	testcount = 0
	bookKeeper = BookKeeper()
	actions = ["Up","Down","Left","Right"]
	nodeList = list()
	frontier = StackFrontier()
        initialNode = InitialNode()
	frontier.new(initialNode)       
	print(frontier.numberOfNodes)
	print(str(frontier.isEmpty()))
	while not(frontier.isEmpty()):
		
	
                startNode = frontier.pop() # add to fringe
		explored  = Explored()
                explored.add(startNode)

		
		print( "goalTestaction > l "   + str(startNode.action))

		if(startNode.state == TargetNode().state):

			bookKeeper.path_to_goal = explored.getParentNode(startNode)

			
			print( "path_to_goal:"   + str(bookKeeper.path_to_goal))
			print( "cost_of_path:"   + str(bookKeeper.getCostOfPath()))
			print( "nodes_expanded:" + str(bookKeeper.nodes_expanded))
			print( "search_depth:"   + str(bookKeeper.getCostOfPath()))
			print( "max_search_depth:" + str(bookKeeper.getCostOfPath() + 1))
			print( "running_time:"+   str( (time.time()-startTime)))
			usage = resource.getrusage(resource.RUSAGE_SELF)

			print("max_ram_usage:" +  str(getattr(usage,'ru_maxrss')))
			explored.getParentNode(startNode)		
			return startNode.state
                 
		
                bookKeeper.nodes_expanded = bookKeeper.nodes_expanded + 1

		print(bookKeeper.nodes_expanded)
		
		
		testcount = testcount + 1
		for action in actions:
			
			node       = Node(startNode)
			returnNode = node.childNode(node.parentState,action)
			
			if( not( explored.found(returnNode) ) and not( frontier.found(returnNode) ) ):
				
				print("adding to the frontier" + str(returnNode.state))
				print("adding to the frontier this parent " + str(returnNode.parentState))
				print("adding to the frontier this action " + str(returnNode.action))
				frontier.new(returnNode)



def dfs():
	bookKeeper = BookKeeper()
	initialNode = InitialNode()
	frontier = FrontierStack(initialNode)
	explored = Explored()
	actions = ["Up","Down","Left","Right"]

	while not(frontier.isEmpty()):
		
		startNode = frontier.pop()
		explored.add(startNode)

		if(TargetNode.state == startNode.state):
		
			print("found solution")
			print(startNode.state)
			print("node_expanded:" + str(bookKeeper.nodes_expanded))
			print("explored" + str(explored.nodecount))
			return startNode.state


		for action in actions:
			bookKeeper.nodes_expanded = bookKeeper.nodes_expanded + 1
			node       = Node(startNode)
			returnNode = node.childNode(node.parentState,action)
	
			if (explored.found(returnNode)!=True):
			
				print("adding to the frontier" + str(returnNode.state))
				print("adding to the frontier this parent " + str(returnNode.parentState))
				print("adding to the frontier this action " + str(returnNode.action))
				print("currenNode count " + str(frontier.numberOfNodes))
				frontier.push(returnNode)



def dfs2():

		
	bookKeeper = BookKeeper()
	initialNode = InitialNode()
	frontier = FrontierStack(initialNode)
	explored = Explored()
	actions = ["Up","Down","Left","Right"]

	while not(frontier.isEmpty()):
		
		startNode = frontier.pop()
		explored.add(startNode)

		if(TargetNode.state == startNode.state):
		
			print("found solution")
			print(startNode.state)
			print("node_expanded:" + str(bookKeeper.nodes_expanded))
			print("explored" + str(explored.nodecount))
			return startNode.state


		for action in actions:
			bookKeeper.nodes_expanded = bookKeeper.nodes_expanded + 1
			node       = Node(startNode)
			returnNode = node.childNode(node.parentState,action)
			print("-----------------------------------------------")
			print("node.state" + str(returnNode.state))
			print("node.action" + str(returnNode.action))
			print("node.count" + str(frontier.numberOfNodes))			
			if not(frontier.found(returnNode) and explored.found(returnNode)):

				frontier.push(returnNode)
	        
		



	
dfs2()
		
#dfs() - does not return enough records

#bfs() - functional already just need to add the file write outs

#startNodeTwo = InitialNode()
#nodetwo = Node(startNodeTwo)
#returnNodeTwo = nodetwo.childNode(nodetwo.parentState,"Down")
#startNodeThree = InitialNode()
#nodethree = Node(startNodeThree)
#returnNodeThree = nodethree.childNode(nodethree.parentState,"Left")








