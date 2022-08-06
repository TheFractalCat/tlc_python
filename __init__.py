"""
the Threaded Language Compiler, in python - Version 1
"""
print("Loading pytlc")



#	========================================================
#	"hidden" module used to include all other modules needed
#	========================================================
from ._includes import *



#	==================================
#	list of all names exported for use
#	==================================
__all__ = [
	*_includes.__all__,
	]
