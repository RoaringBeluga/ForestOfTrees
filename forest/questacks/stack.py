class Stack:
    def __init__(self, size=0):
        self._size = size if size > 0 else 0
        self._stack = []

    def as_list(self):
        """ Returns a copy of the stack as list """
        return self._stack.copy()

    def __len__(self):
        return len(self._stack)

    def __iter__(self):
        """ Stack is iterable! """
        return self

    def __next__(self):
        """ Return next element in the stack """
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            raise StopIteration()

    def size(self):
        return self._size if self._size > 0 else len(self)

    def push(self, value):
        if 0 < self._size == len(self):
            raise IndexError('Stack is full')
        else:
            self._stack.append(value)

    def push_list(self, lst):
        if type(lst) == list:
            for i in lst:
                self.push(i)
        else:
            raise TypeError('Parameter is not of list type')

    def pop(self):
        if len(self) > 0:
            return self._stack.pop()
        else:
            raise IndexError('pop from empty stack')
