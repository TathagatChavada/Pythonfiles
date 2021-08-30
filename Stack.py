# Stack Operation

# Checking if Stack is Empty or not.
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

# Putting an item into the Stack.
def Push(stk,item):
    stk.append(item)
    top = len(stk) - 1

# Popping out the top most element of the Stack.
def Pop(stk):
    if isEmpty(stk):
        return 'Underflow'

    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        
        else:
            top = len(stk) - 1
        return item

# Peeking at the top of the Stack.
def Peek(stk):
    if isEmpty(stk):
        return 'Underflow'

    else:
        top = len(stk) - 1
        return stk[top]

# Displaying the Stack
def Display_Stacks(stk):
    if isEmpty(stk):
        return 'Underflow'

    else:
        top = len(stk) - 1
        print(stk[top],'<----Top')
        for i in range(top-1,-1,-1):
            print(stk[i])

# Initializing a Stack.
Stack = []
top = None

ans = 'y'

# Menu of Operations to be done on Stack.
while ans == 'y' or ans == 'Y':
    print('\t1. Push an element in stack.\n'
          '\t2. Pop an element from stack.\n'
          '\t3. Peek at the top of stack\n'
          '\t4. Display the stack.\n')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        item = int(input('Enter item: '))
        Push(Stack,item)

    elif choice == 2:
        item = Pop(Stack)

        if item == 'Underflow':
            print('Underflow! Stack is Empty.....')

        else:
            print('Popped item is: ',item)

    elif choice == 3:
        item = Peek(Stack)
        if item == 'Underflow':
            print('Underflow! Stack is Empty.....')
        
        else:
            print('Top most item is: ',item)

    elif choice == 4:
        Display_Stacks(Stack)

    ans = input('You want to run again (y or Y): ')