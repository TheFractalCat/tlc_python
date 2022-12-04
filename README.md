# TLC in python - version 3 #
## Stack - a LIFO stack ##

zero-indexed from the top (the most recent entry); negative indexes start with the oldest entry
<br />most methods throw `IndexError` if request is out of range

|Method|Description|
|:-:|-|
|clear()|Clear the stack completely|
|peek(index)| returns the value at the requested location in the stack|
|poke(index, newValue)|replaces the current value at the requested location on the stack with the new value|
|push(newValue)|places a new value on the top of the stack|
|pull()|removes and returns the top value on the stack; throws `IndexError` if stack is empty|
|duplicate(offset=0)|places a copy of the requested value on the top of the stack|
|rotate(depth)|"rotates" the first `depth` values on the stack<br />a negative `depth` rotates deeper in the stack;<br/>a positive `depth` rotates towards the top of the stack|
|array indexes|wrappers for `peek` and `poke`|
|Iteration support|allows walking through the stack from newest entry, and returns `len(Stack)` if requested|

## Deque - the basic deque used by the TLCvm ##

the deque allows additions and removals from both ends; the primary direction is queue-oriented (add to one end, and remove from the other)

zero-indexed from the oldest entry; negative indexes start with the newest entry
<br />most methods throw `IndexError` if request is out of range

|Method|Description|
|:-:|-|
|clear()|Clear the deque completely|
|peek(index)| returns the value at the requested location in the deque|
|poke(index, newValue)|replaces the current value at the requested location on the deque with the new value|
|append(newValue)|places a new value on the bottom of the deque|
|prepend(newValue)|places a new value on the top of the deque|
|popNewest()|removes and returns the bottom value on the deque; throws `IndexError` if deque is empty|
|popOldest()|removes and returns the top value on the deque; throws `IndexError` if deque is empty|
|frot(depth)|"rotates" the first `depth` values on the deque, starting with the oldest entries<br />a negative `depth` rotates deeper in the deque;<br/>a positive `depth` rotates towards the top of the deque|
|rrot(depth)|"rotates" the first `depth` values on the deque, starting with the newest entries<br />a negative `depth` rotates deeper in the deque;<br/>a positive `depth` rotates towards the bottom of the deque|
|isEmpty()|returns True if the deque is empty, or False otherwise|
|addTrigger(trigger)|adds a function (or a bound method) to be called when an entry is added to the deque|
|removeTrigger()|clears any trigger that might have been set|
|array indexes|wrappers for `peek` and `poke`|
|Iteration support|allows walking through the stack from newest entry, and returns `len(Stack)` if requested|


## Processor - the tlcVM processor object ##
|Register|Value|
|:-:|-|
|DS|Data Stack|
|RS|Return Stack|
|OS|Object Stack|
|PS|Processor Stack|
|WS|Word Stack; used to manage the search dictionary|
