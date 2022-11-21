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
	def	setSuccessor(self, newSuccessor):
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
	def	setPredecessor(self, newPredecessor):
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
		self._size = 0
		self._trigger = None




#	========================================
#	magic methods for implementing iteration
#	========================================
	def	__iter__(self):
		"""
		provides a means of iterating through the deque from the top down
		"""
		currentFrame = self._listFront

		while not currentFrame.isInactive():
			yield currentFrame.getPayload()

			if	currentFrame == self._listBack:
				break

			currentFrame = currentFrame.getSuccessor()






	def	__len__(self):
		"""
		returns the current size of the deque
		"""
		return	self._size




#	==============================
#	used to pretty-print the stack
#	==============================
	def	__repr__(self):
		"""
		prints the deque in a meaningful manner with "oldest" to the left, going "newer" to the right
		"""
		sep = ""
		rep = "["
		for v in self:
			rep = rep.rstrip() + sep + f'{v}'
			sep = "/"

		return	rep.rstrip()+"]"





#	=====================================
#	methods used to add/remove from Deque
#	=====================================
	def	append(self, newValue):
		"""
		pushs a new value on to the back of the deque
		"""
		if	not self._listBack.getSuccessor().isInactive():
			newFrame = DequeFrame()
			oldSuccessor = self._listBack.getSuccessor()

			self._listBack.setSuccessor(newFrame.setSuccessor(oldSuccessor))
			newFrame.setPredecessor(oldSuccessor.setPredecessor(newFrame))

		self._listBack.getSuccessor().setPayload(newValue)

		self._listBack = self._listBack.getSuccessor()

		self._size += 1

#	finally, fire the trigger id needed
		if	self._trigger != None:
			self._trigger(self)

		return	self





	def	prepend(self, newValue):
		"""
		pushs a new value on to the front of the deque
		"""
		if	not self._listFront.getPredecessor().isInactive():
			newFrame = DequeFrame()
			oldPredecessor = self._listFront.getPredecessor()

			self._listFront.setPredecessor(newFrame.setPredecessor(oldPredecessor))
			newFrame.setSuccessor(oldPredecessor.setSuccessor(newFrame))

		self._listFront.getPredecessor().setPayload(newValue)

		self._listFront = self._listFront.getPredecessor()

		self._size += 1

#	finally, fire the trigger id needed
		if	self._trigger != None:
			self._trigger(self)

		return	self





	def	popOldest(self):
		"""
		removes the oldest value from the deque and return it
		"""

		payload = self._listFront.getPayload()

		if	not self._listFront.isInactive():
			self._listFront.makeInactive()
			self._listFront = self._listFront.getSuccessor()

		self._size = max(self._size -1, 0)

		return	payload





	def	popNewest(self):
		"""
		removes the newest value from the deque and return it
		"""

		payload = self._listBack.getPayload()

		if	not self._listBack.isInactive():
			self._listBack.makeInactive()
			self._listBack = self._listBack.getPredecessor()

		self._size = max(self._size -1, 0)

		return	payload





#	============================================
#	accessor functions to allow frame peek/pokes
#	============================================
	def	peek(self, offset, default=None):
		"""
		allows access into the entries on the deque; negative numbers start at the back of the deque (newest);
		otherwise access is to next available entry
		"""
		if	offset < 0:
			reverse = True
			current = self._listBack
			endpoint = self._listFront
			offset = abs(offset)-1
		else:
			reverse = False
			current = self._listFront
			endpoint = self._listBack

		while (current != endpoint and not current.isInactive() and offset > 0):
			offset -= 1
			current = current.getPredecessor() if reverse else current.getSuccessor()

		if	current.isInactive() or offset > 0:
			return	default

		return	current.getPayload()




	def	poke(self, offset, newPayload):
		"""
		allows update on the entries on the deque; negative numbers start at the back of the deque (newest);
		otherwise access is to next available entry
		returns	True if the assignment fails, or False otherwise
		"""
		if	offset < 0:
			reverse = True
			current = self._listBack
			endpoint = self._listFront
			offset = abs(offset)-1
		else:
			reverse = False
			current = self._listFront
			endpoint = self._listBack

		while (current != endpoint and not current.isInactive() and offset > 0):
			offset -= 1
			current = current.getPredecessor() if reverse else current.getSuccessor()

		if	current.isInactive() or offset > 0:
			return	True

		current.setPayload(newPayload)
		return	False






#	====================
#	misc support methods
#	====================
	def	isEmpty(self):
		"""
		returns True if the deque is empty, or False otherwise
		"""
		return	self._size == 0



	def	clear(self):
		"""
		clears the deque of all values
		"""
		while not self.isEmpty():
			self.popOldest()

		return	self




	def	addTrigger(self, trigger):
		"""
		adds a funtion (or a bound method) to be called when an entry is added to the deque
		"""
		self._trigger = trigger



	def	removeTrigger(self):
		"""
		clear any trigger that might be set
		"""
		self._trigger = None