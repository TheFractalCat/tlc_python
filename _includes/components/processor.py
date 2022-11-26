"""
this module defines the basic TLC processor used by the tlcVM
"""



#	==============
#	imports needed
#	==============
from .stack import *
from .deque import *
from .tlc_exceptions import *
from .publisher import *
from .tlc_pointers import *
from .registers import *
# from .nodes import *
from .object_memory import *



#	===========
#	export list
#	===========
__all__ = [
			'TLCProcessor',
		]




#	=======================================
#	the virtual processor used by the TLCvm
#	=======================================
class TLCProcessor:
	"""
	the virtual processor used by the TLC
	"""



#	======================================
#	class variables, constants and methods
#	======================================
	_MAX_STACKS = 5
	_INVALID_OBJECT  = TLCInvalidNode()
	_NIL = TLCNilNode()





#	-----------------------------------------------------------
#	class method used for "pretty-printing" the processor state
#	-----------------------------------------------------------
	@classmethod
	def	Show(cls, name, value,*,prefixLength=30, suffixLength=20):
		"""
		class method used for "pretty-printing" the processor state
		"""
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
		subscription handler used for keeping OC and EOC pointers in sync
		"""

		if transactionType == 'p':
			subscriberData.set(publisherData)



	def	subhandler2(self, transactionType, publisher, subscriberData, publisherData):
		"""
		subscription handler used for populating the COR from the EOC
		"""

		if transactionType == 'p':
			subscriberData.set(self.OM[publisherData])




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
		for i in range(0,self.MAX_STACKS):
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

#	-----------------------------
#	and the currentObjectRegister
#	-----------------------------
		self._currentObjectRegister = TLCRegister()

#	---------------------
#	and object memory too
#	---------------------
		self._objectMemory = ObjectMemory(self.INVALID_OBJECT)

#	------------------------------
#	set the default invalid object
#	------------------------------
		TLCNode.setDefaultObject(TLCProcessor.INVALID_OBJECT)

#	------------------------
#	now set up subscriptions
#	------------------------
		self.EOC.subscriber.subscribeTo(self.OC.publisher, additionalData=self.EOC)
		self.COR.subscriber.subscribeTo(self.EOC.publisher, additionalData=self.COR)

#	------------
#	and handlers
#	------------
		self.EOC.subscriber.setDeliveryHandler(self.OC.publisher,self.subhandler1)
		self.COR.subscriber.setDeliveryHandler(self.EOC.publisher,self.subhandler2)





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
		response += TLCProcessor.Show("\nCurrentObjectRegister", self.COR, prefixLength=31, suffixLength=30)

		response += TLCProcessor.Show("\n\nExceptionState", self.ES, prefixLength=32, suffixLength=30)

		response += "\n\n--Object Memory--\n{:}".format(self.OM)

		return response




#	===============================
#	processor component definitions
#	===============================
	def	stack(self, stackIndex):
		"""
		allows an indexed reference to a particular stack
		"""
		if	0 <= stackIndex < self.MAX_STACKS:
			return	self._stacks[stackIndex]

		raise TLC_INVALID_STACKINDEX



	@property
	def MAX_STACKS(self):
		"""
		make MAX_STACKS read-only
		"""
		return TLCProcessor._MAX_STACKS



	@property
	def INVALID_OBJECT(self):
		"""
		make INVALID_OBJECT read-only
		"""
		return TLCProcessor._INVALID_OBJECT



	@property
	def NIL(self):
		"""
		make NIL read-only
		"""
		return TLCProcessor._NIL




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



	@property
	def COR(self):
		"""
		COR is the current object register
		"""
		return	self._currentObjectRegister



	@COR.setter
	def COR(self, value):
		"""
		assign a new value to the current object register
		"""
		self._currentObjectRegister.set(value)



	@property
	def OM(self):
		"""
		OM is the object memory used
		"""
		return	self._objectMemory

