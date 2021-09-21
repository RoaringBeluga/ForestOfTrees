from forest.questacks.queue import Queue
from forest.trees.BinaryTree import Node

if __name__ == '__main__':
    print('Baobab Traversolator')

    root = Node((0, 'Root'))
    root.set_left(Node((1, 'Left')))
    root.set_right(Node((4, 'Right')))
    root.get_left().set_left(Node((2, 'Left to Left')))
    root.get_left().set_right(Node((3, 'Right to Left')))
    root.get_right().set_right(Node((5, 'Right to Right')))

    print('Postorder traversal')
    root.traverse_post_order()
    print('Inorder traversal')
    root.traverse_in_order()
    print('Preorder traversal')
    root.traverse_pre_order()
    print('Level traversal')
    root.traverse_level()

    q = Queue()
    q.push_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A'])
    print(f'Our Q is: {q.as_list()}')
    for i in q:
        print(f'Another element: {i}')
