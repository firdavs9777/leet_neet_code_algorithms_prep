class Node:
  def __init__(self,data):
    self.data = data # Store the value 
    self.next = None #Pinter to the next node

# from the head until tail

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1


my_linked_list = LinkedList(4)

print(my_linked_list.head.data)