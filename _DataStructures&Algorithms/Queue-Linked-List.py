class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


class QueueLinkedListManager:
    def __init__(self):
        self.queues = [QueueLinkedList() for _ in range(3)]

    def enqueue_element(self, element):
        lowest_sum = float('inf')
        lowest_sum_queue = None
        for queue in self.queues:
            current_sum = self.get_queue_sum(queue)
            if current_sum < lowest_sum:
                lowest_sum = current_sum
                lowest_sum_queue = queue
        if lowest_sum_queue is None:
            raise Exception("All queues are empty")
        if lowest_sum_queue.head is None or lowest_sum_queue.head.next is None:
            lowest_sum_queue.enqueue(element)
        else:
            lowest_sum_queue.enqueue(element)

    def dequeue_least(self):
        min_value = float('inf')
        min_queue = None
        for queue in self.queues:
            if not queue.is_empty() and int(queue.head.value) < min_value:
                min_value = int(queue.head.value)
                min_queue = queue
        if min_queue is None:
            raise Exception("All queues are empty")
        return min_queue.dequeue()

    def get_queue_sum(self, queue):
        if queue.is_empty():
            return 0
        queue_sum = 0
        current_node = queue.head
        while current_node:
            queue_sum += int(current_node.value)
            current_node = current_node.next
        return queue_sum

# Example usage
manager = QueueLinkedListManager()

print("----------------------------------")
for i, queue in enumerate(manager.queues):
    current_node = queue.head
    print(f"Queue {i+1}: ", end="")
    while current_node:
        print(current_node.value, end=" ")
        current_node = current_node.next
    print()

print("----------------------------------")
for i in range(3):
    element = int(input(f"Enter an element for queue {i+1}: "))
    manager.queues[i].enqueue(element)

print("----------------------------------")
for i, queue in enumerate(manager.queues):
    current_node = queue.head
    print(f"Queue {i+1}: ", end="")
    while current_node:
        print(current_node.value, end=" ")
        current_node = current_node.next
    print()

while True:
    print("""----------------------------------
[0] Exit
[1] Enqueue
[2] Dequeue""")

    Choice = input("Choice: ")

    match Choice:
        case '0':
            print("Thank you!")
            break
        case '1':
            print("----------------------------------")
            element = input("Enter an Element to Enqueue: ")
            manager.enqueue_element(element)
        case '2':
            try:
                dequeued_element = manager.dequeue_least()
                print("Dequeued element:", dequeued_element)
            except Exception as e:
                print("Error:", str(e))
                break

    for i, queue in enumerate(manager.queues):
        current_node = queue.head
        print(f"Queue {i+1}: ", end="")
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()  

# Documentation
"""
QueueLinkedList: A class representing a linked list implementation of a queue.
- is_empty(): Checks if the queue is empty.
- enqueue(value): Adds a new element to the end of the queue.
- dequeue(): Removes and returns the first element from the queue.

QueueLinkedListManager: A class managing three queues and performing operations on them.
- enqueue_element(element): Enqueues the element sequentially through each queue, choosing the queue with the lowest sum of values.
- dequeue_least(): Dequeues the least first element in comparison to all queues.
- get_queue_sum(index): Calculates the sum of values in a queue up to the given index.
"""

# Error Messages
"""
- Exception("Queue is empty"): Raised when trying to dequeue from an empty queue.
- Exception("All queues are empty"): Raised when all queues are empty.
- IndexError("Invalid queue index"): Raised when an invalid queue index is provided.
"""

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
    
class QueueLinkedListManager:
    def __init__(self):
        self.queues = [QueueLinkedList() for _ in range(3)]

    def enqueue_element(self, element):
        for i in range(3):
            if self.get_queue_sum(i) < self.get_queue_sum(i + 1):
                self.queues[i].enqueue(element)
                return
        self.queues[0].enqueue(element)

    def dequeue_least(self):
        min_value = float('inf')
        min_queue = None
        for queue in self.queues:
            if not queue.is_empty() and queue.head.value < min_value:
                min_value = queue.head.value
                min_queue = queue
        if min_queue is None:
            raise Exception("All queues are empty")
        return min_queue.dequeue()

    def get_queue_sum(self, index):
        if index < 0 or index >= len(self.queues):
            raise IndexError("Invalid queue index")
        queue_sum = 0
        for i in range(index + 1):
            current_queue = self.queues[i]
            current_node = current_queue.head
            while current_node:
                queue_sum += current_node.value
                current_node = current_node.next
        return queue_sum
    
manager = QueueLinkedListManager()

for i in range(3):
    element = input(f"Enter an element for queue {i+1}: ")
    manager.queues[i].enqueue(element)

while True:
    element = input("Enter an element to enqueue or 'q' to quit: ")
    if element == 'q':
        break
    manager.enqueue_element(element)

while True:
    try:
        dequeued_element = manager.dequeue_least()
        print("Dequeued element:", dequeued_element)
    except Exception as e:
        print("Error:", str(e))
        break

for i, queue in enumerate(manager.queues):
    current_node = queue.head
    print(f"Queue {i+1}: ", end="")
    while current_node:
        print(current_node.value, end=" ")
        current_node = current_node.next
    print()
