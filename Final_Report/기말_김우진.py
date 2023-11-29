import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def AttendGraph(G1):
    G1.graph[0][1] = 1
    G1.graph[0][2] = 1
    G1.graph[0][5] = 1
    G1.graph[0][6] = 1
    G1.graph[1][2] = 1
    G1.graph[1][5] = 1
    G1.graph[1][6] = 1
    G1.graph[2][1] = 1
    G1.graph[2][3] = 1
    G1.graph[2][4] = 1
    G1.graph[2][5] = 1
    G1.graph[2][6] = 1
    G1.graph[3][2] = 1
    G1.graph[3][4] = 1
    G1.graph[3][5] = 1
    G1.graph[3][6] = 1
    G1.graph[4][2] = 1
    G1.graph[4][3] = 1
    G1.graph[4][5] = 1
    G1.graph[4][6] = 1
    G1.graph[5][1] = 1
    G1.graph[5][2] = 1
    G1.graph[5][3] = 1
    G1.graph[5][4] = 1
    G1.graph[5][6] = 1
    G1.graph[6][1] = 1
    G1.graph[6][2] = 1
    G1.graph[6][3] = 1
    G1.graph[6][4] = 1
    G1.graph[6][5] = 1


def ReturnGraph(G2):
    G2.graph[0][1] = 1
    G2.graph[0][2] = 1
    G2.graph[0][5] = 1
    G2.graph[0][6] = 1
    G2.graph[1][0] = 1
    G2.graph[1][2] = 1
    G2.graph[1][5] = 1
    G2.graph[1][6] = 1
    G2.graph[2][0] = 1
    G2.graph[2][1] = 1
    G2.graph[2][4] = 1
    G2.graph[2][5] = 1
    G2.graph[2][6] = 1
    G2.graph[3][2] = 1
    G2.graph[3][4] = 1
    G2.graph[3][5] = 1
    G2.graph[3][6] = 1
    G2.graph[4][2] = 1
    G2.graph[4][5] = 1
    G2.graph[4][6] = 1
    G2.graph[5][0] = 1
    G2.graph[5][1] = 1
    G2.graph[5][2] = 1
    G2.graph[5][4] = 1
    G2.graph[5][6] = 1
    G2.graph[6][0] = 1
    G2.graph[6][1] = 1
    G2.graph[6][2] = 1
    G2.graph[6][4] = 1
    G2.graph[6][5] = 1


G1 = Graph(7)
G2 = Graph(7)
# 집노드 출발 방향 그래프
nameArray = ['Home', 'Seongbok', 'Migeum', 'KangnamUniv', 'Giheung', 'Sujigu Office', 'Jukjeon']
AttendGraph(G1)
ReturnGraph(G2)
print("G1 그래프")
for row in range(7):
    for col in range(7):
        print(G1.graph[row][col], end=' ')
    print()
print("G2 그래프")
for row in range(7):
    for col in range(7):
        print(G2.graph[row][col], end=' ')
    print()
DG1 = nx.DiGraph()
DG2 = nx.DiGraph()
for i in range(7):
    for j in range(7):
        if G1.graph[i][j] == 1:
            DG1.add_edge(nameArray[i], nameArray[j])
for i in range(7):
    for j in range(7):
        if G2.graph[i][j] == 1:
            DG2.add_edge(nameArray[i], nameArray[j])

pos = nx.spring_layout(DG1)
plt.figure()
plt.title("HomeToUniv")
nx.draw(DG1, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrows=True)
plt.show()

pos = nx.spring_layout(DG2)
plt.figure()
plt.title("UnivToHome")
nx.draw(DG2, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrows=True)
plt.show()
