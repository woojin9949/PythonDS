def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False


def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었음")
        return
    return stack[top]


stack = ["커피", None, None, None, None]
SIZE = len(stack)
top = -1
# top stack 확인
for i in range(len(stack)):
    if stack[i] is not None:
        top += 1

# print(top)
print(stack)
retData = peek()
print("현재 top에 있는 정보-->", retData)
