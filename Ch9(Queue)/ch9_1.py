queue = []
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
