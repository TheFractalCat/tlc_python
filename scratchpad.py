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





try:
	raise pytlc.TLC_POINTER_OUT_OF_RANGE
except pytlc.TLCException as e:
	print(e.getMessage(), e.getExceptionID())






def	Show(name, value):
	name = "{:s} ".format(name)
	name = "{:.<25s}".format(name)

	value = ": {:s}".format(str(value))
	value = "{:.>25s}".format(value)

	return "{:s}{:s}".format(name, value)



import pytlc
p1 = pytlc.TLCPointer((123,1))
p2 = pytlc.TLCPointer(p1)
p3 = pytlc.TLCPointer(p1+10)
p4 = pytlc.TLCPointer()
p = [p1, p2, p3, p4]
p
vp = pytlc.TLCProcessor()
vp

d = pytlc.deque()
"{:019_X}".format(id(d))
