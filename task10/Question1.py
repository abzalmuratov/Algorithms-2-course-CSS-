class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self): self.head = None

    def is_empty(self): return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def push(self, item):
        current = self.head
        if current is None:
            self.head = Node(item)
        else:
            while current.next:
                current = current.next
            current.next = Node(item)

    def pop(self) :
        current_pos = self.size()
        prev = None
        current = self.head
        while current.next and current_pos < 0:
            prev = current
            current = current.next
            current_pos -= 1
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return current.data

    def print(self) :
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next

class Queue:
    def __init__(self): self.items = []

    def isEmpty(self): return self.items == []

    def enqueue(self, item): self.items.insert(0,item)

    def dequeue(self): return self.items.pop()

    def size(self): return len(self.items)


class LLQueue:
    def __init__(self): self.items = LinkedList()

    def isEmpty(self): return self.items.is_empty()

    def enqueue(self, item): self.items.push(item)

    def dequeue(self): return self.items.pop()

    def size(self): return self.items.size()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
print(q.items)

qq = LLQueue()
qq.enqueue(11)
qq.enqueue(12)
qq.enqueue(13)
qq.enqueue(14)
qq.enqueue(15)
qq.dequeue()
qq.items.print()
