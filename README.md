# TLC in python - version 3 #
## Stack - a LIFO stack, indexed from the top (the most recent entry) ##
|Method|Description|
|:-:|-|
|clear()|Clear the stack completely|
|duplicate(offset=0)|duplicates a value on the stack to the top of the stack; throws `IndexError` if out of range|
|pull()|removes and returns the top value on the stack; throws `IndexError` if stack is empty|
|push(newValue)|places a new value on the top of the stack|
|rotate(depth)|"rotates" the first `depth` values on the stack; a negative `depth` rotates deeper in the stack;<br/>a positive `depth` rotates towards the top of the stack;<br/>throws `IndexError` is stack isn't deep enough|
|array indexes|used to "peek" or "poke" values on the stack.<br/>Positive indexes work from the top, while negative indexes are relative to the bottom of the stack;<br/>throws `IndexError` is the index is out of range|

## Processor - the tlcVM processor object ##
|Register|Value|
|:-:|-|
|DS|Data Stack|
|RS|Return Stack|
|OS|Object Stack|
|PS|Processor Stack|
|WS|Word Stack; used to manage the search dictionary|
