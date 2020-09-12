class BinaryTreeNode():
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  # Inorder: Left Subtree -> Root -> Right Subtree
  def print_inorder_traversal(self, node):
    if node:
      self.print_inorder_traversal(node.left)
      print(node.data)
      self.print_inorder_traversal(node.right)
  
  # Preorder: Root -> Left -> Right  
  def print_preorder_traversal(self, node):
    if node:
      print(node.data)
      self.print_preorder_traversal(node.left)
      self.print_preorder_traversal(node.right)

  # Postorder: Left -> Right -> Root
  def print_postorder_traversal(self, node):
    if node:
      self.print_postorder_traversal(node.left)
      self.print_postorder_traversal(node.right)
      print(node.data)


# Binary Tree : 
#
#            20  
#          /     \
#         5        15
#       /   \     /  \
#     10    12   14  18 
#    / \    /
#   30  7   3




def main():
  # Root
  n1 = BinaryTreeNode(1)

  n2 = BinaryTreeNode(2)
  n3 = BinaryTreeNode(3)
  n4 = BinaryTreeNode(4)
  n5 = BinaryTreeNode(5)
  n6 = BinaryTreeNode(6)
  n7 = BinaryTreeNode(7)
  n8 = BinaryTreeNode(8)
  n9 = BinaryTreeNode(9)
  n10 = BinaryTreeNode(10)

 
  n1.data = 20
  n2.data = 5
  n3.data = 15
  n4.data = 10
  n5.data = 12
  n6.data = 14
  n7.data = 18
  n8.data = 30
  n9.data = 7
  n10.data = 3


  n1.left = n2
  n1.right = n3
  n2.left = n4
  n2.right = n5
  n3.left = n6
  n3.right = n7
  n4.left = n8
  n4.right = n9
  n5.left = n10

  print("Inorder Traversal : " , "\n")   
  n1.print_inorder_traversal(n1)
  print()
  print("Preorder Traversal : ", "\n") 
  n1.print_preorder_traversal(n1)
  print()
  print("Postorder Traversal : ", "\n") 
  n1.print_postorder_traversal(n1)
  print()

if __name__== '__main__':
  main()
  




