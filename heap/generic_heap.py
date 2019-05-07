class Heap:
  def __init__(self, comparator=lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator

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
      # then sift down new first element to correct spot
      self._sift_down(0)
    
    return deleted

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    if index <= 0:
      return
    elif self.comparator(self.storage[index], self.storage[parent]):
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      self._bubble_up(parent)

  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    max = index
    if len(self.storage) > left and self.comparator(self.storage[left], self.storage[max]):
      max = left
    if len(self.storage) > right and self.comparator(self.storage[right], self.storage[max]):
      max = right
    if max == index:
      return
    else:
      self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
      self._sift_down(max)
