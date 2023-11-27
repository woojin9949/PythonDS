global total_time, route, pre, current, head, first_cost, second_cost, total_cost


# 차 타고 등교했을때 미구현
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        self.cost = None


def printNodes():
    global total_time, route, current, head, total_cost
    current = head
    if current is None:
        return
    print()
    print(current.data, end=" ")
    while current.link is not None:
        current = current.link
        print(f" -> {current.data}", end=" ")
    print(f" // {total_time} 분 예상")
    print(f"루트: {route} ")
    print(f"등교 비용: {first_cost}")
    print(f"하교 비용: {second_cost}")
    print(f"총 비용: {first_cost + second_cost}")
    print()


def CarNode():
    global total_time, pre, current, route, first_cost, second_cost
    Car_node = Node()
    Car_node.data = "강남대학교"
    current.link = Car_node
    pre = current
    current = current.link
    total_time += 25
    first_cost += 2400
    route.append("차 타고 등교")
    # 다시 차 타고 집으로 하교
    Home_node = Node()
    Home_node.data = "집"
    current.link = Home_node
    pre = current
    current = current.link
    total_time += 25
    second_cost += 2400
    route.append("차 타고 하교")
    print()


def JukjeonNode():
    global total_time, pre, current, route, first_cost
    print("집에서 죽전역으로 가는 방법을 선택하세요:")
    print("1. 걸어가기 (시간: 60분)")
    print("2. 버스타기 (시간: 30분, 비용: 1,350₩)")
    print("3. 택시타기 (시간: 15분, 비용: 9,500₩)")
    choice = input("선택하세요 (1, 2, 3): ")
    Jukjeon_node = Node()
    Jukjeon_node.data = "죽전역"
    current.link = Jukjeon_node
    pre = current

    if choice == "1":
        current = current.link  # 걷기 선택
        total_time += 60  # 걷기 소요 시간
        Jukjeon_node.cost = 0
        first_cost += 0
        route.append("걸어서 죽전역")
    elif choice == "2":
        current = current.link  # 버스 선택
        total_time += 30  # 버스 소요 시간
        Jukjeon_node.cost = 1350
        first_cost += 1350
        route.append("1번 버스타고 죽전역")
    elif choice == "3":
        current = current.link  # 택시 선택
        total_time += 15  # 택시 소요 시간
        Jukjeon_node.cost = 9500
        first_cost += 9500
        route.append("택시타고 죽전역")
    else:
        print("-----다시 선택해주세요-----")
        return
    print()


def GiheungNode():
    global total_time, current, pre, route, first_cost
    Giheung_node = Node()
    Giheung_node.data = "기흥역"
    current.link = Giheung_node
    pre = current
    print("기흥역으로 가는 방법을 선택하세요:")
    print("1. 버스타기 (시간: 20분, 환승O 100₩, 환승X 1450₩)")
    print("2. 지하철타기 (시간: 15분, 환승O 50₩, 환승X 1400₩)")
    choice = input("선택하세요 (1 또는 2): ")
    if choice == "1":
        if pre.cost == 0 or pre.cost == 9500:
            first_cost += 1450
            Giheung_node.cost = 1450
            route.append("690번 버스타고 기흥역(환승X)")
        else:
            first_cost += 100
            Giheung_node.cost = 100
            route.append("690번 버스타고 기흥역(환승O)")
        current = current.link
        total_time += 20
    elif choice == "2":
        if pre.cost == 0 or pre.cost == 9500:
            first_cost += 1400
            Giheung_node.cost = 1400
            route.append("수인분당선 타고 기흥역(환승X)")
        else:
            first_cost += 50
            Giheung_node.cost = 50
            route.append("수인분당선 타고 기흥역(환승O)")
        current = current.link
        total_time += 15
    else:
        print("다시 선택해주세요")
        return
    print()


def UnivNode():
    global total_time, current, pre, route, first_cost
    Univ_node = Node()
    Univ_node.data = "강남대학교"
    current.link = Univ_node
    pre = current
    print("강남대 이공관으로 가는 방법을 선택하세요:")
    print("1. 에버라인 타고 걸어가기 (시간: 30분, 버스환승: 150₩ 지하철환승: 200₩)")
    print("2. 마을버스 타고 걸어가기 (시간: 20분, 환승 무료")
    print("3. 달구지타기 (시간: 10분)")
    choice = input("선택하세요 (1 또는 2): ")
    if choice == "1":
        if pre.cost == 1450:  # 전에 버스 탔을 경우
            first_cost += 150
            route.append("에버라인 및 걸어서 이공관")
        else:  # 전에 지하철 탔을 경우
            first_cost += 200
            route.append("에버라인 및 걸어서 이공관")
        current = current.link
        total_time += 30
    elif choice == "2":
        current = current.link
        total_time += 20
        route.append("마을버스 타고 이공관")
    elif choice == "3":
        current = current.link
        total_time += 10
        route.append("달구지 타고 이공관")
    else:
        print("다시 선택해주세요")
        return
    print()


