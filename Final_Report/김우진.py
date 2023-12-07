import networkx as nx
import matplotlib.pyplot as plt
import random


# 그저 구현에만 초점을 두고 집에서 학교로 가는 학교에서 집으로 가는 루트에 해당되는 메커니즘에 집중을 하였지만
# 이번 기말 구현과제에서는 그래프 DFS의 과정에 대해 더 공부를 해보고 변형을 해보았습니다.
# 그래프 전체를 탐색하는 방법중 하나이지만 저는 목표지점을 정하여 출발 노드와 도착노드간에 노드들을 설정하여
# 방향 및 무방향 엣지들을 설정하여 구현하였고, 주로 DFS알고리즘을 구현하여 실행 할 경우 그래프의 모든 노드들을 찾아가며
# 순회하지만, 제가 구현한것은 물론 모든 노드들을 들르면서 가는 방법을 구하지만 적은 노드만으로도 갈 수 있게끔 루트를 구현하게 하였습니다.
# 예를들어 Home 노드에서 출발하여 Sujigu-Office를 들렸다가 바로 KangnamUniv노드로 도착을 하는것입니다.
# 이렇게 해서 max_step의 제한을 두어서 총 루트길이 3, 4, 5로 나뉘어 그 길이에 대한 루트가 보여지게끔 하였습니다.
# 이렇게 보면 단순하지만 Best,Average,Worst 알고리즘을 볼 수 있습니다.

class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


class SchoolDay:
    queue = [None for _ in range(7)]
    front = -1
    rear = -1

    def __init__(self, day):
        self.day = day

    def add_activity(self, start_time, end_time, activity):
        self.enQueue(f"{self.day} {start_time} ~ {end_time}: {activity}")

    def process_queue(self):
        self.deQueue()

    def isQueueEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def enQueue(self, data):
        self.rear += 1
        self.queue[self.rear] = data

    def deQueue(self):
        if self.isQueueEmpty():
            print("큐가 비어있습니다.")
            return None
        print("오늘의 일정입니다: ")
        while self.front <= self.rear:
            retData = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            if retData is not None:
                print(retData)


def time_to_minutes(time_str):
    # "HH:MM" 형식의 문자열을 분 단위로 변환
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def selection_sort_start_time(queue):
    n = len(queue)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if queue[j] is not None:
                # queue -> day,start_time,end_time,activity 구성
                start_time_i = time_to_minutes(queue[min_index].split()[1])
                start_time_j = time_to_minutes(queue[j].split()[1])

                if start_time_i > start_time_j:
                    min_index = j
        queue[i], queue[min_index] = queue[min_index], queue[i]


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
    print()


def print_route(stack):
    for i, routes in enumerate(stack):
        if routes:
            print(f"길이가 {i}인 루트:")
            for route in routes:
                print(route)


# max_steps를 5번을 주어 최소 평균 최대 루트를 알 수 있게됨
def dfs(graph, current, end, path, array, visited_nodes, max_steps):
    path.append(array[current])
    visited_nodes.append(current)

    if current == end:
        # path의 길이에 따른 분류를 위해 설정하였음
        stack[len(path)].append(path.copy())
    elif len(path) < max_steps:
        for i in range(len(graph.graph[current])):
            if graph.graph[current][i] == 1 or visited_nodes.count(i) < 2:
                if graph.graph[current][i] == 1:
                    dfs(graph, i, end, path, array, visited_nodes, max_steps)
    path.pop()
    visited_nodes.remove(current)


