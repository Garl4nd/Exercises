from sre_constants import SUCCESS
from BinTree import BT

def traverse(order,root,rev=False):
            if root is None:
                return
            left=root.left if not rev else root.right
            right=root.right if not rev else root.left
            if order=="inorder":
                yield from traverse(order,left)
                yield root
                yield from traverse(order,right)
            elif order=="preorder":
                yield root
                yield from traverse(order,left)
                yield from traverse(order,right)
            elif order=="postorder":
                yield from traverse(order,left)
                yield from traverse(order,right)
                yield root


def successor(node):
    
    if node.right is not None:
            return next(iter(traverse("inorder",node.right)))
    else:
        while node.parent and node!=node.parent.left:
            node=node.parent
        return node.parent

def test_suc(bt):
    node=next(iter(traverse("inorder",bt.root)))
    while node is not None:
        #print(node)
        print(node.val)
        node=successor(node)

bt=BT(30)

bt.multi_append(20,19,18,17,16,15,35,34,32,31,37,38,39,38.4,40,39.5)
bt.print_all()
bt.sprint(xstep=20)
test_suc(bt)

    