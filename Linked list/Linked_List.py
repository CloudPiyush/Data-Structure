class Node:
    def __init__(self,data=None,next=None):
        
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.Head = None

    def ShowDetails(self):
        if self.Head == None:
            print('\nThe Linked List is Empty....!')
            return
        
        Itr = self.Head
        lstr = ''
        while Itr:
            lstr += str(Itr.data) + '--->' if Itr.next else str(Itr.data)
            Itr = Itr.next
        print(lstr)

    def Get_Length(self):
        count = 0
        Itr = self.Head
        while Itr:
            count += 1
            Itr = Itr.next
        
        return count

    def Insert_At_Beginning(self,data):

       node = Node(data,self.Head)
       self.Head = node

    def Insert_At_End(self,data):
        if self.Head == None:
            self.Head = Node(data)
            return
        
        Itr = self.Head
        while Itr.next:
            Itr = Itr.next
        Itr.next = Node(data)

    def Insert_Values(self,Index,data):
        if Index < 0 or Index > self.Get_Length():
            raise Exception('\nIndex is out of range.')
        
        if Index == 0:
            self.Insert_At_Beginning(data)
            return
        
        Count  = 0
        Itr = self.Head
        while Itr:
            if Count == Index - 1:
                node = Node(data,Itr.next)
                Itr.next = node
                break
            Itr = Itr.next
            Count = Count + 1

    def Remove(self,Index):
        if Index < 0 or Index > self.Get_Length():
            raise Exception('Index is out of range..!')
        
        if Index == 0 :
            self.Head = self.Head.next
            return
        
        Itr = self.Head
        Count = 0
        while Itr:
            if Count == Index -1 :
                Itr.next = Itr.next.next
                break
            Itr = Itr.next
            Count = Count + 1
    
    def remove_by_value(self,data):

        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
                
if __name__ == '__main__':
    Obj = LinkedList()

    Obj.Insert_At_Beginning(3)
    Obj.Insert_At_End(4)
    Obj.Insert_At_End(7)
    Obj.Insert_Values(1,32)
    Obj.Remove(3)
    Obj.ShowDetails()
    print('\nThe Length of list is :',Obj.Get_Length())
