# """Queue Using the List."""

# Stock_Price_Queue = []

# Stock_Price_Queue.insert(0,123)
# Stock_Price_Queue.insert(0,189)
# Stock_Price_Queue.insert(0,213)
# Stock_Price_Queue.insert(0,332)
# Stock_Price_Queue.insert(0,434)
# Stock_Price_Queue.insert(0,536)

# print(Stock_Price_Queue)
# print(Stock_Price_Queue.pop())
# print(Stock_Price_Queue)
# print(Stock_Price_Queue.pop())
# print(Stock_Price_Queue)

"""Queue Using the deque"""

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.Buffer = deque()

    def Feed_Data(self,val):
        self.Buffer.appendleft(val)

    def Pop(self):
        return self.Buffer.pop()

    def Size(self):
        return len(self.Buffer)
    
    def Is_Empty(self):
        return len(self.Buffer) == 0
    
    def Show(self):
        return(self.Buffer)

if __name__ == '__main__':

    Obj = Queue()
    Obj.Feed_Data({
            'Company': 'Tata Moters',
            'Time Stamp':'16 March , 9:15 AM ',
            'Price':'21240'
    })
    Obj.Feed_Data({
        'Company': 'Tata Moters',
        'Time Stamp':'16 March ,9:20 AM ',
        'Price':'21270'
    }) 
    Obj.Feed_Data({
        'Company': 'Tata Moters',
        'Time Stamp':'16 March , 9:25 AM',
        'Price':'21300'
    }) 
    Obj.Feed_Data({
        'Company': 'Tata Moters',
        'Time Stamp':'16 March , 9:30 AM ',
        'Price':'21330'
    }) 
    Obj.Feed_Data({
        'Company': 'Tata Moters',
        'Time Stamp':'16 March ,9:40 ',
        'Price':'21360'
    })  
    print(Obj.Show())
    print(Obj.Pop())
    print(Obj.Pop())
    print(Obj.Pop())
    print(Obj.Show())