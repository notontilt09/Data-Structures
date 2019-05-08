class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    # a hash table for our key:value pairs
    self.lookup = {}
    # a hash table for our keys and when they were used
    self.when_used = {}
    # a number to keep track of when a key was used
    self.num = 0
    

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # if key exits
    if key in self.lookup:
      # update priority on key
      self.when_used[key] = self.num
      # increase priority counter
      self.num += 1
      return self.lookup[key]
    # if key isn't in lookup table return none
    else:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # if no room in the lookup and key doesn't already exist
    if len(self.lookup) >= self.limit and key not in self.lookup.keys():
      # find smallest number in when used and delete key from both dicts
      oldest_value = min(self.when_used.values())
      oldest_key = None
      for i in self.when_used:
        if self.when_used[i] == oldest_value:
          oldest_key = i
      self.lookup.pop(oldest_key)
      self.when_used.pop(oldest_key)
    # add new item or overwrite item in lookup and when_used, increase the priority counter
    self.lookup[key] = value
    self.when_used[key] = self.num
    self.num += 1
