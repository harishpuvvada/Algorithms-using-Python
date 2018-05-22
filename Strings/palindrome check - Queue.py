from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch) #at the back

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


def palindrome(string):
    if string == string[::-1]:
        return True
    return False

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))