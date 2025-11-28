def start():
    print("당신은 어두운 숲 속에 서 있습니다.")
    print("1) 왼쪽 길로 간다")
    print("2) 오른쪽 길로 간다")
    choice = input("> ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("잘못된 입력입니다.")
        start()

def left_path():
    print("왼쪽 길로 가니 낡은 상자 하나를 발견했습니다.")
    print("상자 안에는 튼튼한 몽둥이가 들어 있습니다!")
    print("이제 몽둥이를 얻었습니다.")
    
    print("앞으로 가니 늑대가 나타났습니다!")
    print("1) 도망친다")
    print("2) 싸운다")
    choice = input("> ")

    if choice == "1":
        print("당신은 무사히 도망쳤습니다.")
    elif choice == "2":
        print("몽둥이를 휘두르며 늑대와 싸웠습니다...")
        print("🎉 늑대를 무찌르고 길을 안전하게 지나갔습니다!")
    else:
        print("잘못된 입력입니다.")
        left_path()

def right_path():
    print("오른쪽 길로 가니 작은 동굴 입구를 발견했습니다.")
    print("조심스럽게 동굴 안으로 들어가자, 동굴 안에는 오래된 보물 상자와 함께 이상한 문양들이 새겨진 벽이 있습니다.")
    print("보물 상자를 열어보니 금화와 마법의 물약이 들어 있습니다!")
    print("게임 클리어! 하지만 모험은 이제 시작일 것 같다...")

if __name__ == "__main__":
    start()


    