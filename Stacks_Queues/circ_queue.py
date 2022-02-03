from collections import deque
class CircQueue:
    def __init__(self,size):
        self._size=size
        self.stored=0
        self._ar=[None]*size
        self.head=0
        self.tail=-1
        self.max_deque=deque()
    def enq(self,val):
        if self.stored==self._size:
            self.head=(self.head+(self._size-self.tail-1))%self._size
            self._size+=1
            self.stored+=1
            next=(self.tail+1)%self._size
            self._ar=self._ar[(self.tail+1)%self._size:]+self._ar[:next]+[val]
            self.tail=self._size-1
                
        else:
            next=(self.tail+1)%self._size
            self._ar[next]=val
            self.stored+=1
            self.tail=next

        
        while self.max_deque and self.max_deque[-1]<val:
            self.max_deque.pop()
            
        self.max_deque.append(val)

    def deq(self):
        val=self._ar[self.head]
        self._ar[self.head]=None
        self.head=(self.head+1)%self._size
        self.stored-=1
        if val==self.max_deque[0]:
            self.max_deque.popleft()

        return val
    def size(self):
        return self._size
    def max(self):
        return self.max_deque[0]
class ECircQueue(CircQueue):
    def multi_enq(self,*vals):
        for val in vals:
            self.enq(val)
    def multi_deq(self,num):
        for _ in range(num):
            self.deq()
    def print_all(self):
        if self.head<self.tail:
            print(", ".join(str(val) for val in self._ar[self.head:self.tail+1]))
        else:
            print(", ".join(str(val) for val in self._ar[self.head:]+self._ar[:self.tail+1]))
q=ECircQueue(5)
q.multi_enq(4,3,5)
q.print_all()
q.deq()
q.enq(6)
q.deq()
q.enq(7)
q.deq()
print(q._ar)
q.enq(8)
q.deq()
print(q._ar)
q.enq(2)
q.deq()
print(q._ar)
print("tail",q._ar[q.tail])
q.multi_enq(10,11,12)
q.print_all()
q.multi_deq(2)
q.print_all()
q.multi_enq(6,7,8)
q.print_all()
q.multi_deq(2)
q.multi_enq(21,22,23,24,25,26)
q.print_all()
print(q.size())
print(q.max())

w=ECircQueue(20)
w.multi_enq(20,14,18,16,12,15)
print(w.max())
w.deq()
print(w.max())
w.deq()
print(w.max())
w.deq()
print(w.max())
w.deq()
print(w.max())
w.deq()
print(w.max())
