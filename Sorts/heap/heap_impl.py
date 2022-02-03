from .BinTree import BT,Node

class Heap(BT):
    
    def __init__(self,val,key=None):
        super().__init__(mode="balanced",val=val)
        if val is None:
            self.pop()
        self.ln=self.root
        if key is None:
            self.key= lambda x:x
        else:
            self.key=key

    def append(self,val):

        if self.num==2*self.lowest-1:
            self.lowest=1
            self.height+=1
        else:
            self.lowest+=1
            
        path=[int(b) for b in str(bin(self.lowest-1))[2:]]
        path=[0]*(self.height-len(path))+path
        node=self.get(path[:-1])
        if node is None:
            self.__init__(val,key=self.key)
            return
        new_child=Node(val=val)
        #print("appending to parrent with val:",node.val)
        node.append(new_child,lr=path[-1])
        self.ln=new_child
        self.num+=1
        node=new_child
        while node is not self.root and self.key(node.val)>=self.key(node.parent.val):
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
            if node.left and self.key(node.left.val)>=self.key(val):
                res=self.find(val,stnode=node.left)
            if res is None:
                if node.right and self.key(node.right.val)>=self.key(val):
                    res=self.find(val,stnode=node.right)
            return res
        return _find(stnode)

    def remove(self,val):
        node=self.find(val)
        if node is None:
            raise ValueError("The heap doesn't contain this value!")
        lnval=self.ln.val
        if self.ln.parent and self.ln==self.ln.parent.right:
            self.ln=self.ln.parent.left
        else:
            path=[int(b) for b in str(bin(self.lowest-1))[2:]]
            path=[0]*(self.height-len(path))+path
            self.ln=self.get(path)
        
        
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
                if self.key(node.val)<self.key(node.left.val):
                    if node.right and self.key(node.val)<self.key(node.right.val):
                        if self.key(node.left.val)>self.key(node.right.val):
                            node.val,node.left.val=node.left.val,node.val
                            node=node.left
                        else:
                            node.val,node.right.val=node.right.val,node.val
                            node=node.right
                    else:
                        node.val,node.left.val=node.left.val,node.val
                        node=node.left
                elif node.right and self.key(node.val)<self.key(node.right.val):
                    node.val,node.right.val=node.right.val,node.val
                    node=node.right
                else:
                    break
        self.num-=1

    def pop(self):
        if self.height==0:
            rval=self.root.val
            self.root=None
            self.num-=1
            return rval
        node=self.root
        rootval=node.val

        parent=self.ln.parent
        lnval=self.ln.val
        
        
        if self.lowest>1:
            self.lowest-=1
        else:
            self.height-=1
            self.lowest=2**self.height #(1<<self.height)

        
        if self.ln==parent.right:
            self.ln=self.ln.parent.left
        else:
            path=[int(b) for b in str(bin(self.lowest-1))[2:]]
            path=[0]*(self.height-len(path))+path
            self.ln=self.get(path)
            print(path)
        #print(lnval,(self.height,self.lowest),self.ln.val)
        if parent.right:
            parent.right=None
        else:
            parent.left=None
        
        
        
        
       
        
        node.val=lnval
        while node.left is not None:
            if self.key(node.val)<self.key(node.left.val):
                if node.right and self.key(node.val)<self.key(node.right.val):
                    if self.key(node.left.val)>self.key(node.right.val):
                        node.val,node.left.val=node.left.val,node.val
                        node=node.left
                    else:
                        node.val,node.right.val=node.right.val,node.val
                        node=node.right
                else:
                    node.val,node.left.val=node.left.val,node.val
                    node=node.left
            elif node.right and self.key(node.val)<self.key(node.right.val):
                node.val,node.right.val=node.right.val,node.val
                node=node.right
            else:
                break
        self.num-=1
        return rootval

    @staticmethod
    def CreateBinHeap(valar,key=None):
        heap=Heap(None,key=key)
        heap.multi_append(*valar)
        return heap

ar=[2,1,0,8,9,5]
heap=Heap.CreateBinHeap(ar,key=lambda x:-x)

while heap:
    heap.sprint()
    print(heap.pop(),heap.num)
    

