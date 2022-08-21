import pytlc

def ph(action,pub,sd,pd):
	print(f'type={action};pub={pub.getID()},subscriberData={sd},publisherData={pd}')

p = pytlc.Publisher()

s1 = pytlc.Subscriber()
s2 = pytlc.Subscriber()

s1.setDeliveryHandler(p,ph)
s2.setDeliveryHandler(p,ph)

s1.subscribeTo(p, additionalData='this is s1')
s2.subscribeTo(p, additionalData='this is s2')

p.publish('foo')






class classA:
	_counter = 10000

	def	__init__(self):
		print('Initializing classA')
		classA._counter += 1
		self._ID = classA._counter

	def	__repr__(self):
		return f'ID={self.getID()}'

	def	getID(self):
		return	self._ID

class classB(classA):

	def	__init__(self):
		super().__init__()
		print('initializing classB')


