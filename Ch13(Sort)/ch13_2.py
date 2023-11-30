def findMinIdx(arr):
    minIdx = 0
    for i in range(1, len(arr)):
        if arr[minIdx] > arr[i]:
            minIdx = i
    return minIdx


beforeArray = [188, 162, 144, 47, 59, 199, 0]
afterArray = []
print(beforeArray)
# 최솟값을 찾아 array에 저장후, 최솟값에 해당되는 인덱스로 원본 배열에서 삭제를 하고 또 다시 반복함
for _ in range(len(beforeArray)):
    minPos = findMinIdx(beforeArray)
    afterArray.append(beforeArray[minPos])
    del (beforeArray[minPos])
print(afterArray)
