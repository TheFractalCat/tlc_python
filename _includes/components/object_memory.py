"""
a version of a list used for memory access by the TLCvm
"""




#	==============
#	imports needed
#	==============
# from .tlc_pointers import *
# from .nodes import *





#	-----------
#	export list
#	-----------
__all__ = ['MemorySegment',
		   'ObjectMemory',
			]




#	=================================================================
#	a version of list used for memory storage and access by ObjectMemory
#	=================================================================
class MemorySegment:
	"""
	a memory subsection used by Object Memory
	"""



#	-----------
#	constructor
#	-----------
	def __init__(self, baseAddress, default=None):
		"""
		Constructor - builds the empty memory segment
		"""
		self._memory = list()
		self._baseAddress = baseAddress
		self._defaultValue = default





#	========================================
#	check an address to see if it's in range
#	========================================
	def	inRange(self, targetAddress):
		"""
		checks the target address to see if it's in range for this segment
		"""
		if	targetAddress >= self.baseAddress:
			return	True

		return	False





#	==================================================================
#	magic methods used to provide "clean" access to the memory segment
#	==================================================================
	def	__getitem__(self,  address):
		"""
		allows indexed access to the dictionary
		"""
		return	self.peek(address)



	def	__setitem__(self,  address, newValue):
		"""
		allows indexed access to the dictionary
		"""
		return	self.poke(address, newValue)



	def	__add__(self, value):
		"""
		handles addition as an append; result returned is index assigned
		"""
		return	self.append(value)





#	=======================================
#	magic methods for iteration over memory
#	=======================================
	def	__iter__(self):
		"""
		provides a means of iterating through the dictionary
		"""
		i = 0

		while i < len(self._memory):
			v = self[i]
			i += 1
			yield v





	def	__len__(self):
		"""
		returns the current size of object memory
		"""
		return	len(self._memory)




#	======================================
#	method used for pretty-printing memory
#	======================================
	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		i = 0
		buf = ""
		sep = ""

		while(i < len(self)):
			buf += "{0:}{1:011_d} {2:}".format(sep, i+self.baseAddress, self[i+self.baseAddress])
			i += 1
			sep = "\n"

		return	buf




#	===========================
#	memory entry/update methods
#	===========================
	def	append(self, value):
		"""
		adds an entry to object memory and returns the associated index
		"""
		index = len(self)
		self._memory.append(value)

		return	index + self.baseAddress





	def	peek(self, address):
		"""
		retrieves a value from object memory, or returns the default value if none is found
		"""

		address -= self.baseAddress

		if	address >= len(self) or address < 0:
			return	self.defaultNode

		return	self._memory[address]





	def	poke(self, address, newValue):
		"""
		assigns a new value to object memory, or returns the default value if out of range
		"""

		address -= self.baseAddress

		if	address >= len(self) or address < 0:
			return	self.defaultNode

		self._memory[address] = newValue

		return	newValue





	@property
	def	baseAddress(self):
		"""
		Returns the base address for the memory segment (read-only)
		"""
		return self._baseAddress





	@property
	def	defaultNode(self):
		"""
		Returns the default value returned when an invalid object ID is supplied
		"""
		return self._defaultValue




	@defaultNode.setter
	def	defaultNode(self, default):
		"""
		set the default value returned when an invalid object ID is supplied
		"""
		self._defaultValue = default





#	============================================
#	the organizing structure for memory segments
#	============================================
class ObjectMemory:
	"""
	The organizing class for memory segments
	"""



#	-----------
#	constructor
#	-----------
	def __init__(self, default=None):
		"""
		Constructor - builds the empty object memory
		"""
		self._segments = list()
		self._defaultValue = default

#	build the segments needed
		self._segments.append(MemorySegment(1_000_000))
		self._segments.append(MemorySegment(0_000_000))




#	======================================
#	method used for pretty-printing memory
#	======================================
	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		i = len(self._segments)-1
		buf = ""
		sep = ""

		while(i >= 0):
			buf += "{:}{:}".format(sep, self._segments[i])
			i -= 1
			sep = "\n"


		return	buf



	@property
	def SystemSpace(self):
		"""
		reference to the system segment
		"""
		return	self._segments[0]



	@property
	def UserSpace(self):
		"""
		reference to the user segment
		"""
		return	self._segments[1]





#	============================
#	content management Functions
#	============================
	def	peek(self, address):
		"""
		retrieves a value from the appropriate memory segment, or returns the default value if none is found
		"""
		for ms in self._segments:
			if	ms.inRange(address):
				return	ms.peek(address)

		return	self.defaultNode





	def	poke(self, address, newValue):
		"""
		assigns a new value to the appropriate memory segment, or returns the default value if out of range
		"""

		for ms in self._segments:
			if	ms.inRange(address):
				return	ms.poke(address, newValue)

		return	self.defaultNode





#	==================================================================
#	magic methods used to provide "clean" access to the memory segment
#	==================================================================
	def	__getitem__(self,  address):
		"""
		allows indexed access to the dictionary
		"""
		return	self.peek(address)



	def	__setitem__(self,  address, newValue):
		"""
		allows indexed access to the dictionary
		"""
		return	self.poke(address, newValue)


