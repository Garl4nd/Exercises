from tabnanny import check
from BinTree import BT

def check_balanced(bt):
    def _check_balanced(node):
        if node is None:
            return True,0
        else:
            left_bal,left_height=_check_balanced(node.left)
            if not left_bal:
                return False,-1
            right_bal,right_height=_check_balanced(node.right)
            return left_bal and right_bal and -1<=left_height-right_height<=1,max(left_height,right_height)+1
    return _check_balanced(bt.root)

def largest_complete(bt): #Write a program that returns the size of the largest subtree that is complete. 
    heights=[]
    def _check_balanced(node):
        if node is None:
            return True,0
        else:
            left_bal,left_height=_check_balanced(node.left)
            if not left_bal:
                return False,-1
            right_bal,right_height=_check_balanced(node.right)
            height=max(left_height,right_height)+1
            if left_bal and right_bal and -1<=left_height-right_height<=1:
                heights.append(height)
                return True,height
            else:
                return False,-1
    _check_balanced(bt.root)
    return max(heights)

def k_balance(bt,k): #Define a node in a binary tree to be k-balanced if the difference in the number of nodes in 
                     #its left and right subtrees is no more than k. Design an algorithm that takes as input a binary tree 
                    #and positive integer k, and returns a node in the binary tree such that the node is not k-balanced, 
                    #but all of its descendants are k-balanced. 
    heights=[]
    def _check_balanced(node):
        if node is None:
            return True,None,0
        else:
            left_bal,left_node,left_count=_check_balanced(node.left)
            if left_node is not None :
                return False,left_node,-1
            right_bal,right_node,right_count=_check_balanced(node.right)
            if right_node is not None :
                return False,right_node,-1

            count=left_count+right_count+1
            #print(node.val,count)

            if left_bal and right_bal:
                if -k<=left_count-right_count<=k:
                    return True,None,count
                else:
                    return False,node,count
            else:
                return False,None,count
            
    res=_check_balanced(bt.root)[1]
    if res is None:
        raise ValueError("No solution!")
    else:
        return res
    
    
bt=BT(49,mode="sorted")
bt.multi_append(20,10,14,25,27,55,50,57,49.9,57.8,5,6,1,7,8,9)
bt.sprint(xstep=25)
print(check_balanced(bt))
print(largest_complete(bt))
print(k_balance(bt,5).val)