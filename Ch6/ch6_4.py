class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()


def deleteNodes(deleteData):
    global memory, head, current, pre
    if head.data == deleteData:  # 첫 번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current:  # 마지막 노드 link 연결
            last = last.link
        last.link = head
        del current
        return

    current = head
    while current.link != head:  # 중간 노드 삭제
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del current
            return


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    deleteNodes("다현")
    printNodes(head)

    deleteNodes("쯔위")
    printNodes(head)

    deleteNodes("지효")
    printNodes(head)
