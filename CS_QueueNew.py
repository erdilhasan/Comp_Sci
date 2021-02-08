class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.front_pointer = 0
        self.end_pointer = -1
        self.queue = [None] * max_size

    def enqueue(self, new_item):
        if self.size < self.max_size:
            self.end_pointer += 1
            if self.end_pointer == self.max_size:
                self.end_pointer = 0
            self.queue[self.end_pointer] = new_item
            self.size += 1
        else:
            print("Queue Full")

    def dequeue(self):
        item = None
        if self.size > 0:
            item = self.queue[self.front_pointer]
            self.queue[self.front_pointer] = None
            self.size -= 1
            self.front_pointer += 1
        else:
            print("Queue Empty")
        return item

    def show(self):
        queue_list = []
        for self.front_pointer in range(self.size):
            if self.queue[self.front_pointer] != None:
                queue_list.append(self.queue[self.front_pointer])
        print(*queue_list)


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.queue)

q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)
q.enqueue(99)
print(q.queue)

q.enqueue(100)
print(q.queue)
q.enqueue(101)
print(q.queue)
q.dequeue()
print(q.queue)
q.show()
