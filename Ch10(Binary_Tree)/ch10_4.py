class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)


def findNode(findNode):
    current = root
    while True:
        if findNode == current.data:
            print(findNode, "을 찾음")
            break
        elif findNode < current.data:
            if current.left is None:
                print(findNode, "가 트리에 없음")
                break
            current = current.left
        else:
            if current.right is None:
                print(findNode, "가 트리에 없음")
                break
            current = current.right


memory = []
root = None
nameArray = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = nameArray[0]
root = node
memory.append(node)

for name in nameArray[1:]:
    node = TreeNode()
    node.data = name
    current = root

    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리 구성 완료')
inorder(root)
print()
findNode('에이핑크')
