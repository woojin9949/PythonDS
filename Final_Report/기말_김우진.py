import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum


class Day(Enum):
    Mon = "월"
    Tue = "화"
    Wed = "수"
    Thu = "목"
    Fri = "금"


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def DrawGraph(Graph, title_name, array):
    DiGraph = nx.DiGraph()
    for i in range(7):
        for j in range(7):
            if Graph.graph[i][j] == 1:
                DiGraph.add_edge(array[i], array[j])
    pos = nx.spring_layout(DiGraph)
    plt.figure()
    plt.title(title_name)
    nx.draw(DiGraph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8,
            arrows=True)
    plt.show()


# HomeArray = ['Home', 'Seongbok', 'Migeum', 'Sujigu Office', 'Jukjeon', 'Giheung', 'KangnamUniv']
def AttendGraph(G1):
    G1.graph[0][1] = 1
    G1.graph[0][2] = 1
    G1.graph[0][3] = 1
    G1.graph[0][4] = 1
    G1.graph[1][2] = 1
    G1.graph[1][3] = 1
    G1.graph[1][4] = 1
    G1.graph[2][1] = 1
    G1.graph[2][3] = 1
    G1.graph[2][4] = 1
    G1.graph[2][5] = 1
    G1.graph[2][6] = 1
    G1.graph[3][1] = 1
    G1.graph[3][2] = 1
    G1.graph[3][4] = 1
    G1.graph[3][5] = 1
    G1.graph[3][6] = 1
    G1.graph[4][1] = 1
    G1.graph[4][2] = 1
    G1.graph[4][3] = 1
    G1.graph[4][5] = 1
    G1.graph[4][6] = 1
    G1.graph[5][2] = 1
    G1.graph[5][3] = 1
    G1.graph[5][4] = 1
    G1.graph[5][6] = 1
    G1.graph[6][2] = 1
    G1.graph[6][3] = 1
    G1.graph[6][4] = 1
    G1.graph[6][5] = 1


# UnivArray = ['KangnamUniv', 'Giheung', 'Jukjeon', 'Sujigu Office', 'Migeum', 'Seongbok', 'Home']
def ReturnGraph(G2):
    G2.graph[0][1] = 1
    G2.graph[0][2] = 1
    G2.graph[0][3] = 1
    G2.graph[0][4] = 1
    G2.graph[1][2] = 1
    G2.graph[1][3] = 1
    G2.graph[1][4] = 1
    G2.graph[2][1] = 1
    G2.graph[2][3] = 1
    G2.graph[2][4] = 1
    G2.graph[2][6] = 1
    G2.graph[3][1] = 1
    G2.graph[3][2] = 1
    G2.graph[3][4] = 1
    G2.graph[3][5] = 1
    G2.graph[3][6] = 1
    G2.graph[4][1] = 1
    G2.graph[4][2] = 1
    G2.graph[4][3] = 1
    G2.graph[4][5] = 1
    G2.graph[4][6] = 1
    G2.graph[5][2] = 1
    G2.graph[5][3] = 1
    G2.graph[5][4] = 1
    G2.graph[5][6] = 1


def Matrix(Graph, title_name):
    print(title_name)
    for row in range(7):
        for col in range(7):
            print(Graph.graph[row][col], end=' ')
        print()


G1 = None
G2 = None
stack = []
visitedAry = []
G1 = Graph(7)
G2 = Graph(7)
# 집노드 출발 방향 그래프
HomeArray = ['Home', 'Seongbok', 'Migeum', 'Sujigu Office', 'Jukjeon', 'Giheung', 'KangnamUniv']
UnivArray = ['KangnamUniv', 'Giheung', 'Jukjeon', 'Sujigu Office', 'Migeum', 'Seongbok', 'Home']
AttendGraph(G1)
ReturnGraph(G2)
Matrix(G1, "G1 행렬")
Matrix(G2, "G2 행렬")


DrawGraph(G1, "HomeToUniv", HomeArray)
DrawGraph(G2, "UnivToHome", UnivArray)
