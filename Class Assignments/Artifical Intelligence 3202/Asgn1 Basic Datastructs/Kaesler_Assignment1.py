import Queue

#implementing queue using python queue module 

queue = Queue.Queue()

#implementing stack

class Stack(object):
	
	def __init__(self):
		self.holder = []  #initializing stack
	
	def push(self, item):
		self.holder.append(item)  #pushing to the stack
	
	def pop(self):
		return self.holder.pop() #popping from stack
	
	def checkSize(self):
		return len(self.holder)
	
	def isEmpty(self):
		if self.holder == []:
			return True

# implementing Binary Tree
class Node(object):
	def __init__(self, key):
		self.left = None
		self.right = None
		self.parent = None
		self.data = key
		
	def getValue(self):
		return self.data	
	def getBothChild(self):
		return [self.left, self.right]		
		
class binaryTree(object):
	def __init__(self):
		self.root = None
		
	def add(self, val, parentValue):
		if self.root == None:
			self.root = Node(val)
		else:
			self.add1(val, parentValue)
			
	def add1(self, val, parentValue):
		if self.find(self.root, parentValue) == None:
			print "Parent value not found"
			return None
		else:
			parent = self.find(self.root, parentValue) ##assuming self.find returns correct node and makes 'parent' that node
			if parent.left == None:
				parent.left = Node(val)
			elif parent.left != None and parent.right == None:
				parent.right = Node(val)
			else:
				print "Parent has two children, node not added"
				
	def preorder_print(self):
		if self.root== None:
			return
		print self.root.getValue()
		for child in self.root.getBothChild():
			self.printHelper(child)
			
	def printHelper(self, root=None):
		if root == None:
			return
		print root.getValue()
		for child in root.getBothChild():
			self.printHelper(child)			
			
	def find(self, node, key):
		if node != None and node.data != key:
			self.find(node.left, key)
			self.find(node.right, key)
		elif node != None and node.data == key:
			return node
		else:
			return None	
	 

## implementing graph
class graph(object):
	def __init__(self, graphDict = {}):
		self.graph_dict = graphDict
		
	def addVertex(self, value):
		if value not in self.graph_dict:
			self.graph_dict[value] = []
		else:
			print "Vertex already exists"
	
	def addEdge(self, value1, value2):
		if value1 not in self.graph_dict or value2 not in self.graph_dict:
			print "One or more vertices not found"
		else:
			if value1 in self.graph_dict:
				self.graph_dict[value1].append(value2)
				self.graph_dict[value2].append(value1)
			
				
	def findVertex(self, value):
		if value in self.graph_dict:
			print value, "has", self.graph_dict[value], "as adjacent vertices"




#TEST FUNCTIONS

#Queue test
print "Testing queue now. Adding values 0-9, dequeuing FIFO and printing"

for i in range(10):
	queue.put(i)
while not queue.empty():
	print queue.get()
	
print "\n"
#Stack Test
print "Testing Stack now. Initializing stack 's'"
s = Stack() #initializing an instance of stack

print "pushing numbers 0-9 to the stack in that respective order, 0 first"
for i in range(10):
	s.push(i)
print s.holder
print "now popping from the stack"  #NOTE STILL HAS PROBLEM WITH GOING PAST


print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
	

'''while not s.isEmpty == True:		# THE END OF THE STACK
	num = s.pop()
	print num'''
	
	
print "\n"
#Binary Tree Test
print "now testing Binary tree"
print "NOTE: MY BINARY TREE CLASS IS SLIGHTLY BUGGY AND DOES NOT WORK COMPLETELY"
print "but it is pretty close"

tree = binaryTree()

tree.add(1,2)  


tree.add(3,1)
tree.add(6,3)
tree.add(4,6)
tree.add(5,4)
tree.preorder_print()

print "\n"
### Graph Test 
print "now testing the graph"
print "adding vertices from 1 to 10"
g = graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)

print "Creating many edges between these vertices"
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,7)
g.addEdge(2,8)
g.addEdge(2,9)
g.addEdge(5,9)
g.addEdge(5,8)
g.addEdge(9,10)
g.addEdge(7,4)
g.addEdge(9,3)
g.addEdge(8,1)
g.addEdge(5,9)
g.addEdge(9,3)
g.addEdge(5,1)
g.addEdge(6,8)
g.addEdge(6,9)
g.addEdge(6,4)
g.addEdge(10,3)
g.addEdge(10,5)
g.addEdge(3,8)
print "showing neighbors of vertices 1, 3, 2, 6, 9"
g.findVertex(1)
g.findVertex(3)
g.findVertex(2)
g.findVertex(6)
g.findVertex(9)
