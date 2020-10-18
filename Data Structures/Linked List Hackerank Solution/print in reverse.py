"""
Hackerrank solution in python for print in reverse
"""
def reversePrint(head):
    if head is None:
        return
    if head.next is not None:
        reversePrint(head.next)
    print(head.data)
