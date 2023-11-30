def findMinIdx(arr):
    minIdx = 0
    for i in range(1, len(arr)):
        if arr[minIdx] > arr[i]:
            minIdx = i
    return minIdx


testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)
print("최솟값: ", testAry[minPos])
