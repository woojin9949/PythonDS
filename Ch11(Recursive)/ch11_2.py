# 재귀 호출로 구현
def sumValue(num):
    if num <= 1:
        return 1
    return num + sumValue(num - 1)


def sumValueUp(num):
    if num >= 10:
        return 10
    return num + sumValueUp(num + 1)


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def factorialOp(num):
    if num <= 1:
        print("1 반환")
        return 1
    print("%d * %d! 호출" % (num, num - 1))
    retVal = factorialOp(num - 1)
    return num * retVal


print(sumValue(10))
print(sumValueUp(1))
print('10! =', factorial(10))
print('10! =', factorialOp(10))
