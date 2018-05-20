'''
Note:
stack - reverses the order of input elements while output
Queue - prints in same order. So,

We use in_stack to fill in with elements and then pop them in to out_stack.Then we have in the given order of elements. So now we can return the poped element from out_stack
'''


class Queue2Stacks(object):

    def __init__(self):
        
        self.in_stack = []          # Two Stacks
        self.out_stack = []


    def enqueue(self, element):
        self.in_stack.append(element)


    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print (q.dequeue())

#output will be 0,1,2,3,4
