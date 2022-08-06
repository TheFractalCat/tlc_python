"""
This module defines the basic structure and function of a TLC Node - the basic form of storage used by the TLCVM
"""



#	-----------
#	export list
#	-----------
__all__ = ['TLCNode', 'TLCNilNode']



class	TLCNode:
	"""
	the basic node used as a parent for all other Node types. it provides default behavior used by other types
	"""

	def	__init__(self):
		"""
		constructor for the class - currently it does nothing
		"""
		pass





	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	f'<TLCNode at {hex(id(self))}>'





	def	isInvalid(self):
		"""
		True if this is not a valid TLCNode, or False otherwise
		default is False
		"""
		return	False





	def	isError(self):
		"""
		True is this is an ErrorNode of some kind, or False otherwise
		default is False
		"""
		return	False




	def	isNil(self):
		"""
		True if this node represents a Nil Pointer, or False otherwise
		default is False
		"""
		return	False





	def	isPointer(self):
		"""
		True if this node represents a pointer, or False otherwise
		default is False
		"""
		return False





	def	isInstruction(self):
		"""
		True if this node is a TLC Opcode, or False otherwise
		default is False
		"""
		return	False





	def	isData(self):
		"""
		True if this node contains data of any kind, or False otherwise
		default is False
		"""
		return False





	def	isDict(self):
		"""
		True if this node is a TLC Dictionary, or False otherwise
		default is False
		"""
		return False





class	TLCNilNode(TLCNode):
	"""
	a Nil node is used to represent null pointers inside the TLCVM
	"""

	def	__init__(self):
		"""
		constructor for the class - currently it does nothing
		"""
		pass





	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	f'<Nil Node>'





	def	isNil(self):
		"""
		True if this node represents a Nil Pointer, or False otherwise
		we return True
		"""
		return	True





	def	isPointer(self):
		"""
		True if this node represents a pointer, or False otherwise
		we return True
		"""
		return True
