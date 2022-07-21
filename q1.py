operator =['+', '-', '*', '/', '(', ')', '^'] 
priority = {'+':1, '-':1, '*':2, '/':2, '^':3}  
 
def infixToPostfix(exp):
    stack = [] 
    post = ''    
    for c in exp:
        if c not in operator: 
            post+= c
        elif c=='(':  
            stack.append('(')
        elif c==')':
            while stack and stack[-1]!= '(':
                post+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[c]<=priority[stack[-1]]:
                post+=stack.pop()
            stack.append(c)            
    while stack: 
        print(stack)            
        post+=stack.pop()           
    return post
class postfix:
    def __init__(self):
        self.items=[]
          
    def push(self,item):
        self.items.append(item)            
    def pop(self):          
        return self.items.pop()
    def evalute(self,exp):
        for c in exp:
            if c in '0123456789':
                self.push(c)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op2,op1,c)
                self.push(result)
        return self.pop()
    def cal(self,op2,op1,c):
        if (c == '^'):
            return int(op2)**int(op1)
        elif (c =='*'):
            return int(op2)*int(op1)
        elif (c =='/'):
            return int(op2)//int(op1)
        elif (c =='+'):
            return int(op2)+int(op1)
        elif (c =='-'):
            return int(op2)-int(op1)
        
exp = input('Enter infix expression : ')
post=infixToPostfix(exp)
#print(post)
s=postfix()
value=(s.evalute(post))
print('Result of postfix expression',exp,'=',value)