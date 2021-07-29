class Node: 
    def __init__(self, val, next = None, random = None) -> None:
        self.val = val 
        self.next = next 
        self.random = random 

def copyRandomList(self, head: 'Node') -> 'Node':
    def copyNode(node, res): 
        if not node: return None 
        if node in res: return res[node] 
        copy = Node(node.val, None, None) 
        res[node] = copy 
        copy.next = copyNode(node.next, res)
        copy.random = copyNode(node.random, res)
        return copy

    return copyNode(head, {})