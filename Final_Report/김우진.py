class Node:
    def __init__(self, name, transportation=None, children=None):
        self.name = name
        self.transportation = transportation or "도보"
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)


def print_path(node, path=[]):
    path = path + [(node.name, node.transportation)]
    if not node.children:
        print(" -> ".join(f"{location} ({mode})" for location, mode in path))
    else:
        for child in node.children:
            print_path(child, path)


# 트리 구성
home = Node("Home")
gate = Node("Gate", "도보")
street = Node("Street", "도보", [gate])
school = Node("School", "도보", [gate])

subway_station = Node("Subway Station", "지하철", [street])
bus_stop = Node("Bus Stop", "버스", [street])

home.add_child(street)
street.add_child(subway_station)
street.add_child(bus_stop)
subway_station.add_child(school)
bus_stop.add_child(school)

# 중간 노드 추가
seongbok_station = Node("Seongbok Station", "지하철", [subway_station])
jukjeon_station = Node("Jukjeon Station", "지하철", [subway_station])
gangnam_univ_station = Node("Gangnam University Station", "지하철", [subway_station])

street.add_child(seongbok_station)
street.add_child(jukjeon_station)
street.add_child(gangnam_univ_station)

# 가장 간단한 경우의 예시 출력
print("집에서 학교로 가는 경로:")
print_path(home)
