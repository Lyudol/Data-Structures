def init():
  queuemaxsize = (int(input("Please specify max queue length (Non-Zero-Based): ")))
  iteration = (int(input("Please specify iteration amount: ")))
  queue = []
  head = 0
  tail = -1
  enqueuecheck(queuemaxsize, queue, head, tail, iteration)
def enqueuecheck(queuemaxsize, queue, head, tail, iteration):
  while len(queue) != queuemaxsize:
    if len(queue) < queuemaxsize:
      element = input("Enter queue element: ")
      queue.append(element)
      tail = len(queue) - 1
    else:
      pass
  if tail == queuemaxsize - 1:
    loop(queuemaxsize, queue, head, tail, iteration)
  else:
    pass
def loop(queuemaxsize, queue, head, tail, iteration):
  count = 0
  print(queue)
  while iteration - 1 > count:
    count = count + 1
    if tail == (queuemaxsize - 1):
      tail = -1
    elif tail < (queuemaxsize - 1):
      tail = tail + 1
    if head == (queuemaxsize - 1):
      head = 0
    elif head > 0 and head < queuemaxsize - 1 or (count > 0):
      head = head + 1
    else:
      head = 0
    element1 = queue[0]
    queue.pop(0)
    queue.append(element1)
    print(queue)
init()