def SchoolCalendar():
    day = input("오늘은 무슨 요일입니까??")
    if day == '화':
        print("--수업 일정--")
        tuesday = SchoolDay("화요일")
        tuesday.add_activity("09:00", "11:40", "컴파일러구성론")
        for i in range(len(tuesday.queue)):
            if tuesday.queue[i] is not None:
                print(tuesday.queue[i])
        while True:
            print("추가 일정이 어떻게 되시나요?")
            start_time = input("시작시간: ")
            end_time = input("종료시간: ")
            activity = input("어떤걸 하실건가요?: ")
            tuesday.add_activity(start_time, end_time, activity)
            print("일정 작성을 그만하시려면 e를 눌러주세요")
            if input().lower() == 'e':
                break
        selection_sort_start_time(tuesday.queue)
        tuesday.process_queue()
    elif day == '수':
        print("--수업 일정--")
        wednesday = SchoolDay("수요일")
        wednesday.add_activity("17:30", "20:00", "미디어문학의이해")
        for i in range(len(wednesday.queue)):
            if wednesday.queue[i] is not None:
                print(wednesday.queue[i])
        while True:
            print("추가 일정이 어떻게 되시나요?")
            start_time = input("시작시간: ")
            end_time = input("종료시간: ")
            activity = input("어떤걸 하실건가요?: ")
            wednesday.add_activity(start_time, end_time, activity)
            print("일정 작성을 그만하시려면 e를 눌러주세요")
            if input().lower() == 'e':
                break
        selection_sort_start_time(wednesday.queue)
        wednesday.process_queue()
    elif day == '목':
        print("--수업 일정--")
        thursday = SchoolDay("목요일")
        thursday.add_activity("09:00", "11:40", "실감미디어컴퓨팅기초")
        thursday.add_activity("11:50", "14:30", "자료구조및알고리즘")
        for i in range(len(thursday.queue)):
            if thursday.queue[i] is not None:
                print(thursday.queue[i])
        while True:
            print("추가 일정이 어떻게 되시나요?")
            start_time = input("시작시간: ")
            end_time = input("종료시간: ")
            activity = input("어떤걸 하실건가요?: ")
            thursday.add_activity(start_time, end_time, activity)
            print("일정 작성을 그만하시려면 e를 눌러주세요")
            if input().lower() == 'e':
                break
        selection_sort_start_time(thursday.queue)
        thursday.process_queue()
    elif day == '금':
        print("--수업 일정--")
        friday = SchoolDay("금요일")
        friday.add_activity("14:40", "17:20", "현대암호학")
        for i in range(len(friday.queue)):
            if friday.queue[i] is not None:
                print(friday.queue[i])
        while True:
            print("추가 일정이 어떻게 되시나요?")
            start_time = input("시작시간: ")
            end_time = input("종료시간: ")
            activity = input("어떤걸 하실건가요?: ")
            friday.add_activity(start_time, end_time, activity)
            print("일정 작성을 그만하시려면 e를 눌러주세요")
            if input().lower() == 'e':
                break
        selection_sort_start_time(friday.queue)
        friday.process_queue()


def recommend_route(stack):
    # 0 1 2 3 4 5
    for i in range(len(stack)):
        # 3 4 5
        if len(stack[i]) > 0:
            random_path = random.choice(stack[i])
            print(f"길이가{i}인 루트: {random_path}")


G1, G2 = Graph(7), Graph(7)
visited_nodes = []
HomeArray = ['Home', 'Seongbok', 'Migeum', 'Sujigu Office', 'Jukjeon', 'Giheung', 'KangnamUniv']
UnivArray = ['KangnamUniv', 'Giheung', 'Jukjeon', 'Sujigu Office', 'Migeum', 'Seongbok', 'Home']

AttendGraph(G1)
ReturnGraph(G2)
Matrix(G1, "G1 행렬")
Matrix(G2, "G2 행렬")
DrawGraph(G1, "HomeToUniv", HomeArray)
DrawGraph(G2, "UnivToHome", UnivArray)
SchoolCalendar()
max_step = 5
stack = [[] for _ in range(max_step + 1)]
dfs(G1, 0, 6, [], HomeArray, visited_nodes, max_step)
print("\n집에서 강남대학교로 Best,Average,Worst 가는 루트:")
print_route(stack)
recommend_route(stack)

stack = [[] for _ in range(max_step + 1)]
dfs(G2, 0, 6, [], UnivArray, visited_nodes, max_step)
print("\n강남대학교에서 집으로 가는 Best,Average,Worst 추천 루트:")
print_route(stack)
recommend_route(stack)

