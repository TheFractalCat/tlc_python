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
		return	"{:}".format(self.currentValue)





#	-----------------------------------------------
#	method used to update the value of the register
#	-----------------------------------------------
	def	set(self, newValue):
		"""
		assigns a value to the register, based on the value supplied
		"""
		self._value = newValue
		return	self




#	-----------------------------
#	externally visible properties
#	-----------------------------
	@property
	def currentValue(self):
		"""
		return the current value of the register
		"""
		return	self._value




	@property
	def	publisher(self):
		"""
		returns the publisher associated with the register, generating one if needed
		"""
		if	self._publisher is None:
			self._publisher = Publisher()

		return self._publisher



	@property
	def	subscriber(self):
		"""
		returns the subscriber associated with the register, generating one if needed
		"""
		if	self._subscriber is None:
			self._subscriber = Subscriber()

		return self._subscriber
