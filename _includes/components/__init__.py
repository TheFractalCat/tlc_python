"""
loads the various components used in the TLCvm
"""
print("Loading components")



#	==========================
#	exceptions used by the TLC
#	==========================
from .tlc_exceptions import *



#	============================
#	publisher/subscriber classes
#	============================
from .publisher import *



#	====================
#	the basic stack used
#	====================
from .stack import *



#	===========================
#	the indexed dictionary used
#	===========================
from .dict import *



#	============
#	TLC pointers
#	============
from .tlc_pointers import *



#	=============
#	object memory
#	=============
from .object_memory import *



#	==============================
#	the "atomic" memory cells used
#	==============================
from .nodes	import *



#	===========================
#	registers used by the tlcVM
#	===========================
from .registers	import *



#	=====================================
#	the virtual processor used by the TLC
#	=====================================
from .processor	import *



#	==================================
#	list of all names exported for use
#	==================================
__all__ = [
	*tlc_exceptions.__all__,
	*tlc_pointers.__all__,
	*publisher.__all__,
	*stack.__all__,
	*dict.__all__,
	*object_memory.__all__,
	*registers.__all__,
	*nodes.__all__,
	*processor.__all__,
	]
