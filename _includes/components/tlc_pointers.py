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





	def	__init__(self, pointerValue=None):
		"""
		constructor for building a pointer
		"""
#	first initialize instance variables ...
		self._nullState = True
		self._objectID = None
		self._offset = None

#	... then assign the value passed it
		self.set(pointerValue)





	def	__repr__(self):
		"""
		provides a string version of the pointer
		"""
		if	self._nullState:
			return "NULL"

		return	"{0:04d}|{1:+d}".format(self.objectID, self.offset)





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
			self._objectID = None
			self._offset = None

#	is it a tuple pair?
		elif type(pointerValue) is tuple:
			self._nullState = False
			self._objectID = pointerValue[0]
			self._offset = pointerValue[1]

#	must be an object ID
		else:
			self._nullState = False
			self._objectID = pointerValue
			self._offset = 0

