class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    if len(self.storage) == 0:
      self.storage.append(value)
    else:
      self.storage.append(value)
      index = len(self.storage) - 1
      parent = (index - 1) // 2
      while value > self.storage[parent] and parent >= 0:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        index = parent
        parent = (parent - 1) // 2

  def delete(self):
    # edge cases
    if len(self.storage) == 0:
      return None
    
    deleted = self.storage[0]

    if len(self.storage) == 1:
      self.storage.pop()
    else:
      # swap max with last element, then remove it
      self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
      self.storage.pop()
      # then bubble down new first element to correct spot
      i = 0
      left = 2*i + 1
      right = 2*i + 2
      while len(self.storage) > right:
        if self.storage[left] >= self.storage[right]:
          self.storage[i], self.storage[left] = self.storage[left], self.storage[i]
          i = left
          left = 2*i + 1
          right = 2*i + 2
        else:
          self.storage[i], self.storage[right] = self.storage[right], self.storage[i]
          i = right
          left = 2*i + 1
          right = 2*i + 2
    
    return deleted


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
