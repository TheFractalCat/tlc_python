"""
this module defines the registers used by the TLCvm
"""



#	==============
#	imports needed
#	==============





#	===========
#	export list
#	===========
__all__ = [
			'TLCRegister',
		]





class TLCRegister:
	"""
	the basic "onboard" storage used throughout the TLCvm
	"""

#	=====================================
#	class variables and constants, if any
#	=====================================




#	===========
#	constructor
#	===========
	def	__init__(self, initialValue=None):
		"""
		constructor for the register
		"""
#	define the storage for the register
		self._value = None

#	... then assign the initial value passed in
		self.set(initialValue)





#	==============================
#	method used for representation
#	==============================
	def	__repr__(self):
		"""
		provides a string version of the register
		"""
		return	"{:}".format(self.get())





#	-----------------------------------------------
#	method used to update the value of the register
#	-----------------------------------------------
	def	set(self, newValue):
		"""
		assigns a value to the register, based on the value supplied
		"""
		self._value = newValue
		return	self




#	-------------------------------------------------------
#	method used to return the current value of the register
#	-------------------------------------------------------
	def	get(self):
		"""
		return the current value of the register
		"""
		return	self._value
