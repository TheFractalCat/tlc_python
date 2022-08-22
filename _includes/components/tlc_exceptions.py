"""
this module defines all exceptions used by the TLC
"""




#	-----------
#	export list
#	-----------
__all__ = [
			'TLCException',
		]





class TLCException(Exception):
	"""
	The base class used for defining exceptions used by the TLC
	"""

#	====================
#	class variables used
#	====================
#	used in gerating exceptionIDs for TLCExceptions
	_nextExceptionID = 10001





	def	__init__(self,message,*,ExceptionID=None):
		"""
		constructor used to build the TLCExceptions.
		optional ExceptionID can be specified which will override system assigned value
		"""
#	assign/generate exceptionID
		if	ExceptionID is None:
			self._exceptionID = TLCException._nextExceptionID
			TLCException._nextExceptionID += 1
		else:
			self._exceptionID = ExceptionID

#	save exception message
		self._message = message

#	and trigger baseclass constructor
		super().__init__(self.getMessage())





	def	__repr__(self):
		"""
		provides a printable form of the exception
		"""
		return self.getMessage()





	def	getMessage(self):
		"""
		returns the message associated with the exception
		"""
		return	f'{self._message} ({self.getExceptionID()})'





	def	getExceptionID(self):
		"""
		returns the numeric exceptionID assigned to the exception
		"""
		return	self._exceptionID





#	==========================
#	define all exceptions used
#	==========================
TLC_OK 						= TLCException('OK',ExceptionID=0)
__all__.append("TLC_OK")

TLC_EMPTY_RETURN_STACK 		= TLCException('Empty Return Stack')
__all__.append("TLC_EMPTY_RETURN_STACK")

TLC_POINTER_OUT_OF_RANGE 	= TLCException('Pointer Out of Range')
__all__.append("TLC_POINTER_OUT_OF_RANGE")

TLC_INVALID_OBJECTID 		= TLCException('Invalid ObjectID')
__all__.append("TLC_INVALID_OBJECTID")

TLC_INVALID_STACKINDEX 		= TLCException('Invalid Stack Index')
__all__.append("TLC_INVALID_STACKINDEX")
