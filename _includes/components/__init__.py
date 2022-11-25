"""
loads the various components used in the TLCvm
"""
print("Loading components")





#	====================
#	the basic stack used
#	====================
from .stack import *
from .deque import *
from .registers import *
from .processor import *





#	==================================
#	list of all names exported for use
#	==================================
__all__ = [
	*stack.__all__,
	*deque.__all__,
	*registers.__all__,
	]
