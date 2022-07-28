"""
This module defines the basic structure and function of the TLC Dictionary - the fundamental named storage used by TLC
"""



class	TLCDict:
	"""
	the basic named storage used by TLC - it allows access to a value by both name and index
	"""

	def	__init__(self):
		"""
		constructor for the class - initialized all internal storage needed by the class
		_names - dictionary used to cross-reference names to indexes within the values
		_values - list that stores the associated values tied to a name

		"""

		self._names = dict()
		self._values = list()





	def	addEntry(self, key, value):
		"""
		adds an entry to the TLCDict and returns the dictionary index
		"""
		self._values.append(value)
		index = len(self._values)-1
		self._names[key.casefold()] = index

		return	index





	def	getEntry(self, target):
		"""
		looks up a dictionary entry and returns a tuple of the form (index, value)
		returns (None, None) if no match is found
		"""
		target = target.casefold()

		if	target in self._names:
			index = self._names[target]
			value = self._values[index]
		else:
			index = None
			value = None

		return	(index, value)
