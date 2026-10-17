prev = 0
prev1 = 1

print(prev)
print(prev1)

for fibo in range(18):
    newFibo = prev1 + prev
    print(newFibo)
    prev = prev1
    prev1 = newFibo


"""
this shows how we can do fibo with loops, we can also do fibo with recursions this is introduce the concept of algorothms and how to choose the 
the most efficient
"""

start = 0
start2 = 1

print(start)
print(start2)

for f in range(10):
    newStart = start + start2
    print(newStart)
    start = start2
    start2 = newStart

