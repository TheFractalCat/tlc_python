"""
this module defines the registers used by the TLCvm
"""



#	==============
#	imports needed
#	==============
from .publisher import *





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

#	and the backup values
		self._oldvalue = self._value

#	set up the default validity checker
		self._valueChecker = self.defaultValidityChecker

#	set up the instance variables needed for publishing/subscribing
		self._publisher = None
		self._subscriber = None

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





#	==========================================
#	commit changes to the register and publish
#	==========================================
	def	commit(self):
		if	self._oldvalue != self._value:
			self._oldvalue = self._value

			if	self._publisher is not None:
				self._publisher.publish(additionalData=self)




#	==========================================
#	default validity checker; accepts ANYTHING
#	==========================================
	def	defaultValidityChecker(self, newValue):
		"""
		default validity checker; always returns True
		"""
		return	True



#	=====================================================================
#	set the validity checker used to ensure only good values are accepted
#	=====================================================================
	def	setValidityChecker(self, checker):
		"""
		assigns a validity checker to the register
		"""
		self._valueChecker = checker




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



#	-----------------------------------------------
#	method used to update the value of the register
#	-----------------------------------------------
	def	set(self, newValue):
		"""
		assigns a value to the register, based on the value supplied
		"""

#	first, check for validity
		isValid = self._valueChecker(newValue)

		if	isValid:
			self._value = newValue

#	and publish the changes, if needed
			self.commit()

#	return results of validity check
		return	isValid
