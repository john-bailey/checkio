# binary search tree patterns

# define a node for a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# return nodes in non-decreasing order
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end= ' ')
        inOrder(root.right)

# used to create a copy of the tree
def preOrder(root):
    if root:
        print(root.val, end=' ')
        preOrder(root.left)
        preOrder(root.right)

# used to delete a tree
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val, end=' ')

    

# load tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# check returns

print('\ninOrder:')
inOrder(root)

print('\npreOrder:')
preOrder(root)

print('\npostOrder:')
postOrder(root)


# new tree
tree = Node(25)
tree.left = Node(15)
tree.right = Node(50)
tree.left.left = Node(10)
tree.left.right = Node(22)
tree.right.left = Node(35)
tree.right.right = Node(70)
tree.left.left.left = Node(4)
tree.left.left.right = Node(12)
tree.left.right.left = Node(18)
tree.left.right.right = Node(24)
tree.right.left.left = Node(31)
tree.right.left.right = Node(44)
tree.right.right.left = Node(66)
tree.right.right.right = Node(90)

# check return
print('\ninOrder:')
inOrder(tree)

print('\npreOrder:')
preOrder(tree)

print('\npostOrder:')
postOrder(tree)