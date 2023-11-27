def countDown(n):
    if n == 0:
        print("발사!!")
    else:
        print(n)
        countDown(n - 1)


def countDownRet(n):
    if n == 6:
        print("발사!!")
        return
    else:
        countDownRet(n + 1)
        print(n)


def printStar(n):
    if n > 0:
        printStar(n - 1)
        print('★' * n)


def printStarRet(n):
    if n > 5:
        return 5
    print('★' * n)
    printStarRet(n + 1)
    print('★' * n)


countDown(5)
countDownRet(1)
printStar(5)
printStarRet(1)
