"""
This module defines the basic structure and function of a TLC Node - the basic form of storage used by the TLCVM
"""



#	-----------
#	export list
#	-----------
__all__ = ['TLCNode', 'TLCNilNode']




#	=======================================================================
#	the base class used to define all methods offered, and default behavior
#	=======================================================================
class	TLCNode:
	"""
	the basic node used as a parent for all other Node types. it provides default behavior used by other types
	"""



#	======================================
#	class variables, constants and methods
#	======================================
	_DEFAULT_INVALID_OBJECT = None



#	---------------------------------------------------
#	class method used to set the default invalid object
#	---------------------------------------------------
	@classmethod
	def	setDefaultObject(cls, node):
		"""
		set the class variable used to hold the default invalid object
		"""
		TLCNode._DEFAULT_INVALID_OBJECT = node




#	------------------------
#	default base constructor
#	------------------------
	def	__init__(self):
		"""
		constructor for the class - currently it does nothing
		"""
		pass




#	--------------------------------
#	default representation of a node
#	--------------------------------
	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	f'<{self.__class__.__name__} at {hex(id(self))}>'




#	---------------------------------------------------------------------------------------------
#	returns True if this is an invalid object, like TLCInvalidNode; generally used as a singleton
#	---------------------------------------------------------------------------------------------
	def	isInvalid(self):
		"""
		True if this is not a valid TLCNode, or False otherwise
		default is False
		"""
		return	False




#	-----------------------------------------------------------------------------------------
#	returns True if this is an error object, like TLCErrorNode; generally used as a singleton
#	-----------------------------------------------------------------------------------------
	def	isError(self):
		"""
		True is this is an ErrorNode of some kind, or False otherwise
		default is False
		"""
		return	False




#	----------------------------------------------------------------------------------------------------------------------------------------
#	returns true if this is a Nil pointer, like TLCNilPointer; generally used as a singleton, and normally returns True to isPointer as well
#	----------------------------------------------------------------------------------------------------------------------------------------
	def	isNil(self):
		"""
		True if this node represents a Nil Pointer, or False otherwise
		default is False
		"""
		return	False





#	---------------------------------------------------------------------------------
#	returns true if this is some form of a pointer, like TLCNilNode or TLCPointerNode
#	---------------------------------------------------------------------------------
	def	isPointer(self):
		"""
		True if this node represents a pointer, or False otherwise
		default is False
		"""
		return False




#	----------------------------------------------------------------------------------
#	True if this node contains an executable stream of opcodes, like TLCExecutableNode
#	----------------------------------------------------------------------------------
	def	isExecutable(self):
		"""
		True if this node contains an executable stream of opcodes, like TLCExecutableNode
		default is False
		"""
		return	False




#	-------------------------------------------
#	True if this node contains data of any kind
#	-------------------------------------------
	def	isData(self):
		"""
		True if this node contains data of any kind, or False otherwise
		default is False
		"""
		return False




#	----------------------------------------------------------
#	returns True if this node is a TLC Vocabulary of some kind
#	----------------------------------------------------------
	def	isVocabulary(self):
		"""
		True if this node is a TLC Vocabulary, or False otherwise
		default is False
		"""
		return False




#	---------------------------------------------------------------------
#	processes a pointer offset (if needed) and returns the related object
#	---------------------------------------------------------------------
	def	get(self, offset):
		"""
		processes a pointer offset (if needed) and returns the related object
		"""
#	default processing to to just return ourself
		return	self




#	---------------------------------------------------------------------
#	processes an update request based upon a pointer offset (if needed) and returns the related object (or an Invalid node if the update fails)
#	---------------------------------------------------------------------
	def	set(self, value, offset):
		"""
		processes an update request based upon a pointer offset (if needed) and returns the related object (or an Invalid node if the update fails)
		"""
#	default processing to to just return an invalid object
		return	self.DEFAULT_INVALID_OBJECT




#	--------------------------------------------------
#	property used to access the default invalid object
#	--------------------------------------------------
	@property
	def DEFAULT_INVALID_OBJECT(self):
		"""
		returns the class-level default invalid object, used for returning errors
		"""
		return	TLCNode._DEFAULT_INVALID_OBJECT





#	==========================================================================================================
#	this class defines nil nodes, used to represent an empty space. it can be used as either data or a pointer
#	==========================================================================================================
__all__.append('TLCNilNode')

class	TLCNilNode(TLCNode):
	"""
	a Nil node is used to represent an empty space. it can be used as either data or a pointer inside the TLCVM
	"""


#	-----------
#	constructor
#	-----------
	def	__init__(self):
		"""
		constructor for the class - currently it does nothing except call its super constructor
		"""
		super().__init__()





#	--------------------------------
#	default representation of a node
#	--------------------------------
	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	'<Nil Node>'





#	------------------------------------------------------------------------------------------------------------------------------------------------
#	returns true if this is a Nil pointer, like TLCNilNode; generally used as a singleton, and normally returns True to isPointer and isData as well
#	------------------------------------------------------------------------------------------------------------------------------------------------
	def	isNil(self):
		"""
		True if this node represents a Nil Pointer, or False otherwise
		default is False
		"""
		return	True





#	---------------------------------------------------------------
#	returns true if this is some form of a pointer, like TLCNilNode
#	---------------------------------------------------------------
	def	isPointer(self):
		"""
		True if this node represents a pointer, or False otherwise
		default is False
		"""
		return True




#	-------------------------------------------
#	True if this node contains data of any kind
#	-------------------------------------------
	def	isData(self):
		"""
		True if this node contains data of any kind, or False otherwise
		default is False
		"""
		return True





#	===========================================================================================================
#	this class defines invalid nodes, used to represent a node returned when the requested operation has failed
#	===========================================================================================================
__all__.append('TLCInvalidNode')

class	TLCInvalidNode(TLCNode):
	"""
	this class defines invalid nodes, used to represent a node returned when the requested operation has failed
	"""


#	-----------
#	constructor
#	-----------
	def	__init__(self):
		"""
		constructor for the class - currently it does nothing except call its super constructor
		"""
		super().__init__()





#	--------------------------------
#	default representation of a node
#	--------------------------------
	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	'<Invalid Node>'





#	---------------------------------------------------------------------------
#	returns true if this is a Nil node, which TLCInvalidNode will pretend to be
#	---------------------------------------------------------------------------
	def	isNil(self):
		"""
		True if this node represents a Nil Pointer, or False otherwise
		default is False
		"""
		return	True




#	---------------------------------------------------------------------------------------------
#	returns True if this is an invalid object, like TLCInvalidNode; generally used as a singleton
#	---------------------------------------------------------------------------------------------
	def	isInvalid(self):
		"""
		True if this is not a valid TLCNode, or False otherwise
		default is False
		"""
		return	True
