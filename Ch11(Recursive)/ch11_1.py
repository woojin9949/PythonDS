# 각 Tree 마다 Recursive를 해준다면?
#           A
#      B         C      # A에서 left와 right 검사
#   D      E  F     G   # B에서 left와 right 검사 / C에서 left와 right 검사

def openBox():
    global count
    print("종이 상자를 엽니다.")
    count -= 1
    if count == 0:
        print("반지를 넣고 반환합니다.")
        return
    # 함수 호출보다 앞에 있으므로 호출하는 과정
    openBox()
    # 함수 호출보다 뒤에 있으므로 복귀 하는 과정
    print("종이 상자를 닫습니다.")


count = 10
openBox()
