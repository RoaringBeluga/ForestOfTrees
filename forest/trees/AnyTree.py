class Node:
    def __init__(self, value, parent=None):
        self._value = value
        self._parent = parent
        self._left = None
        self._right = None
        self._traverse_func = lambda v: print(f'Node value: {v}')

    def set_parent(self, parent):
        self._parent = parent
        self._traverse_func = self._parent._traverse_func

    def set_left(self, left):
        self._left = left
        self._left.set_parent(self)

    def set_right(self, right):
        self._right = right
        self._right.set_parent(self)

    def wither(self):
        self._value = None
        if self._left:
            self._left.wither()
            del self._left
            self._left = None
        if self._right:
            self._right.wither()
            del self._right
            self._right = None

    def traverse_in_order(self):
        if self._left:
            self._left.traverse_in_order()
        self._traverse_func(self._value)
        if self._right:
            self._right.traverse_in_order()

    def traverse_pre_order(self):
        self._traverse_func(self._value)
        if self._left:
            self._left.traverse_pre_order()
        if self._right:
            self._right.traverse_pre_order()

    def traverse_post_order(self):
        if self._left:
            self._left.traverse_post_order()
        if self._right:
            self._right.traverse_post_order()
        self._traverse_func(self._value)

    def set_traverse(self, traverse_func):
        self._traverse_func = traverse_func
        if self._left:
            self._left.set_traverse(traverse_func)
        if self._right:
            self._right.set_traverse(traverse_func)

    def right_subtree(self):
        return self._right

    def left_subtree(self):
        return self._right

    def is_leaf(self):
        return self._left is None and self._right is None
