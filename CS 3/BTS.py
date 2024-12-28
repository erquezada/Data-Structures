from BTs import BinaryTree
from BTs import Node
from BTs import *

#######################################################################
class BinarySearchTree(BinaryTree):
    
  def __init__(self,root = None):
    self.root = root

  def insert(self, value):
    # Kept this so I wouldnt have to pass self.root in the calls within main function every time
    self._insert(value,self.root)

  def _insert(self, value, node):
    if not node:
      return Node(value)
    else:
      if value <= node.value:
        if node.left is None:
          node.left = Node(value)
        else:
          self._insert(value, node.left)
      else:
        if node.right is None:
          node.right = Node(value)
        else:
          self._insert(value, node.right)

  def search(self, value, node):
    # Activity 3
    if not node:
      return False
    elif node.value == value:
      return True
    elif value < node.left:
      return self.search(value, node.left)
    else:
      return self.search(value, node.right)

  def delete(self, value):
    self._delete(value,self.root)

  def _delete(self, value, node):
    # Activity 4
    if not node:
      return False
    elif node.value == value:
      if not node.left and not node.right:
        node = None
        return True
      else:
        node = node.right
        return True
    elif value <= node.value:
      self._delete(value, node.left)
    else:
      self._delete(value, node.right)

  def max_node(self, node):
    while node.right is not None:
      node = node.right
    return node

#######################################################################

tree = BinarySearchTree(Node(8))
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

print("Pre Order: " , preOrder(tree.root,[]))
print("Pre Order with Stack: ",preOrderWithStack(tree.root,[]))
print("Post Order: ",postOrder(tree.root,[]))
print("In Order:",inOrder(tree.root,[]))
print("Level Order: ", levelOrder(tree.root))

print("------------------------------------")
tree.delete(13)
print("Deleted Node with value 5")
print("Pre Order: " , preOrder(tree.root,[]))
tree.delete(8)
print("Deleted Node with value 4 (root)")
print("Pre Order: " , preOrder(tree.root,[]))
print("Tree Root: ", tree.root.value)