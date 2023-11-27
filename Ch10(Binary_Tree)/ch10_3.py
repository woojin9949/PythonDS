class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


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
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)


print('이진 탐색 트리 구성 완료')
print(memory)
inorder(root)
