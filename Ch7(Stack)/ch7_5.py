def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False


def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


stack = ["커피", None, None, None, None]
SIZE = len(stack)
top = -1
# top stack 확인
for i in range(len(stack)):
    if stack[i] is not None:
        top += 1

print(top)
print(stack)
retData = pop()
print("추출 데이터:-->", retData)
print(stack)
retData = pop()
