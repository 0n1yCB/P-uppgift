class Node():
	def __init__(self, item, nextitem = None):
		self.item = item
		self.next = nextitem

class queue():
	def __init__(self):
		self.top = None
		self.last = None
		self.length = 0

	def put(self, inputdata):
		self.length += 1
		if self.isEmpty():
			self.top = Node(inputdata)
			self.last = self.top
			self.top.next = self.last
		else:
			self.last.next = Node(inputdata)
			self.last = self.last.next

	def get(self):
		if self.isEmpty():
			return None
		else:
			out = self.top.item
			self.length = self.length -1
			if self.top == self.last:
				self.last = None
				return self.top.item

			self.top = self.top.next
			return out
			
	def isEmpty(self):
		if self.last == None:
			return True
		else:
			return False