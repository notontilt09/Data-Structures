"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head == None:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
      self.length += 1
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    deleted = self.head.value
    if self.head == None:
      pass
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      self.head.delete()
      self.head = self.head.next
      self.length -= 1
    return deleted

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if self.tail == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

    self.length += 1
      

  def remove_from_tail(self):
    if self.tail:
      deleted = self.tail.value

    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      self.tail.delete()
      self.tail = self.tail.prev
      self.length -= 1

    return deleted
    
  def move_to_front(self, node):
    self.add_to_head(node.value)
    if self.tail == node:
      self.tail = self.tail.prev
    node.delete()
    self.length -= 1

  def move_to_end(self, node):
    self.add_to_tail(node.value)
    if self.head == node:
        self.head = self.head.next
    node.delete()
    self.length -= 1

  def delete(self, node):
    if self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1

    
  def get_max(self):
    current_node = self.head
    max = self.head.value
    while current_node:
      if current_node.value > max:
        max = current_node.value
      current_node = current_node.next
    return max
