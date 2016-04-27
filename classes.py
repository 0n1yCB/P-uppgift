import random

class time():
	def __init__(self):
		self.current = 540

	def get(self):
		hour = str(self.current//60)
		minute = str(self.current%60)
		if len(minute) is 1:
			minute = "0" + minute

		return str("Kl. " + str(hour) + ":" + minute)

	def __str__(self):
		hour = str(self.current//60)
		minute = str(self.current%60)
		if len(hour) is 1:
			hour = "0" + hour
		if len(minute) is 1:
			minute = "0" + minute

		return str("Kl. " + str(hour) + ":" + minute)

class person():
	def __init__(self, custNo = 0, enterQueue = 0):
		def noErrands():
			errands = 1
			while random.randrange(0,2) == 1:
				errands += 1
			return errands
			
		def isRobber():
			return random.randrange(0,1000) == 0

		self.errands = noErrands()
		self.kundnr = custNo
		self.consumedTime = 0
		self.isRobber = isRobber()
		self.enterQueue = enterQueue

	def canLeave(self):
		return self.consumedTime >= 2*self.errands

class Node():
	def __init__(self, item, nextitem = None):
		self.item = item
		self.next = nextitem

class queue():
	def __init__(self):
		self.top = None
		self.last = None
		self.length = 0
		self.queueTime = 0

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

	def empty(self):
		self.top = None
		self.last = None
		self.length = 0
