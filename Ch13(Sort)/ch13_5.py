def findInsertIdx(arr, data):
    findIdx = -1
    for i in range(0, len(arr)):
        # 인덱스 i에 대입
        if arr[i] > data:
            findIdx = i
            break
    # 값이 가장 클때 마지막 인덱스 대입
    if findIdx == -1:
        return len(arr)
    else:
        return findIdx


before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print(before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print(after)
