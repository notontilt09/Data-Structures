class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # if value less than root put on left
    if value < self.value:
      # if nothing on left, set self.left to new BST
      if not self.left:
        self.left = BinarySearchTree(value)
      # else perform insert method on self.left
      else:
        self.left.insert(value)
    # if value greater than root put on right
    else:
      # if nothing on right set self.right to new BST
      if not self.right:
        self.right = BinarySearchTree(value)
      # else perform insert on node on right
      else:
        self.right.insert(value)


  def contains(self, target):
    # if self.value is target, we've found it
    if target == self.value:
      return True
    
    # if target higher than current node value
    elif target > self.value:
      # if node on right
      if self.right:
        # perform contains() method on right node
        return self.right.contains(target)
      # if nothing on right, target not in tree
      else:
        return False
    
    # if target lower than current node value
    elif target < self.value:
      # if node on left
      if self.left:
        # perform contains() method on left node
        return self.left.contains(target)
      # if nothing on left, target not in tree
      else:
        return False


  def get_max(self):
    # define current node
    current = self
    # if node on right
    while current.right:
      # set current to node on right
      current = current.right
    # escape while loop when we reach far right side of tree
    return current.value

  def for_each(self, cb):
    # if node is a leaf, perform cb on value
    if self.left == None and self.right == None:
      return cb(self.value)
    # if there's a left but no right, perform cb on value, and then for_each on node to left
    elif self.left and not self.right:
      cb(self.value)
      self.left.for_each(cb)
    # if there's a right but no left, perform cb on value, and then for_each on node to right
    elif self.right and not self.left:
      cb(self.value)
      self.right.for_each(cb)
    # if nodes to right and left, perform cb on value, and for_each on node to right and to left
    else:
      cb(self.value)
      self.right.for_each(cb)
      self.left.for_each(cb)