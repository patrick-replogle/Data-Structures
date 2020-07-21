Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list? O(1)

2. What is the runtime complexity of `push` using a linked list? O(n)

3. What is the runtime complexity of `pop` using a list? O(1)

4. What is the runtime complexity of `pop` using a linked list? O(n)

5. What is the runtime complexity of `len` using a list? O(1)

6. What is the runtime complexity of `len` using a linked list? O(n)

## Queue

1. What is the runtime complexity of `enqueue` using a list? O(n)

2. What is the runtime complexity of `enqueue` using a linked list? O(1)

3. What is the runtime complexity of `dequeue` using a list? O(n)

4. What is the runtime complexity of `dequeue` using a linked list? O(1)

5. What is the runtime complexity of `len` using a list? O(1)

6. What is the runtime complexity of `len` using a linked list? O(n)

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`? o(1)

2.  What is the runtime complexity of `ListNode.insert_before`? o(1)

3.  What is the runtime complexity of `ListNode.delete`? o(1)

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`? o(1)

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`? o(1)

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`? o(1)

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? o(1)

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    o(1) if you know the placement of the node, otherwise o(n) if you must search for the node first.

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    o(1) if you know the placement of the node, otherwise o(n) if you must search for node first.

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    o(1) if you know the placement of the node, otherwise o(n) if you must search for node first.

        a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

        DLL = o(1) if you know the placement of the node, otherwise o(n) if you must search for node first.
        Array.splice worst case will be o(n) since elements will need to be re-indexed.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

4. What is the runtime complexity of `for_each`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
