class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = Graph(7)
# 집노드 출발 방향 그래프
nameArray = ['집', '성복역', '미금역', '강남대역', '기흥역', '수지구청역', '죽전역']
집, 성복역, 미금역, 강남대역, 기흥역, 수지구청역, 죽전역 = 0,1,2,3,4,5,6
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][5] = 1; G1.graph[0][6] = 1
G1.graph[1][2] = 1; G1.graph[1][5] = 1; G1.graph[1][6] = 1
G1.graph[2][1] = 1; G1.graph[2][3] = 1; G1.graph[2][4] = 1; G1.graph[2][5] = 1; G1.graph[2][6] = 1
G1.graph[3][2] = 1; G1.graph[3][4] = 1; G1.graph[3][5] = 1; G1.graph[3][6] = 1
G1.graph[4][2] = 1; G1.graph[4][3] = 1; G1.graph[4][5] = 1; G1.graph[4][6] = 1
G1.graph[5][1] = 1; G1.graph[5][2] = 1; G1.graph[5][3] = 1; G1.graph[5][4] = 1; G1.graph[5][6] = 1
G1.graph[6][1] = 1; G1.graph[6][2] = 1; G1.graph[6][3] = 1; G1.graph[6][4] = 1; G1.graph[6][5] = 1

print("G1 그래프 완성")
# for v in range(7):
#     print(nameArray[v],end=' ')
# print()
# for row in range(7):
#     print(nameArray[row],end=' ')
#     for col in range(7):
#         print(G1.graph[row][col],end=' ')
#     print()
# print()
for row in range(7):
    for col in range(7):
        print(G1.graph[row][col],end=' ')
    print()

