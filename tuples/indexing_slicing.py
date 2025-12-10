"""
INDEXING
>Each item in a tuple can be retrieved using index value,
placed inside square brackets.
>index usually begins at 0-N

The syntax to retrieve individual item is.

tuple_name[index]
"""

months= ("jan","feb","mar","apr","may","Jun")
#to retrieve apr
retrieve = months[3]
print(retrieve)

#to reverse indexing(-1,-2,-3,-N)
reverse_retrieval = months [-2]
print(reverse_retrieval)

""""
Slicing
This is extracting a chunk of tuples items.
In slicing,0:3, the last index is usually ignored i.e 3
the syntax: tuple_name[start: stop:step]
"""
colors = ("y","i","R","g","o")

#start and stop index value
extraction = colors[0:3]
print(extraction)

#start value only
start_value =colors[3:]
print(start_value)

#stop value only
stop_value = colors[:2]
print(stop_value)

#start,stop and step values
start_stop_step = colors[0:5:2]
print(start_stop_step)

#step only
step = colors[::2]
print(step)

#display in reverse
reverse_order = colors[::-1]
print(reverse_order)

#use the negative indexes
extra = colors[-5:-1]
ec = colors[-6:-3]
print(extra)
print(ec)
