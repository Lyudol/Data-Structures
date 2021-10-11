def init():
    queue = []
    element = 0
    addflag = 0
    elementset(queue, element, addflag)
def elementset(queue, element, addflag):
    if addflag == 0:
        if element != "-$fin":
            element = input("Enter queue element (Enter '-$fin' to finalize): ")
            queue.append(element)
            elementset(queue, element, addflag)
        elif element == "-$fin":
            queue.pop(-1)
            loop(queue, addflag)
    elif addflag == 1:
        addflag = 0
        queue.append(element)
        loop(queue, addflag)
def loop(queue, addflag):
    print("--------------------")
    print("Queue is ", queue,".")
    element = input("To append element, enter it here. To pop 1st element, enter '-$pop': ")
    if element != "" and element != "-$pop":
        addflag = 1
        elementset(queue, element, addflag)
    elif element == "-$pop":
        queue.pop(0)
        loop(queue, addflag)
    else:
        loop(queue, addflag)
init()