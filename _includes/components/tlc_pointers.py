"""
this module defines the behavior of the pointers used by the TLCvm
"""



#	==============
#	imports needed
#	==============





#	===========
#	export list
#	===========
__all__ = [
			'TLCPointer',
		]





class TLCPointer:
	"""
	the basic object ID/offset used throughout the TLCvm
	"""

#	=====================================
#	class variables and constants, if any
#	=====================================




#	-----------
#	constructor
#	-----------
	def	__init__(self, pointerValue=None):
		"""
		constructor for building a pointer
		"""
#	first initialize instance variables ...
		self._nullState = True
		self._invalidState = False
		self._objectID = None
		self._offset = None

#	... then assign the value passed it
		self.set(pointerValue)




#	------------------------------
#	method used for representation
#	------------------------------
	def	__repr__(self):
		"""
		provides a string version of the pointer
		"""
		if	self.isInvalid():
			return "Invalid Pointer"

		if	self.isNull():
			return "NULL"

		return	"{0:_d}|{1:d}".format(self.objectID, self.offset)





#	---------------------------------------------
#	property mappings from variable list to names
#	---------------------------------------------





#	----------------------------------------------
#	externally visible properties and state checks
#	----------------------------------------------
	@property
	def objectID(self):
		"""
		the object ID part of the pointer
		"""
		return	self._objectID



	@property
	def offset(self):
		"""
		the offset portion of the pointer
		"""
		return	self._offset





#	------------------
#	state methods used
#	------------------
	def	isNull(self):
		"""
		returns true if the pointer is null or invalid
		"""
		return	(self._nullState or self._invalidState)



	def	isInvalid(self):
		"""
		returns true if the pointer is invalid
		"""
		return	(self._invalidState)



	def makeInvalid(self):
		"""
		mark the pointer as invalid
		"""
		self._invalidState = True
		return	self





#	--------------------------------------------------------
#	method used to update the value and state of the pointer
#	--------------------------------------------------------
	def	set(self, pointerValue):
		"""
		assigns a value to the pointer, based on the value supplied
		None represents a null pointer
		tuple of the form (object ID, offset)
		integer = object ID implies offset = 0
		"""
#	is it a null pointer?
		if pointerValue is None:
			self._nullState = True
			self._invalidState = False
			self._objectID = None
			self._offset = None

#	is it a tuple pair?
		elif type(pointerValue) is tuple:
			self._nullState = False
			self._invalidState = False
			self._objectID = pointerValue[0]
			self._offset = pointerValue[1]

#	how about another pointer?
		elif type(pointerValue) is TLCPointer:
			if	pointerValue.isNull():
				self.set(None)
			else:
				self.set((pointerValue.objectID, pointerValue.offset))

#	must be an object ID
		else:
			self.set((pointerValue,0))

#	make sure we're in range
		if	not self.isNull() and (self.objectID < 0 or self.offset < 0):
			self.makeInvalid()





#	=======================
#	math function overloads
#	=======================
	def	__add__(self, value):
		"""
		add to a pointer; ONLY affects the offset
		"""
		if	self.isNull():
			return	TLCPointer()

		return	TLCPointer((self._objectID, self.offset + value))



	def	__iadd__(self, value):
		"""
		in-place addition on a pointer; ONLY affects the offset
		"""
		if	not self.isNull():
			self.set((self.objectID, self.offset + value))

		return self



	def	__sub__(self, value):
		"""
		subtraction on a pointer
		pointer-pointer returns an integer for the same object id or None if objectIDs don't match
		pointer-integer returns a pointer
		"""
		if	self.isNull():
			return	TLCPointer()

		if	type(value) is TLCPointer:
			if	self.objectID != value.objectID:
				return	None

			return	self.offset - value.offset

		return	TLCPointer((self._objectID, self.offset - value))



	def	__isub__(self, value):
		"""
		in-place subtraction on a pointer; ONLY affects the offset
		"""
		if	not self.isNull():
			self.set((self.objectID, self.offset - value))

		return self





#	=================
#	logical operators
#	=================
	def	__bool__(self):
		"""
		returns True if the pointer is good, or False otherwise
		"""
		return self.isNull()



	def	__eq__(self, target):
		"""
		compares two pointers and returns equality
		"""
		if	target is None:
			if	self.isNull():
				return True
			return False

		elif type(target) is not TLCPointer:
			return False

		else:
			return	(self.objectID == target.objectID) and (self.offset == target.offset) and (self.isNull() == target.isNull()) and (self.isInvalid() == target.isInvalid())