def ReGiheungNode():
    global total_time, current, pre, route, second_cost
    ReGiheung_node = Node()
    ReGiheung_node.data = "기흥역"
    current.link = ReGiheung_node
    pre = current
    print("강남대 이공관에서 기흥역으로 가는 방법을 선택하세요:")
    print("1. 강남대입구역까지 걸어가서 에버라인 타기(시간: 30분, 비용: 1,600₩)")
    print("2. 이공관에서 달구지 타기 (시간: 10분)")
    choice = input("선택하세요 (1 또는 2): ")
    if choice == "1":
        current = current.link
        total_time += 30
        ReGiheung_node.cost = 1600
        second_cost += 1600
        route.append("에버라인타고 기흥역")
    elif choice == "2":
        current = current.link
        total_time += 10
        ReGiheung_node.cost = 0
        route.append("달구지 타고 기흥역")
    else:
        print("다시 선택해주세요")
        return
    print()


def ReJukjeonNode():
    global total_time, current, pre, route, second_cost
    ReJukjeon_node = Node()
    ReJukjeon_node.data = "죽전역"
    current.link = ReJukjeon_node
    pre = current
    print("죽전역으로 가는 방법을 선택하세요:")
    print("1. 버스타기 (시간: 20분, 환승O: 0₩, 환승X: 1,450₩")
    print("2. 지하철타기 (시간: 10분, 환승O: 0₩, 환승X: 1,400₩)")
    choice = input("선택하세요 (1 또는 2): ")
    if choice == "1":
        if pre.cost == 0:  # 달구지 탔을 경우
            second_cost += 1450
            ReJukjeon_node.cost = 1450
            route.append("690번 버스타고 죽전역(환승X)")
        else:  # 에버라인 탔을 경우
            second_cost += 0
            ReJukjeon_node.cost = 0
            route.append("690번 버스타고 죽전역(환승O)")
        current = current.link
        total_time += 20
    elif choice == "2":
        if pre.cost == 0:  # 달구지 탔을 경우
            second_cost += 1400
            ReJukjeon_node.cost = 1400
            route.append("수인분당선 타고 죽전역(환승X)")
        else:  # 에버라인 탔을 경우
            second_cost += 0
            ReJukjeon_node.cost = 0
            route.append("수인분당선 타고 죽전역(환승O)")
        current = current.link
        total_time += 10
    else:
        print("다시 선택해주세요")
        return
    print()


def ReHomeNode():
    global total_time, current, pre, route, second_cost
    print("집으로 가는 방법을 선택하세요:")
    print("1. 걸어가기 (시간: 60분)")
    print("2. 버스타기 (시간: 30분, 환승O: 0₩)")
    print("3. 택시타기 (시간: 15분, 비용: 9,500₩)")
    choice = input("선택하세요 (1, 2, 3): ")
    ReHome_node = Node()
    ReHome_node.data = "집"
    current.link = ReHome_node
    pre = current
    if choice == "1":
        current = current.link
        total_time += 60
        second_cost += 0
        route.append("걸어서 집으로")
    elif choice == "2":
        current = current.link
        total_time += 30
        second_cost += 0
        route.append("1번 버스타고 집으로")
    elif choice == "3":
        current = current.link
        total_time += 15
        second_cost += 9500
        route.append("택시타고 집으로")
    else:
        print("-----다시 선택해주세요-----")
        return
    print()


def main():
    global current, head, total_time, route, total_cost
    # 기본 노드 설정
    homeNode = Node()
    homeNode.data = "집"
    homeNode.link = None
    # head 설정
    head = homeNode
    current = head
    while True:
        print("1. 차 타고 등교하기")
        print("2. 대중교통 이용하여 등교하기")
        choice = input("선택하세요 (1, 2): ")
        if choice == "1":
            CarNode()
        else:
            JukjeonNode()
            GiheungNode()
            UnivNode()
            ReGiheungNode()
            ReJukjeonNode()
            ReHomeNode()
        printNodes()
        choice = input("계속하려면 'Y'를 입력하고, 종료하려면 'N'을 입력하세요: ")
        if choice.lower() != 'y':
            break
        # 루트,비용,시간 초기화
        route.clear()
        total_time = 0
        total_cost = 0
        current = head


if __name__ == "__main__":
    # global변수 초기화 작업
    total_time = 0
    total_cost = 0
    first_cost = 0
    second_cost = 0
    cost = 0
    route = []
    current = Node()
    # main 함수 실행
    main()
