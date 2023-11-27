def isStackFull():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if isStackFull():
        print("스택이 다 찼음")
        print(f"{data} 넣을 수 없음")
        return
    top += 1
    stack[top] = data


stack = ["커피", "녹차", "꿀물", "콜라", None]
SIZE = len(stack)
top = -1
# top stack 확인
for i in range(len(stack)):
    if stack[i] is not None:
        top += 1

print(top)
print(stack)
push("환타")
print(stack)
push("삼다수")
