class CustomQueue:
    def __init__(self, limit=None):
        self.capacity = limit
        self.input_stack = []   # добавления элементов
        self.output_stack = []  # извлечения элементов

    def push(self, value):
        # если лимит задан и очередь достигла предела
        if self.capacity is not None and self._current_size() == self.capacity:
            self.pop()  # удаляем самый старый элемент
        self.input_stack.append(value)

    def pop(self):
        if not self.input_stack and not self.output_stack:
            return None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self):
        if not self.input_stack and not self.output_stack:
            return None
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def _current_size(self):
        return len(self.input_stack) + len(self.output_stack)


# тест
if __name__ == "__main__":
    queue = CustomQueue(3)
    
    queue.push('A')
    queue.push('B')
    queue.push('C')
    print(queue.peek())
    
    queue.push('D')
    print(queue.pop())
    print(queue.pop())
    print(queue.pop()) 
