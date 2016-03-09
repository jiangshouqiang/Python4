import heapq
head = []
heapq.heappush(head,(5,"rest"))
heapq.heappush(head,(2,"work"))
heapq.heappush(head,(4,"study"))
print(head)

for x in head :
    print(type(x))