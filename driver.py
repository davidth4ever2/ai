import sys, copy

class SimpleNode:

	action           = None
	direction 	 = None
	parentNodeState  = None
	currentNodeState = None


class Node:

	floor  = None
	door   = None
	state  = None
	parent = None
        isLeaf = False

	maxdoor  = None 
	maxfloor = None 

	canMoveUp    = False
	canMoveDown  = False
	canMoveLeft  = False
	canMoveRight = False
	pathCost     = 0
	pathToGoal   = list()

        
	currentLocation = list()

	def __init__(self,input_board):

		
		self.maxdoor  = len(board[0]) -1 
		self.maxfloor = len(board) - 1
		
		self.state = list(input_board)

		for row in input_board:
			
			for columnvalue in row:	
			
				if(columnvalue==0):

					self.door  = int(str(row.index(columnvalue)))
			 		self.floor = int(str(input_board.index(row)))

           				if(self.door==0):
						
						self.canMoveLeft  = False
						self.canMoveRight = True

					if(self.door==self.maxdoor):

						self.canMoveLeft   = True
						self.canMoveRight  = False

					if(self.door < self.maxdoor  and self.door > 0):
 
						self.canMoveLeft  = True
						self.canMoveRight = True

		
					if(self.floor==0): # this means we are on the top floor which is counter intuitive but what ever

						self.canMoveUp  = False
						self.canMoveDown = True

					if(self.floor==self.maxfloor):

						self.canMovUp   = True
						self.canMoveLeft  = False
						self.canMoveDown  = False

					if(self.floor < self.maxfloor  and self.door > 0):


						self.canMoveUp = True
						self.canMoveDown = True
					
		print(str(self.state))	
		print(str(self.canMoveLeft))
		print(str(self.canMoveRight))
		print(str(self.canMoveUp))
		print(str(self.canMoveDown))
					
	def childNodes(self,nextNode):
		
		currentNode =  copy.deepcopy(nextNode)
	
		print('nextNode > ' + str(nextNode))
                returnNodeList = list()
			
		if(self.canMoveUp == True):

		        u_childNode = copy.deepcopy(currentNode)

			temp =  u_childNode[(self.floor-1)][self.door]

			u_childNode[(self.floor-1)][self.door] = 0

			u_childNode[(self.floor)][self.door] = temp

			simpleNode 		       	 = SimpleNode()
			simpleNode.parentNodeState       = currentNode
			simpleNode.currentNodeState      = u_childNode
			simpleNode.action 	         = 'Up'

			returnNodeList.append(simpleNode)
           


		if(self.canMoveDown == True):

			d_childNode = copy.deepcopy(currentNode)

			temp = d_childNode[(self.floor+1)][self.door]

			d_childNode[(self.floor+1)][self.door] = 0

			d_childNode[(self.floor)][self.door] = temp
			
			simpleNode 		     = SimpleNode()
			simpleNode.parentNodeState   = currentNode
			simpleNode.currentNodeState  = d_childNode
			simpleNode.action 	     = 'Down'

			returnNodeList.append(simpleNode)

			
           

		if(self.canMoveRight == True):
			
                    
			r_childNode = copy.deepcopy(currentNode)
			
			temp =  r_childNode[(self.floor)][self.door+1]

			r_childNode[(self.floor)][self.door+1] = 0

			r_childNode[(self.floor)][self.door] = temp
                       
			simpleNode 			= SimpleNode()
			simpleNode.parentNodeState  	= currentNode
			simpleNode.currentNodeState 	= r_childNode
			simpleNode.action 		= 'Right'

			returnNodeList.append(simpleNode)
	
						
		if(self.canMoveLeft == True):
			
			l_childNode = copy.deepcopy(currentNode)
			
			temp = l_childNode[(self.floor)][self.door-1]

			l_childNode[(self.floor)][self.door-1] = 0

			l_childNode[(self.floor)][self.door] = temp
			

			simpleNode 			= SimpleNode()
			simpleNode.parentNodeState 	= currentNode
			simpleNode.currentNodeState 	= l_childNode
			simpleNode.action       	= 'Left'

			returnNodeList.append(simpleNode)



		
		for i in returnNodeList:

			print(str(i))

		return returnNodeList
        
	


class Frontier:
	
	items = list()
	
	def add(self,input_list):
		
		self.items.append(input_list)

	def pop(self):

	    return self.items.pop(0)

	def found(self,input_list):
	
		if(items.count(input_list) > 0):
			
			return True
		else:
			return False	
	def empty(self):
		
		if( len(items) > 0):
			
			return False
		else:
			return True

class Explored :
	
	items = list()
	
	def add(self,input_list):

		self.item.append(input_list)


		
	def found(self,input_list):
	
		if(items.count(input_list) > 0):
			
			return True
		else:
			return False	
 
		
		

		


board  = [ [1,2,5], [3,4,0], [6,7,8] ]
goal   = [ [0,1,2], [3,4,5], [6,7,8] ]


class Problem:

	frontier = None
	explored = None
	node     = None
	pathCost = 0

	def __init__(self,board):

		self.frontier 		= Frontier()
		self.explored 		= Explored()
		self.problemNode 	= Node(board)
		self.frontier.add(board)

	def bfs(self):
	
		if(self.problemNode.state = goalState):
		
			return 'Solution'
			
		frontier.add(node.state)
		
		while True:

				
			
			if(frontier.empty() == True):
				
				return 'Failure'

		
			input_node  = frontier.pop()

			for child in input_node.childNodes(input_node.state):
				
				if( not(explored.found(child.state)) and not (frontier.found(child.state))):
						
					if(child.state==goalState):
						
						return 'Solution'
					else:
						frontier.add(child.state)
					
					

	

	



