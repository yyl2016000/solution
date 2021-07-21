import sys 
sys.path.append("..")

from myutils.utils import * 

def mySolution(headA: ListNode, headB: ListNode) -> ListNode: 
    a_dict = {}
    while headA != None: 
        a_dict[headA] = 1 
        headA = headA.next 
    print(a_dict)
    while headB != None: 
        if headB in a_dict: 
            return headB
        headB = headB.next 
    return None 

def solution(headA: ListNode, headB: ListNode) -> ListNode:
    h1 = headA 
    h2 = headB 

    while(h1 != h2): 
        h1 = headB if not h1 else h1.next 
        h2 = headA if not h2 else h2.next 
    return h1 

# def main(): 
#     listNodeA = stringToListNode(input()) 
#     listNodeB = stringToListNode(input())
#     out_node = mySolution(listNodeA, listNodeB)
#     print(out_node.val)

# if __name__ == '__main__': 
#     main() 