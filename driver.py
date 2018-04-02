import sys, copy

class SimpleNode:

	action           = list()
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

			returnNodeList.append(u_childNode)
           


		if(self.canMoveDown == True):

			d_childNode = copy.deepcopy(currentNode)

			temp = d_childNode[(self.floor+1)][self.door]

			d_childNode[(self.floor+1)][self.door] = 0

			d_childNode[(self.floor)][self.door] = temp
			
			returnNodeList.append(d_childNode)


		if(self.canMoveRight == True):
			
                    
			r_childNode = copy.deepcopy(currentNode)
			
			temp =  r_childNode[(self.floor)][self.door+1]

			r_childNode[(self.floor)][self.door+1] = 0

			r_childNode[(self.floor)][self.door] = temp
                       
			returnNodeList.append(r_childNode)
	
						
		if(self.canMoveLeft == True):
			
			l_childNode = copy.deepcopy(currentNode)
			
			temp = l_childNode[(self.floor)][self.door-1]

			l_childNode[(self.floor)][self.door-1] = 0

			l_childNode[(self.floor)][self.door] = temp

			returnNodeList.append(l_childNode)



		
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
			


class Explored :
	
	items = list()
	
	def add(self,input_list):

		self.item.append(input_list)


		
	def found(self,input_list):
	
		if(items.count(input_list) > 0):
			
			return True
		else:
			return False	
		
		

def bfs:
		
	board  = [ [1,2,5], [3,4,0], [6,7,8] ]
	goal   = [ [0,1,2], [3,4,5], [6,7,8] ]


	frontier = Frontier()
	explored = Explored()
        s = Node(board)
	
	while True:

		for i in s.childNodes(s.state):
	
			frontier.add(i)


		toTest = frontier.pop()

		explored.add(toTest)


		if not(toTest == goal):

			print('no match')

			return toTest

		 s = Node(toTest)
	
	
	
	
	


