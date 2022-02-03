from BinTree import BT,Node

class Heap(BT):
    
    def __init__(self,val,minmax="max"):
        super().__init__(mode="balanced",val=val)
        self.minmax=minmax
        self.mmsign=1 if minmax=="max" else -1
        self.ln=self.root

    def append(self,val):
        if self.num==2*self.lowest-1:
            self.lowest=1
            self.height+=1
        else:
            self.lowest+=1
            
            #print(self.lowest)
        path=[int(b) for b in str(bin(self.lowest-1))[2:]]
        path=[0]*(self.height-len(path))+path
            #print(f"{path=}",self.lowest)
        node=self.get(path[:-1])
        if node is None:
            self.__init__(val,minmax=self.minmax)
            return
        new_child=Node(val=val)
        #print("appending to parrent with val:",node.val)
        node.append(new_child,lr=path[-1])
        self.ln=new_child
        self.num+=1
        node=new_child
        while node is not self.root and node.val*self.mmsign>=node.parent.val*self.mmsign:
            node.val,node.parent.val=node.parent.val,node.val
            node=node.parent
    
    def find(self,val,stnode=None):
        if stnode is None:
            stnode=self.root
        def _find(node):
            if node is None:
                return None
            if node.val==val:
                return node
            res=None
            if node.left and node.left.val*self.mmsign>=val*self.mmsign:
                res=self.find(val,stnode=node.left)
            if res is None:
                if node.right and node.right.val*self.mmsign>=val*self.mmsign:
                    res=self.find(val,stnode=node.right)
            return res
        return _find(stnode)

    def remove(self,val):
        node=self.find(val)
        if node is None:
            raise ValueError("The heap doesn't contain this value!")
        if self.ln.parent and self.ln==self.ln.parent.right:
            self.ln=self.ln.parent.left
        else:
            path=[int(b) for b in str(bin(self.lowest-1))[2:]]
            path=[0]*(self.height-len(path))+path
            self.ln=self.get(path)
        
        lnval=self.ln.val
        if self.ln.parent:
            if self.ln.parent.right:
                self.ln.parent.right=None
            else:
                self.ln.parent.left=None

        
        if self.lowest>1:
            self.lowest-=1
        else:
            self.height-=1
            self.lowest=2**self.height #(1<<self.height)
        if node is not None:
            node.val=lnval
            while node.left is not None:
                if node.val*self.mmsign<node.left.val*self.mmsign:
                    if node.right and node.val*self.mmsign<node.right.val*self.mmsign:
                        if node.left.val*self.mmsign>node.right.val*self.mmsign:
                            node.val,node.left.val=node.left.val,node.val
                            node=node.left
                        else:
                            node.val,node.right.val=node.right.val,node.val
                            node=node.right
                    else:
                        node.val,node.left.val=node.left.val,node.val
                        node=node.left
                elif node.right and node.val*self.mmsign<node.right.val*self.mmsign:
                    node.val,node.right.val=node.right.val,node.val
                    node=node.right
                else:
                    break
                
    def pop(self):
        if self.height==0:
            rval=self.root.val
            self.root=None
            return rval
        node=self.root
        rootval=node.val
        if self.ln.parent and self.ln==self.ln.parent.right:
            self.ln=self.ln.parent.left
        else:
            path=[int(b) for b in str(bin(self.lowest-1))[2:]]
            path=[0]*(self.height-len(path))+path
            self.ln=self.get(path)
        
        lnval=self.ln.val
        if self.ln.parent:
            if self.ln.parent.right:
                self.ln.parent.right=None
            else:
                self.ln.parent.left=None
        if self.lowest>1:
            self.lowest-=1
        else:
            self.height-=1
            self.lowest=2**self.height #(1<<self.height)
        if node is not None:
            node.val=lnval
            while node.left is not None:
                if node.val*self.mmsign<node.left.val*self.mmsign:
                    if node.right and node.val*self.mmsign<node.right.val*self.mmsign:
                        if node.left.val*self.mmsign>node.right.val*self.mmsign:
                            node.val,node.left.val=node.left.val,node.val
                            node=node.left
                        else:
                            node.val,node.right.val=node.right.val,node.val
                            node=node.right
                    else:
                        node.val,node.left.val=node.left.val,node.val
                        node=node.left
                elif node.right and node.val*self.mmsign<node.right.val*self.mmsign:
                    node.val,node.right.val=node.right.val,node.val
                    node=node.right
                else:
                    break

        return rootval
    @staticmethod
    def CreateBinHeap(valar):
        heap=Heap(None)
        heap.pop()
        heap.multi_append(*valar)
        return heap

exit()
h=Heap.CreateBinHeap([1,2,5,20])
h.multi_append(1,7,8)
h.sprint(xstep=10)
h.multi_append(24,5,11,13,19,25)
h.sprint(xstep=10)
n=h.find(14)
print(n)
h.remove(24)
h.sprint(xstep=10)
h.remove(25)
h.sprint(xstep=10)
h.pop()
h.pop()
h.sprint(xstep=10)