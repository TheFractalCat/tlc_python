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




