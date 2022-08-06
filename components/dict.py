"""
This module defines the basic structure and function of the TLC Dictionary - the fundamental named storage used by TLC
"""



#	-----------
#	export list
#	-----------
__all__ = ['TLCDict']



class	TLCDict:
	"""
	the basic named storage used by TLC - it allows access to a value by both name and index
	"""

	def	__init__(self, *, defaultValue=None, defaultKey=None):
		"""
		constructor for the class - initialized all internal storage needed by the class
		_names - dictionary used to cross-reference names to indexes within the values
		_values - list that stores the associated values tied to a name

		an optional default value and/or key can be specified, using named parameters
		"""

		self._names = dict()
		self._values = list()

#	add a default value
		if	defaultKey is not None:
			defaultKey = defaultKey.casefold()
			self._names[defaultKey] = 0

		self._values.append((defaultKey, 0, defaultValue))





	def	__repr__(self):
		"""
		provides a printable view of the object
		"""
		return	f'<{type(self).__name__} at {hex(id(self))}=Names{self._names};Values{self._values}>'





	def	addEntry(self, key, value):
		"""
		adds an entry to the TLCDict and returns the dictionary index
		"""
		key = key.casefold()
		index = len(self._values)
		self._values.append((key, index, value))
		self._names[key] = index

		return	index





	def	getEntry(self, target):
		"""
		looks up a dictionary entry and returns a tuple of the form (name, index, value)
		returns (None, None, None) if no match is found
		"""
		target = target.casefold()

		if	target in self._names:
			index = self._names[target]
			value = self._values[index]
			return	value
		else:
			return	(None, None, None)





	def	getDefaultEntry(self):
		"""
		Returns the default dictionary entry; a tuple of the form (name, index, value)
		"""
		return self._values[0]
