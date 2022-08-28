"""
this module defines the behavior of the pointers used by the TLCvm
"""



#	==============
#	imports needed
#	==============
from .publisher import *





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
#	define the list that represents all instance storage
		self._variables = [None]*4

#	and the backup values
		self._oldvalues = self._variables.copy()

#	first initialize instance variables ...
		self._nullState = True
		self._invalidState = False
		self._objectID = None
		self._offset = None
		self._publisher = None
		self._subscriber = None

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

		return	"{0:04d}|{1:d}".format(self.objectID, self.offset)





#	---------------------------------------------
#	property mappings from variable list to names
#	---------------------------------------------
	@property
	def _objectID(self):
		"""
		used to store the objectID associated with the pointer
		"""
		return	self._variables[0]



	@_objectID.setter
	def _objectID(self, value):
		"""
		assign a new object ID to the pointer
		"""
		self._variables[0] = value



	@property
	def _offset(self):
		"""
		used to store the offset associated with the pointer
		"""
		return	self._variables[1]



	@_offset.setter
	def _offset(self, value):
		"""
		assign a new offset to the pointer
		"""
		self._variables[1] = value



	@property
	def _nullState(self):
		"""
		used to indicate whether the pointer is null or not
		"""
		return	self._variables[2]



	@_nullState.setter
	def _nullState(self, value):
		"""
		change the null status of the pointer
		"""
		self._variables[2] = value



	@property
	def _invalidState(self):
		"""
		used to indicate whether the pointer is invalid or not
		"""
		return	self._variables[3]



	@_invalidState.setter
	def _invalidState(self, value):
		"""
		change the validity state of the pointer
		"""
		self._variables[3] = value



#	------------------------------------------
#	commit changes to the pointer and snapshot
#	------------------------------------------
	def	commit(self):
		if	self._oldvalues != self._variables:
			self._oldvalues = self._variables.copy()

			if	self._publisher is not None:
				self._publisher.publish(additionalData=self)





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
		self.commit()

		return	self



	@property
	def	publisher(self):
		"""
		returns the publisher associated with the pointer, generating one if needed
		"""
		if	self._publisher is None:
			self._publisher = Publisher()

		return self._publisher



	@property
	def	subscriber(self):
		"""
		returns the subscriber associated with the pointer, generating one if needed
		"""
		if	self._subscriber is None:
			self._subscriber = Subscriber()

		return self._subscriber



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
		try:
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
				self._variables = pointerValue._variables.copy()

#	must be an object ID
			else:
				self._nullState = False
				self._invalidState = False
				self._objectID = pointerValue
				self._offset = 0

#	make sure we're in range
			if	not self.isNull() and (self.objectID < 0 or self.offset < 0):
				self.makeInvalid()

#	check for an update state
		finally:
			self.commit()





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
			return self._variables == target._variables


