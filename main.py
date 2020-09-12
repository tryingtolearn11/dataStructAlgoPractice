
class BinaryTreeNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = None
    self.left = left
    self.right = right
  
  # Inorder: Left Subtree -> Root -> Right Subtree
  def print_inorder_traversal(self, node):
    if node:
      self.print_inorder_traversal(node.left)
      print(node.data)
      self.print_inorder_traversal(node.right)
      

# Root
n1 = BinaryTreeNode(1)
# left child
n2 = BinaryTreeNode(2)
# right child 
n3 = BinaryTreeNode(3)
n1.left = n2
n1.right = n3


n1.data = 20
n2.data = 5
n3.data = 15

