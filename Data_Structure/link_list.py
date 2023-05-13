class Node:
    def __init__(self , value):
        self.next = None
        self.prev = None
        self.val = value



class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def add(self, val):
        node = Node(val)
        if self.tail is None :
            self.head = node
            self.tail = node
            self.size += 1
        else :
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"         


number_list = DoubleLinkedList()
number_list.add(1)
number_list.add(5)
number_list.add(9)
number_list.add(6)
print(number_list)
