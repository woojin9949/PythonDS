def isQueueFull():
    global SIZE, front, rear, queue
    if rear != SIZE - 1:
        return False
    elif rear == SIZE - 1 and front == -1:
        return True
    # else:
    #     for i in range(front + 1, SIZE):
    #         queue[i - 1] = queue[i]
    #         queue[i] = None
    #     front -= 1
    #     rear -= 1
    #     return False


def isQueueEmpty():
    global SIZE, front, rear, queue
    if front == rear:
        return True
    else:
        return False


def peek():
    global SIZE, front, rear, queue
    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None
    return queue[front + 1]


def enQueue(data):
    global SIZE, front, rear, queue
    if isQueueFull():
        print("큐 꽉찼습니다.")
        return
    rear += 1
    queue[rear] = data


def deQueue():
    global SIZE, front, rear, queue
    if isQueueEmpty():
        print("큐가 비어있습니다.")
        return None
    front += 1
    retData = queue[front]
    queue[front] = None
    # 추출했을때 큐 앞당기기
    for i in range(front + 1, SIZE):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1
    return retData


SIZE = int(input("큐 크기 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = -1

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
        elif select == 'X' or select == 'x':
            break
        else:
            print("입력 오류")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    print("프로그램 종료")
