class Queue:
    def __init__(self):
        self._enq,self._deq=[],[]

    def enq(self,val):
        self._enq.append(val)
    def multi_enq(self,*vals):
        for val in vals:
            self.enq(val)
    def deq(self):
        if self._deq:
            return self._deq.pop()
        else:
            while self._enq:
                self._deq.append(self._enq.pop())
            
            if not self._deq:
                raise IndexError("The queue is empty!")
            return self._deq.pop()
    def multi_deq(self,num):
        for _ in range(num):
            self.deq()
q=Queue()
q.multi_enq(1,2,3,4,5,6)
for _ in range(6):
    print(q.deq())