"""
this module defines the basic TLC processor used by the tlcVM
"""



#	==============
#	imports needed
#	==============
from .stack import *
from .tlc_exceptions import *
from .publisher import *
from .tlc_pointers import *




#	===========
#	export list
#	===========
__all__ = [
			'TLCProcessor',
		]





class TLCProcessor:
	"""
	the virtual processor used by the TLC
	"""

#	=============================
#	class variables and constants
#	=============================
	MAX_STACKS = 5




	@classmethod
	def	Show(cls, name, value,*,prefixLength=30, suffixLength=20):
		name = "{:s} ".format(name)
		name = "{0:.<{1}s}".format(name, prefixLength)

		value = ": {:s}".format(str(value))
		value = "{0:.>{1}s}".format(value, suffixLength)

		return "{:s}{:s}".format(name, value)




#	============================
#	subscription handlers needed
#	============================
	def	subhandler1(self, transactionType, publisher, subscriberData, publisherData):
		"""
		subscription handler used for keeping pointers in sync
		"""

		if transactionType == 'p':
			subscriberData.set(publisherData)




#	===========
#	constructor
#	===========
	def	__init__(self):
		"""
		constructor for building the virtual processor
		"""
#	----------------------
#	define the stacks used
#	----------------------
		self._stacks = list()
		for i in range(0,TLCProcessor.MAX_STACKS):
			self._stacks.append(TLCStack())

#	-----------------------------------
#	provide direct references to stacks
#	-----------------------------------
		self._RS = self._stacks[0]
		self._DS = self._stacks[1]
		self._IS = self._stacks[2]
		self._SS = self._stacks[3]

#	--------------------------
#	set up the exception state
#	--------------------------
		self._exceptionState = TLC_OK

#	----------------------
#	and the ObjectCounters
#	----------------------
		self._objectCounter = TLCPointer()
		self._effectiveObjectCounter = TLCPointer()

#	------------------------
#	now set up subscriptions
#	------------------------
		self.EOC.subscriber.subscribeTo(self.OC.publisher, additionalData=self.EOC)

#	------------
#	and handlers
#	------------
		self.EOC.subscriber.setDeliveryHandler(self.OC.publisher,self.subhandler1)





#	========================
#	processor representation
#	========================
	def	__repr__(self):
		"""
		provides a string version of the VM state
		"""
		response =  TLCProcessor.Show("DataStack", self.DS, suffixLength=30)
		response += TLCProcessor.Show("\nReturnStack", self.RS,prefixLength=31, suffixLength=30)
		response += TLCProcessor.Show("\nIterationStack", self.IS, prefixLength=31, suffixLength=30)
		response += TLCProcessor.Show("\nSuspenseStack", self.SS, prefixLength=31, suffixLength=30)

		response += TLCProcessor.Show("\n\nObjectCounter", self.OC, prefixLength=32, suffixLength=30)
		response += TLCProcessor.Show("\nEffectiveObjectCounter", self.EOC, prefixLength=31, suffixLength=30)

		response += TLCProcessor.Show("\n\nExceptionState", self.ES, prefixLength=32, suffixLength=30)

		return response




#	===============================
#	processor component definitions
#	===============================
	def	stack(self, stackIndex):
		"""
		allows an indexed reference to a particular stack
		"""
		if	0 <= stackIndex < TLCProcessor.MAX_STACKS:
			return	self._stacks[stackIndex]

		raise TLC_INVALID_STACKINDEX





	@property
	def RS(self):
		"""
		RS is the Return Stack
		"""
		return	self._RS



	@property
	def DS(self):
		"""
		DS is the Data Stack
		"""
		return	self._DS



	@property
	def IS(self):
		"""
		IS is the Iteration Stack
		"""
		return	self._IS



	@property
	def SS(self):
		"""
		SS is the Suspense Stack
		"""
		return	self._SS



	@property
	def ES(self):
		"""
		ES is the Exception State
		"""
		return	self._exceptionState

	@ES.setter
	def ES(self, value):
		"""
		set the new value for Exception State
		"""
		self._exceptionState = value



	@property
	def OC(self):
		"""
		OC is the object counter
		"""
		return	self._objectCounter



	@OC.setter
	def OC(self, value):
		"""
		assign a new value to the object counter
		"""
		self._objectCounter.set(value)



	@property
	def EOC(self):
		"""
		EOC is the effective object counter
		"""
		return	self._effectiveObjectCounter



	@EOC.setter
	def EOC(self, value):
		"""
		assign a new value to the effective object counter
		"""
		self._effectiveObjectCounter.set(value)
