class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # add value to end of storage
    self.storage.append(value)
    # grab index of end
    index = len(self.storage) - 1
    # bubble up value to correct position
    self._bubble_up(index)

  def delete(self):
    # edge cases
    if len(self.storage) == 0:
      return None
    
    # return value
    deleted = self.storage[0]

    if len(self.storage) == 1:
      self.storage.pop()
    else:
      # swap max with last element, then remove it
      self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
      self.storage.pop()


      # implementation without _sift_down helper below

      # i = 0
      # left = 2*i + 1
      # right = 2*i + 2
      # while len(self.storage) > right:
      #   if self.storage[left] >= self.storage[right]:
      #     self.storage[i], self.storage[left] = self.storage[left], self.storage[i]
      #     i = left
      #     left = 2*i + 1
      #     right = 2*i + 2
      #   else:
      #     self.storage[i], self.storage[right] = self.storage[right], self.storage[i]
      #     i = right
      #     left = 2*i + 1
      #     right = 2*i + 2
      
      # then sift down new first element to correct spot
      self._sift_down(0)
    
    return deleted


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    if index <= 0:
      return
    elif self.storage[parent] < self.storage[index]:
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      self._bubble_up(parent)

  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    max = index
    if len(self.storage) > left and self.storage[max] < self.storage[left]:
      max = left
    if len(self.storage) > right and self.storage[max] < self.storage[right]:
      max = right
    if max == index:
      return
    else:
      self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
      self._sift_down(max)
    
    
    

