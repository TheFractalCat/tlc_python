"""
this is the module that defines my basic deque for TLC
"""



#	===========
#	export list
#	===========
__all__ = ['Deque']




#	================================
#	internal class used by the deque
#	================================
class	DequeFrame:
	"""
	internal class used to build the deque
	"""



#	===========
#	constructor
#	===========
	def	__init__(self):
		"""
		constructor; initializes the next deque frame
		"""
		self._payload = None
		self._successor = self
		self._predecessor = self
		self._inactive = True





#	===============================
#	get the current frame successor
#	===============================
	def	getSuccessor(self):
			return	self._successor




#	=================================
#	change the successor on the frame
#	=================================
	def	setSuccessor(self, newSuccessor)
		"""
		assigns a new successor to the frame, and returns the old one
		"""
		oldSuccessor = self.getSuccessor()
		self._successor = newSuccessor

		return	oldSuccessor





#	=================================
#	get the current frame predecessor
#	=================================
	def	getPredecessor(self):
			return	self._predecessor




#	===================================
#	change the predecessor on the frame
#	===================================
	def	setPredecessor(self, newPredecessor)
		"""
		assigns a new predecessor to the frame, and returns the old one
		"""
		oldPredecessor = self.getPredecessor()
		self._predecessor = newPredecessor

		return	oldPredecessor





#	====================================
#	get the current payload of the frame
#	====================================
	def	getPayload(self):
		"""
		get the current payload associated with the frame
		"""
		return	self._payload





#	============================
#	set the payload of the frame
#	============================
	def	setPayload(self, newPayload, inactive=False):
		"""
		assigns a new payload to the frame
		"""
		self._payload = newPayload
		self._inactive = inactive

		return	self





#	=====================================
#	returns True if the frame is inactive
#	=====================================
	def	isInactive(self):
		"""
		returns True if the frame is inactive
		"""
		return	self._inactive




#	=======================
#	make the frame inactive
#	=======================
	def	makeInactive(self):
		"""
		make the frame inactive
		"""
		self.setPayload(None, True)
		return	self





#	==============================
#	used to pretty-print the frame
#	==============================
	def	__repr__(self):
		"""
		prints the frame in a meaningful manner
		"""
		if	self.isInactive():
			return	""

		return	"{:}".format(self.getPayload())





#	==================================
#	the basic deque used by the TLC vm
#	==================================
class	Deque():
	"""
	the actual deque class used by TLC
	"""



#	===========
#	constructor
#	===========
	def	__init__(self):
		"""
		constructor; initializes the list used to store deque values
		"""
		self._listFront = DequeFrame()
		self._listBack = self._listFront





#	=====================================================================
#	magic methods used to make indexing on the stack work the way we want
#	=====================================================================
	def	__getitem__(self,  key):
		"""
		reverses indexing so top of stack is 0
		"""
		return	self._list.__getitem__(-(key+1))





	def	__setitem__(self,  key, newValue):
		"""
		reverses indexed assignment so top of stack is 0
		"""
		return	self._list.__setitem__(-(key+1), newValue)




#	========================================
#	magic methods for implementing iteration
#	========================================
	def	__iter__(self):
		"""
		provides a means of iterating through the stack from the top down
		"""
		i = 0

		while i < len(self._list):
			v = self[i]
			i += 1
			yield v





	def	__len__(self):
		"""
		returns the current size of the stack
		"""
		return	len(self._list)




#	==============================
#	used to pretty-print the stack
#	==============================
	def	__repr__(self):
		"""
		prints the stack in a meaningful manner with "top" to the left, going deeper to the right
		"""
		sep = ""
		rep = "["
		for v in self:
			rep = rep.rstrip() + sep + f'{v}'
			sep = "/"

		return	rep.rstrip()+"]"




#	==========================
#	stack manipulation methods
#	==========================
	def	clear(self):
		"""
		clears the stack of all data and returns a self reference
		"""
		self._list.clear()

		return self





	def	push(self, newValue):
		"""
		pushs a new value on to the stack and returns a self reference
		"""
		self._list.append(newValue)
		return	self





	def	pull(self):
		"""
		removes the top value on the stack and returns it
		"""
		return	self._list.pop()





	def	rotate(self, depth):
		"""
		"rotates" the first depth values on the stack and returns a self reference

		if depth is negative, rotation is to the rear (deeper into the stack)
		otherwise, rotation is to the front (towards the "top" of the stack)
		"""
		if	depth < 0:
			depth = -depth
			first = depth - 1
			last = 0
			direction = -1
		else:
			first = 0
			last = depth - 1
			direction = 1

		temp = self[first]
		first = first + direction

		while((depth := depth - 1) > 0):
			self[first-direction] = self[first]
			first += direction


		self[last] = temp

		return	self





	def	duplicate(self,offset=0):
		"""
		duplicates a value on the stack and returns a self reference
		offset can be supplied if value to be duplicated is not the TopOfStack
		"""
		self.push(self[offset])

		return	self