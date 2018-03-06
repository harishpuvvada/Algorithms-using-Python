class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,new):#push is inserting in place of head
        temp = Node(new)
        if self.head is None:
            self.head = temp
        else:
            self.head,self.head.next = temp,self.head

    def PrintKthElement(self,K):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        while(count < K):
            if(ref_ptr is None):
                    print("%d is greater than the no. of nodes in list" %(K))
                    return
            ref_ptr = ref_ptr.next
            count+=1

        while(ref_ptr is not None):
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next
        print("Kth element from last in list is ",(main_ptr.data))


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)

llist.PrintKthElement(4)
