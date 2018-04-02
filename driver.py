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

		print('input_board ' + str(input_board))
		
		self.maxdoor  = len(input_board[0]) -1 
		self.maxfloor = len(input_board) - 1

		print('maxdoor'  + str(self.maxdoor))
		print('maxfloor' + str(self.maxfloor))
		
		self.state = list(input_board)

		for row in input_board:
			
			for columnvalue in row:	
			
				if(columnvalue=='0'):

					self.door  = int(str(row.index(columnvalue)))
			 		self.floor = int(str(input_board.index(row)))

           				print('self.door' + str(self.door))
					print('self.floor'+ str(self.floor))
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

						self.canMoveUp   = True
						self.canMoveDown  = False


					if(self.floor < self.maxfloor  and self.floor > 0):

						self.canMoveUp = True
						self.canMoveDown = True
					
		print('start > '      + str(self.state))	
		print('move left > '  + str(self.canMoveLeft))
		print('move right > ' + str(self.canMoveRight))
		print(' move up > '   + str(self.canMoveUp))
		print(' move down > ' + str(self.canMoveDown))
					
	def childNodes(self,nextNodestate):
		
		currentNode =  copy.deepcopy(nextNodestate)
	
		print('nextNode > ' + str(nextNodestate))
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

			print(str('simpleNode.action'))

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



		print('total size of returnNodeList ' + str(len(returnNodeList)))
		for i in returnNodeList:


			print('returning' + str(i.currentNodeState))

		return returnNodeList
        
	


class Frontier:
	
	items = list()
	
	def add(self,input_list):
		
		self.items.append(input_list)

	def pop(self):

	    return self.items.pop(0)

	def found(self,input_list):
	
		if(self.items.count(input_list) > 0):
			
			return True
		else:
			return False	
	def empty(self):
		
		if( len(self.items) > 0):
			
			return False
		else:
			return True

class Explored :
	
	items = list()
	
	def add(self,input_list):

		self.item.append(input_list)


		
	def found(self,input_list):
	
		if(self.items.count(input_list) > 0):
			
			return True
		else:
			return False	
 
		
		

		






class Problem:

	frontier    = None
	explored    = None
	node        = None
	pathCost    =  0
	goalState   = list() 
	initialState = list()
	

	def __init__(self,board):


                goalboard    = board.split(',')
		goalboard.sort()

		print('the goal is ' + str(goalboard))
		
		self.goalState.append(goalboard[0:3])
		self.goalState.append(goalboard[3:6])
	        self.goalState.append(goalboard[6:9])


		print(str(self.goalState[0])) 
		print(str(self.goalState[1]))
		print(str(self.goalState[2]))


	
             	self.initialState.append(board.split(',')[0:3])
		self.initialState.append(board.split(',')[3:6])
	        self.initialState.append(board.split(',')[6:9])

		self.frontier 		= Frontier()
		self.explored 		= Explored()
		self.problemNode 	= Node(self.initialState)
		self.frontier.add(self.initialState)

	def bfs(self):
	
		if(self.problemNode.state == self.goalState):
		
			return 'Solution'
			
		self.frontier.add(self.initialState)
		
		while True:

			if(self.frontier.empty() == True):
				
				return 'Failure'

		
			input_node  = self.frontier.pop()

			print('input node ' + str(input_node))			

			newNode = Node(input_node)

			for child in newNode.childNodes(newNode.state):
				
				if( not(self.explored.found(child.currentNodeState)) and not (self.frontier.found(child.currentNodeState))):
						
					if(child.currentNodeState==self.goalState):
						
						return 'Solution'
					else:


						print('--------------------------------------------------')
						print('parentNodeState > ' +  str(child.parentNodeState))
						print(' childNodeState > ' + str(child.currentNodeState))
						print(' action that got me here >' + str(child.action))

					
					

	

	
#board  = [ [1,2,5], [3,4,0], [6,7,8] ]
#goal = [ [0,1,2], [3,4,5], [6,7,8] ]

if(sys.argv[1]=="bfs"):
	
	problem = Problem(sys.argv[2])
        problem.bfs()
 
