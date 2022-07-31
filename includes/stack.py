"""
this is the module that defines my basic stack for TLC
"""


class	myStack():
	"""
	the actual stack class used by TLC
	"""


	def	__init__(self):
		"""
		constructor; initializes the list used to store stack values
		"""
		self._list = list()






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





	def	__iter__(self):
		"""
		provides a means of iterating through the stack from the top down
		"""
		i = 0

		while i < len(self._list):
			v = self[i]
			i += 1
			yield v





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