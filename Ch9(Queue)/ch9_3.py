SIZE = 5
queue = [None for _ in range(SIZE)]
print(queue)
front = rear = -1


def isQueueFull():
    global SIZE, front, rear, queue
    if rear == SIZE - 1:
        return True
    else:
        return False


def isQueueEmpty():
    global SIZE, front, rear, queue
    if front == rear:
        return True
    else:
        return False


def enQueue(data):
    global SIZE, front, rear, queue
    if isQueueFull():
        print("큐 꽉참")
        return
    rear += 1
    queue[rear] = data
    print()
    print("enQueue -->", data)
    for i in range(0, len(queue)):
        print(queue[i], end=" ")


def deQueue():
    global SIZE, front, rear, queue
    if isQueueEmpty():
        print()
        print("큐가 비어있음 deQueue 불가!")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    print()
    print("deQueue -->", data)
    for i in range(0, len(queue)):
        print(queue[i], end=" ")
    if front == rear:
        front = rear = -1


enQueue("솔라")
enQueue("화사")
deQueue()
deQueue()
deQueue()

print("front, rear 값:", end=" ")
print(f"{front, rear}")
