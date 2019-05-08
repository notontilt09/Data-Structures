Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(n)

2. What is the runtime complexity of `dequeue`?
O(1)

3. What is the runtime complexity of `len`?
O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(n)

2. What is the runtime complexity of `contains`?
Average runtime probably O(log n)
Worst case O(n) if entire tree is one branch and target is the leaf.

3. What is the runtime complexity of `get_max`? 
if H is the height of the tree, runtime will be O(H)

## Heap

1. What is the runtime complexity of `_bubble_up`?
Worst case O(log n) if it has to climb to the top of the tree

2. What is the runtime complexity of `_sift_down`?
Worst case O(log n) if it has to sift to the bottom of the tree

3. What is the runtime complexity of `insert`?
O(log n) since it calls _bubble_up

4. What is the runtime complexity of `delete`?
O(log n) since it calls _sift_down

5. What is the runtime complexity of `get_max`?
O(1) simply grabs root value

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
O(1)

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Linked list is 0(1), Array.splice worst case is 0(n) if we are deleting the first element.  It seems linked list delete() is much faster on average.