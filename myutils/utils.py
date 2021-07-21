class ListNode: 
    def __init__(self, x):
        self.val = x 
        self.next = None


def stringToIntergerList(inputString: str) -> list: 
    # Translate input string to interger list split by ','
    return list(map(int, inputString.split(',')))

def stringToListNode(inputString: str) -> ListNode: 
    # Generate list from the input
    numbers = stringToIntergerList(inputString) 

    root = ListNode(-1) 
    ptr = root 
    for number in numbers: 
        ptr.next = ListNode(number) 
        ptr = ptr.next 

    ptr = root.next
    return ptr 

def listNodeToString(node: ListNode) -> str: 
    # Return string from ListNode
    if not node: 
        return None 
    
    result = "" 
    while node: 
        result += str(node.val) + ', '
        node = node.next 

    return '[' + result[:-2] + ']'
    