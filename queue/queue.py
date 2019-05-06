class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements? How bout a list?
    self.storage = []

  def enqueue(self, item):
    # use list insert to put item at index 0
    self.storage.insert(0, item)
    # increase size of Queue
    self.size += 1
  
  def dequeue(self):
    # if nothing in Queue return NOne
    if self.size == 0:
      return None
    # if something in Queue, reduce size by 1 and return the last value
    else:
      self.size -= 1
      return self.storage.pop()

  def len(self):
    return self.size
