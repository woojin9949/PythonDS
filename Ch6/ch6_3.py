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


def insertNodes(findData, insertData):
    global memory, head, current, pre
    if head.data == findData:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node  # 마지막 노드 첫 번째 노드 link 연결
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()  # 마지막 노드 삽입
    node.data = insertData
    current.link = node
    node.link = head


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

    insertNodes("다현", "화사")
    printNodes(head)

    insertNodes("사나", "솔라")
    printNodes(head)

    insertNodes("지효", "문별")
    printNodes(head)
