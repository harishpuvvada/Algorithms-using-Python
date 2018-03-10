class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def detectLoop(self):
        current = self.head
        slow = fast = self.head
        while slow and fast and fast.next:

            if fast.next is None:
                return False

            if slow == fast.next or slow == fast.next.next:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        count = 0  #using count to prevent infinite loop
        while temp and count <10:
            print(temp.data,"-->",end = "")
            temp = temp.next
            count +=1
        print("null")


llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

#Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next



print("Linked List has cycle ? ",llist.detectLoop())
