class TwoStackQueue:
    def __init__(self, limit=None):
        self.capacity = limit          # максимальный размер
        self.stack_add = []            # (enqueue)
        self.stack_remove = []         # (dequeue)
        self.operations_count = 0      # счётчик операций 
    
    def enqueue(self, value):
        if self.capacity is not None and self.size() >= self.capacity:
            self.dequeue()
        
        self.stack_add.append(value)
        self.operations_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста!")
        
        if not self.stack_remove:
            while self.stack_add:
                self.stack_remove.append(self.stack_add.pop())
        
        self.operations_count += 1
        return self.stack_remove.pop()
    
    def front(self):
        if self.is_empty():
            raise IndexError("Очередь пуста!")
        
        if not self.stack_remove:
            while self.stack_add:
                self.stack_remove.append(self.stack_add.pop())
        
        return self.stack_remove[-1]
    
    def is_empty(self):
        return len(self.stack_add) == 0 and len(self.stack_remove) == 0
    
    def size(self):
        return len(self.stack_add) + len(self.stack_remove)
    
    def clear(self):
        self.stack_add.clear()
        self.stack_remove.clear()
    
    def display(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        
        elements = []
        while not self.is_empty():
            elements.append(self.dequeue())
        
        print(" -> ".join(map(str, elements)))
        
        for elem in elements:
            self.enqueue(elem)
    
    def contains(self, value):
        return value in self.stack_add or value in self.stack_remove
    
    def get_operations_count(self):
        return self.operations_count


if __name__ == "__main__":
    queue = TwoStackQueue(limit=3)
    
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(f"Первый элемент: {queue.front()}")
    
    queue.enqueue('D')
    print(f"Размер: {queue.size()}")
    
    queue.display()
    
    print(f"Извлечено: {queue.dequeue()}")
    print(f"Извлечено: {queue.dequeue()}")
    print(f"Извлечено: {queue.dequeue()}")
    
    print(f"Очередь пуста? {queue.is_empty()}")
    print(f"Всего операций: {queue.get_operations_count()}")
