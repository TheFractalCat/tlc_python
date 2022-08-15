"""
this is the module that adds publishing capabilty to objects
"""



#	-----------
#	export list
#	-----------
__all__ = ['Publisher', 'Subscriber']





class Publisher:
	"""
	Implements the broadcast side of publisher/subscriber
	"""




	def __init__(self, publisherID=None):
		"""
		Constructor - builds the empty subscriber list
		"""
		self._subscribers = dict()
		self._id = hex(id(self)) if publisherID is None else publisherID






	def subscribe(self, subscriber,*,additionalData=None):
		"""
		Add a subscriber to the subscription list
		"""
		self._subscribers[hex(id(subscriber))] = (subscriber, additionalData)
		subscriber._deliver('a', self, additionalData, None)





	def unsubscribe(self, subscriber, *,additionalData=None):
		"""
		Remove a subscriber from the subscription list
		"""
		if ((client := self._subscribers.pop(hex(id(subscriber)), None))) is not None:
			client[0]._deliver('u', self, client[1], additionalData)





	def publish(self, additionalData=None):
		"""
		Publish event to all subscribers
		"""
		for s in self._subscribers.values():
			s[0]._deliver('p', self, s[1], additionalData)





	def	getID(self):
		"""
		return the ID assigned to this publisher
		"""
		return	self._id





class Subscriber:
	"""
	The receiver side of the publisher/subscriber model
	"""



	def __init__(self, subscriberID=None):
		"""
		Constructor - builds the empty subscription dictionary and initializes the boundDeliveryHandler
		"""
		self._subscriptions = dict()
		self._boundDeliveryHandler = None





	def subscribeTo(self, publisher, *, additionalData=None):
		"""
		Subscribe to a publisher's offering
		"""
		if	publisher.getID() not in self._subscriptions:
			self._subscriptions[publisher.getID()] = (publisher, self.deliver)

		if	additionalData is None:
			publisher.subscribe(self)
		else:
			publisher.subscribe(self, additionalData=additionalData)




	def unsubscribeFrom(self, publisher, *, additionalData=None):
		"""
		Unsubscribe from a publisher's offering
		"""
		if	publisher.getID() in self._subscriptions:

			if	additionalData is None:
				publisher.unsubscribe(self)
			else:
				publisher.unsubscribe(self, additionalData=additionalData)
			self._subscriptions.pop(publisher.getID())




	def unsubscribeFromAll(self, *, additionalData=None):
		"""
		Unsubscribe from all publishers
		"""
		for publisher in self._subscriptions.values():
			if	additionalData is None:
				publisher[0].unsubscribe(self)
			else:
				publisher[0].unsubscribe(self, additionalData=additionalData)

		self._subscriptions.clear()




	def _deliver(self, transactionType, publisher, subscriberData, publisherData):
		"""
		Invoked by the publisher when they have an event to deliver
		this extracts the handler from the subscription dictionary and calls it with all data
		"""

		if	(publisherEntry := self._subscriptions.get(publisher.getID(), None)) is not None:
				publisherEntry[1](transactionType, publisher, subscriberData, publisherData)





	def deliver(self, transactionType, publisher, subscriberData, publisherData):
		"""
		Invoked by the publisher when they have an event to deliver
			this is the default handler which should be replaced by the actual handler
		"""
		pass




	def setDeliveryHandler(self, publisher, handler):
		"""
		replace the Delivery handler with another method
		"""
		self._subscriptions[publisher.getID()] = (publisher, handler)





	def __repr__(self):
		"""Return a representation of the Subscriber"""
		return super(type(self), self).__repr__()
