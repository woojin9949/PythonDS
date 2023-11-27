queue = []
global front, rear
for i in range(0, 5):
    queue.append(None)
print(queue)
front = rear = -1

rear += 1
queue[rear] = "화사"

rear += 1
queue[rear] = "솔라"

rear += 1
queue[rear] = "문별"

for i in range(0, len(queue)):
    print(queue[i], end=" ")

print()


def deQueue():
    global front, rear
    front += 1
    data = queue[front]
    queue[front] = None
    print("deQueue -->", data)
    if front == rear:
        front = rear = -1


deQueue()
deQueue()
# deQueue()
for i in range(0, len(queue)):
    print(queue[i], end=" ")

print()
print("front, rear 값:", end=" ")
print(f"{front, rear}")
