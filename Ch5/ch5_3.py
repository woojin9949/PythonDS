class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current is None:
        return
    print(current.data, end=" ")
    while current.link is not None:
        current = current.link
        print(current.data, end=" ")
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data is findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    # 오류
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    insertNode("다현", "화사")
    printNodes(head)
