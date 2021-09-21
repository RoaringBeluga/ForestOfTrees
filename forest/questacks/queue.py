class Queue():
    def __init__(self):
        self._queue = []

    def __iter__(self):
        """ Queue is iterable! """
        return self

    def __next__(self):
        """ Return next element in the queue """
        if len(self._queue) > 0:
            return self._queue.pop()
        else:
            raise StopIteration()

    def __len__(self):
        return len(self._queue)

    def as_list(self):
        """ Return the copy of the queue as list"""
        return self._queue.copy()

    def push(self, value):
        self._queue.insert(0, value)

    def pop(self):
        return self._queue.pop()

    def push_list(self, lst):
        """ Push the list of elements into the queue """
        for i in lst:
            self._queue.insert(0, i)
