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
    # if nothing at head set head and tail to new node
    if self.head == None:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
      self.length += 1
    # insert new node before current head, update self.head pointer
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    # keep track of return value
    deleted = self.head.value
    # if no head return none
    if self.head == None:
      return None
    # if list only has only one node set head and tail to none
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    # else delete head and update self.head pointer
    else:
      self.head.delete()
      self.head = self.head.next
      self.length -= 1
    return deleted

  def add_to_tail(self, value):
    # new node to be added
    new_node = ListNode(value)
    # if list is empty, head and tail will point to new_node
    if self.tail == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    # else, insert at end and update self.tail pointer
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

    self.length += 1
      

  def remove_from_tail(self):
    # returning deleted value, get reference to it if it exists
    if self.tail:
      deleted = self.tail.value

    # if list is just 1 node, set head and tail to None
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    # if list is multiple nodes, delete tail and update self.tail pointer
    else:
      self.tail.delete()
      self.tail = self.tail.prev
      self.length -= 1

    return deleted
    
  def move_to_front(self, node):
    # add node to head
    self.add_to_head(node.value)
    # if we moved the tail, updated self.tail pointer
    if self.tail == node:
      self.tail = self.tail.prev
    # delete the node that we moved
    node.delete()
    self.length -= 1

  def move_to_end(self, node):
    # add node to the end
    self.add_to_tail(node.value)
    # if we moved the head, updated self.head pointer
    if self.head == node:
        self.head = self.head.next
    # delete the node that we moved
    node.delete()
    self.length -= 1

  def delete(self, node):
    # if trying to delete head, use remove_from_head
    if self.head == node:
      self.remove_from_head()
    # if trying to delete tail, use remove_from_tail
    elif self.tail == node:
      self.remove_from_tail()
    # otherwise just delete the node
    else:
      node.delete()
      self.length -= 1

    
  def get_max(self):
    # keep track of current_node to iterate through list
    current_node = self.head
    # update max with the max value we see as we move through the list
    max = self.head.value
    while current_node:
      if current_node.value > max:
        max = current_node.value
      current_node = current_node.next
    return max
