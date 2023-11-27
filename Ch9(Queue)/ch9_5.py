SIZE = int(input("큐 크기 입력하세요 ==>"))
queue = [None for _ in range(SIZE)]
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


def peek():
    global SIZE, front, rear, queue
    if isQueueEmpty():
        print("큐가 비었음")
        return None
    return queue[front + 1]


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
    return data


if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    while select != 'X' or select != 'x':
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print("큐 상태: ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태: ", queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태: ", queue)
        else:
            print("입력 오류")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    print("프로그램 종료")
