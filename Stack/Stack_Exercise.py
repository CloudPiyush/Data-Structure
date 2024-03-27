from collections import deque

class Stack:

    def __init__(self) -> None:
        self.contanier = deque()

    def Push(self,val):
        self.contanier.append(val)
    
    def Show(self):
        return self.contanier
    
    def Pop(self):
        return self.contanier.pop()
    
    def Size(self):
        return len(self.contanier)
    
# def Reverse_String(String):

#     stack = Stack()

#     for Ch in String:
#         stack.Push(Ch)
    
#     rstr = ''
#     while stack.Size() != 0 :
#         rstr += stack.Pop()

#     return rstr



# if __name__ == '__main__':

#     print(Reverse_String("Piyush Patil"))

def is_Match(Ch1,Ch2):

    Match_Dict = {
        ']' : '[',
        ')' : '(',
        '}' : '{'
    }

    return Match_Dict[Ch1] == Ch2

def is_Balanced(string):

    stack = Stack()

    for Chr in string:
        if Chr == '(' or Chr == '[' or Chr == '{':
            stack.Push(Chr)

        if Chr == ')' or Chr == ']' or Chr == '}':
            if stack.Size() == 0:
                return False
            
            if not is_Match(Chr,stack.Pop()):
                return False
    
    return stack.Size() == 0

if __name__ == "__main__":

    print(is_Balanced("({a+b})"))
    print(is_Balanced("))((a+b}{"))
    print(is_Balanced("((a+b))"))
    print(is_Balanced("((a+g))"))
    print(is_Balanced("))"))
    print(is_Balanced("[a+b]*(x+2y)*{gg+kk}"))