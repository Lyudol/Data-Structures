stack = []
element = 0
count = 0
limit = int(input("Please enter your stack limit: "))

def push(element):    
    while len(stack) != limit:
        if element != "":
            print("--------------------")
            element = input("If you want to push, enter data here. Otherwise skip: ")
            if element == "":
                userinputs(element)
            else:
                stack.append(element)
        elif element == "":
            pass
    if len(stack) == limit:
        print("--------------------")
        print("STACK FULL")
        userinputs(element)
    else:
        userinputs(element)

def userinputs(element):
    print("--------------------")
    operation = input("Enter 'Push', 'Pop', or 'Peek' to perform their respective operations: ")
    if operation == "push":
        push(element)
    elif operation == "pop":
        if len(stack) == 0:
            print("--------------------")
            print("STACK EMPTY")
            print("--------------------")
            userinputs(element)
        else:
            stack.pop()
            userinputs(element)
    elif operation == "peek":
        print("--------------------")
        print("Top element is:", stack[-1])
        userinputs(element)

push(element)