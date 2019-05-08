"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0

  # adding is_leaf method for display to work
  def is_leaf(self):
    if self.node.left or self.node.right:
      return False
    return True

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
      if self.node.left != None: 
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    # for each case we'll just add 1 to height of the largest subtree
    # can find the height of subtrees recursively
    if self.node.left and self.node.right:
      self.height = 1 + max(self.node.left.update_height(), self.node.right.update_height())
    elif self.node.left:
      self.height = 1 + self.node.left.update_height()
    elif self.node.right:
      self.height = 1 + self.node.right.update_height()
    else:
      self.height = 0
    return self.height


  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    # if node has two children, balance is left.height - right.height
    # then need to update balance on both child nodes
    if self.node.left and self.node.right:
      self.balance = self.node.left.height - self.node.right.height
      self.node.left.update_balance()
      self.node.right.update_balance()
    # if only left node, take height of left and subtract -1 which is height of non-existant right tree
    elif self.node.left:
      self.balance = self.node.left.height - (-1)
      self.node.left.update_balance()
    # if only right node, subtrace height of right from -1 which is height of non-existatnt left tree
    elif self.node.right:
      self.balance = -1 - self.node.right.height
      self.node.right.update_balance()
    # if no children, balance is 0
    else:
      self.balance = 0

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def _left_rotate(self):
    # setting up temp variables for swap
    top = self.node
    R = self.node.right.node
    left_child_of_R = R.left.node
    # swapping
    self.node = R
    self.node.left.node = top
    self.node.left.node.right.node = left_child_of_R

  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def _right_rotate(self):
    # setting up temp variables fro swap
    top = self.node
    L = self.node.left.node
    right_child_of_L = L.right.node
    # swapping
    self.node = L
    self.node.right.node = top
    self.node.right.node.left.node = right_child_of_L

  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  # CASES FOR REBALANCING
  # 1.  Left/Left: Just RIGHT rotate 
  # 2.  Left/Right: Rotate subtree LEFT then main tree RIGHT
  # 3.  Right/Left: Rotate subtree RIGHT then main tree LEFT
  # 3.  Right/Right: Just LEFT rotate until we're balanced
  def rebalance(self):
    # update height and balance to check if we need balancing
    self.update_height()
    self.update_balance()
    # while we're unbalanced
    while self.balance < -1 or self.balance > 1:
      # Left side too large
      if self.balance > 1:
        # Case 2 first part
        if self.node.left.balance < 0:
          self.node.left._left_rotate()
          self.update_height()
          self.update_balance()
        # Case 1 and 2nd half of case 2
        self._right_rotate()
        self.update_height()
        self.update_balance()
      
      # Right side too large
      if self.balance < -1:
        # Case 3 first part
        if self.node.right.balance > 0:
          self.node.right._right_rotate()
          self.update_height()
          self.update_balance()
        # Case 4 and 2nd half of case 3
        self._left_rotate()
        self.update_height()
        self.update_balance()

        
  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    new_node = AVLTree(Node(key))
    if self.node == None:
      self.node = Node(key)
    # if value less than root put on left
    elif key < self.node.key:
      # if nothing on left, set self.left to new AVL Tree
      if not self.node.left:
        self.node.left = new_node
      # else perform insert method on self.left
      else:
        self.node.left.insert(key)
    # if value greater than root put on right
    elif key > self.node.key:
      # if nothing on right set self.right to new AVLTree
      if not self.node.right:
        self.node.right = new_node
      # else perform insert on node on right
      else:
        self.node.right.insert(key)
    
    
    # rebalance after insertion
    self.rebalance()


## can't get final test to pass, I think because my update_balace() method is not recursive.  Going to move on to LRU instead of trying to debug this any more
