import random

# 선수 카드 목록
players = ["리오넬 메시", "크리스티아누 호날두", "킬리안 음바페", "엘링 홀란드", "손흥민"]

# 강화 확률
upgrade_chances = {
    1: 70,
    2: 50,
    3: 40,
    4: 30,
    5: 20,
    6: 15,
    7: 10,
    8: 5,
    9: 3,
    10: 1
}

def choose_player():
    print("=== 선수 카드 선택 ===")
    for idx, player in enumerate(players, 1):
        print(f"{idx}. {player}")
    while True:
        choice = input("선수 번호를 선택하세요: ")
        if choice.isdigit() and 1 <= int(choice) <= len(players):
            return players[int(choice)-1]
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def upgrade_card(current_level):
    if current_level >= 10:
        print("이미 최대 강화 단계입니다!")
        return current_level
    chance = upgrade_chances[current_level + 1]
    roll = random.uniform(0, 100)
    print(f"{current_level + 1}진 강화 시도! 성공 확률: {chance}%")
    if roll <= chance:
        print("강화 성공!")
        return current_level + 1
    else:
        print("강화 실패...")
        return current_level

def main():
    player = choose_player()
    level = 0
    print(f"\n{player} 카드를 선택했습니다! 현재 강화 단계: {level}진\n")
    
    while level < 10:
        action = input("강화 시도 하시겠습니까? (y/n): ").lower()
        if action == 'y':
            level = upgrade_card(level)
            print(f"현재 강화 단계: {level}진\n")
        elif action == 'n':
            print(f"{player} 카드 강화 종료. 최종 강화 단계: {level}진")
            break
        else:
            print("y 또는 n으로 입력해주세요.")
    
    if level == 10:
        print(f"축하합니다! {player} 카드가 최대 10진까지 강화되었습니다!")

if __name__ == "__main__":
    main()
