class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    # if value less than root put on left
    if value < self.value:
      # if nothing on left, set self.left to new BST
      if not self.left:
        self.left = new_node
      # else perform insert method on self.left
      else:
        self.left.insert(value)
    # if value greater than root put on right
    elif value > self.value:
      # if nothing on right set self.right to new BST
      if not self.right:
        self.right = new_node
      # else perform insert on node on right
      else:
        self.right.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False


  def get_max(self):
    current = self
    while current.right:
      current = current.right
    return current.value

  def for_each(self, cb):
    # if at a leaf, perform cb
    if self.left == None and self.right == None:
      return cb(self.value)
    
    # if there's a left but no right, perform cb on value, and then for_each on BST to left
    elif self.left and not self.right:
      cb(self.value)
      self.left.for_each(cb)
    elif self.right and not self.left:
      cb(self.value)
      self.right.for_each(cb)
    else:
      cb(self.value)
      self.right.for_each(cb)
      self.left.for_each(cb)