"""
a version of a list used for memory access by the TLCvm
"""



#	==============
#	imports needed
#	==============
from .tlc_pointers import *
from .nodes import *





#	-----------
#	export list
#	-----------
__all__ = ['ObjectMemory',]




#	=================================================================
#	a version of list used for memory storage and access in the TLCvm
#	=================================================================
class ObjectMemory:
	"""
	implements memory for the TLCvm
	"""



#	-----------
#	constructor
#	-----------
	def __init__(self, default=None):
		"""
		Constructor - builds the empty object memory
		"""
		self._memory = list()
		self._defaultValue = default





#	=================================================================
#	magic methods used to provide "clean" access to the object memory
#	=================================================================
	def	__getitem__(self,  key):
		"""
		allows indexed access to the dictionary
		"""
		return	self.getEntry(key)



	def	__add__(self, value):
		"""
		handles addition as an append; result returned is index assigned
		"""
		return	self.addEntry(value)





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
			buf += "{0:}{1:04d} {2:}".format(sep, i, self[i])
			i += 1
			sep = "\n"

		return	buf




#	===========================
#	memory entry/update methods
#	===========================
	def	addEntry(self, value):
		"""
		adds an entry to object memory and returns the associated index
		"""
		index = len(self._memory)
		self._memory.append(value)

		return	index





	def	getEntry(self, key):
		"""
		retrieves a value from object memory, or returns the default value if none is found
		"""

#	we can accept integers, tuples, or pointers; anything else makes us unhappy
		if	type(key) is int:
			key = TLCPointer(key)
		elif type(key) is tuple:
			key = TLCPointer(key)
		elif type(key) is not TLCPointer:
			return self.defaultNode

		if	key.objectID >= len(self._memory) or key.objectID < 0:
			return	self.defaultNode

		return	self._memory[key.objectID].get(key.offset)




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






