# from typing import List


# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
  
#   # Function to print the list
#   def printList(self):
#     node = self
#     output = '' 
#     while node != None:
#       output += str(node.val)
#       output += " "
#       node = node.next
#     print(output)

#   # Iterative Solution
#   def reverseIteratively(self, head):
#     # Implement this.
#     values = []
#     tail = ListNode(None)
    
#     while head != None:
#         if head.next is None:
#             tail = head

#         values.append(head.val)
#         temp = head.next
#         head = None
#         head = temp

    
    
#     for idx, v in enumerate(values):
#         if tail is None:
#             tail = ListNode(v)
#         else:
#             new_node = ListNode(v)
#             new_node.next = tail
#             tail = new_node

# #   # Recursive Solution      
# #   def reverseRecursively(self, head):
# #     # Implement this.


# # Test Program
# # Initialize the test list: 
# testHead = ListNode(4)
# node1 = ListNode(3)
# testHead.next = node1
# node2 = ListNode(2)
# node1.next = node2
# node3 = ListNode(1)
# node2.next = node3
# testTail = ListNode(0)
# node3.next = testTail

# print("Initial list: ")
# testHead.printList()
# # 4 3 2 1 0
# testHead.reverseIteratively(testHead)
# #testHead.reverseRecursively(testHead)
# print("List after reversal: ")
# testTail.printList()
# # 0 1 2 3 4


from typing import List


class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    # Implement this.
    curr = head
    prev = None

    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

#   # Recursive Solution      
  def reverseRecursively(self, prev, head):
    # Implement this.
    if head is None:
        return
    else:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        self.reverseRecursively(prev, head)




# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")  
testHead.printList()
# 4 3 2 1 0
# testHead.reverseIteratively(testHead)
testHead.reverseRecursively(None,testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4