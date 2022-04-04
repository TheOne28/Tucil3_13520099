from heapq import heappush, heappop

class PriorityQueue:

    def __init__(self):
        self.queue = []
    
    def length(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def empty(self):
        return self.length() == 0
    
    def clear(self):
        self.queue.clear()

    def pop(self):
        item = heappop(self.queue)
        return item

    def push(self, item):
        heappush(self.queue, item)
