#!/usr/bin/python3

from collections import deque
queue=deque(["Eric","John","Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())   #the first to arrive now leaves
print(queue.popleft())   #the second to arrive now leaves
print(queue)   #print the queue
