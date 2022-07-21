def create_stack():
    stack = []
    return stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
def pop(stack):
    if (len(stack)==0):
        return "stack is empty"
    else:
        print("popped element is:"+ stack.pop())
def display(stack):
    print("stack: "+ str(stack))
       

stack = create_stack()
push(stack,"1")
push(stack,"1")
push(stack,"3")
push(stack,"4")
push(stack,"5")
display(stack)
pop(stack)
display(stack)

