from tabnanny import check
from BinTree import BT

def check_bst(tree: BT) -> bool : #zkontroluje, jestli je tree BST. Kontrola probíha jak rekurzivně (kontroluje se každý substrom), tak lokálně (pokud je podmínka lokálně narušena, tak se hned vrátí False). Nejhorší možná časová komplexita je O(n), v případě, že je narušena lokální podmínka, tak O(h), kde h je hloubka poruchy.
    root=tree.root
    def _check_bst(node):
        if node is None:
            return True, float("inf"),float("-inf")
        if node.left and node.val<node.left.val or node.right and node.val>=node.right.val:
            return False,0,0
        lvalid,lmin,lmax=_check_bst(node.left)
        rvalid,rmin,rmax=_check_bst(node.right)
        if not (lvalid and rvalid):
            return False,0,0
        print(node.val,lmax,rmin)
        if lmax<node.val<rmin:
            return True,min(lmin,node.val),max(rmax,node.val)
        else:
            return False, 0,0
        lmin=min()
    return _check_bst(root)[0]

bt=BT(8,mode="balanced")
bt.multi_append(7,10,4)
print(check_bst(bt))