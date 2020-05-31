# Print "Hello, world!" to your terminal
# print('Hello World!  Wooo')

new_tuple = tuple('new tuple wut')
# print(new_tuple)
# print(new_tuple[2])

arr = ['a', 'b', 'c', 'd', 'e', 'a', 'a']
arr.remove('a')
# print(arr)

car = {
  "brand": "Honda",
  "model": "CR-V",
  "year": 2002
}
x = car.pop("model")
# print(x)
# print(car)

signs = {'alpha', 'beta', 'gamma', 'omega'}
# print(signs.pop())
# print(signs)

# class Point :
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# point = Point(1,2)
# print(point)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
      # return 'Point(x=%s, y=%s)' % (self.x, self.y)
      return f'Point(x={point.x}, y={point.y})'

point = Point(1,2)
# print(point)

# print(dir(__builtins__))

# ------ code from lecture on linked lists from Sean Chen ------

# class Node:
#   def __init__(self, value=None, next_node=None):
#     # the value at this linked list node
#     self.value = value
#     # reference to the next node in the list
#     self.next_node = next_node
# ​
#   def get_value(self):
#     return self.value
# ​
#   def get_next(self):
#     return self.next_node
# ​
#   def set_next(self, new_next):
#     # set this node's next_node reference to the passed in node
#     self.next_node = new_next
# ​
# class LinkedList:
#     def __init__(self):
#         # first node in the list 
#         self.head = None
# ​
#     def add_to_end(self, value):
#         # regardless of if the list is empty or not, we need to wrap the value in a Node 
#         new_node = Node(value)
#         # what if the list is empty? 
#         if not self.head:
#             self.head = new_node
#         # what if the list isn't empty?
#         else:
#             # what node do we want to add the new node to? 
#             # the last node in the list 
#             # we can get to the last node in the list by traversing it 
#             current = self.head 
#             while current.get_next() is not None:
#                 current = current.get_next()
#             # we're at the end of the linked list 
#             current.set_next(new_node)
# ​
#     def remove_from_head(self):
#         # what if the list is empty?
#         if not self.head:
#             return None
#         # what if it isn't empty?
#         else:
#             # we want to return the value at the current head 
#             value = self.head.get_value()
#             # remove the value at the head 
#             # update self.head 
#             self.head = self.head.get_next()
#             return value

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  # initialize head
  def __init__(self):
    self.head = None

  # reverse the list
  def reverse_list(self):
    prev = None
    current = self.head
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def push(self, value): 
    new_node = Node(value) 
    new_node.next = self.head 
    self.head = new_node 

  def print_list(self):
    temp = self.head
    while(temp):
      print(temp.value)
      temp = temp.next

# test the linked list by initializing, printing, reversing, then printing again
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List")
llist.print_list() 
llist.reverse_list() 
print("\nReversed Linked List")
llist.print_list() 
