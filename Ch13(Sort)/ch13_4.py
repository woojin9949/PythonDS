def findInsertIdx(arr, data):
    findIdx = -1
    for i in range(0, len(arr)):
        if arr[i] > data:
            findIdx = i
            break
    if findIdx == -1:
        return len(arr)
    else:
        return findIdx


testArray = []
insPos = findInsertIdx(testArray, 55)
print("삽입할 위치: ", insPos)

testArray = [33, 77, 88]
insPos = findInsertIdx(testArray, 55)
print("삽입할 위치: ", insPos)

testArray = [33, 55, 77, 88]
insPos = findInsertIdx(testArray, 100)
print("삽입할 위치: ", insPos)
