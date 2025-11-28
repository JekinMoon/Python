'''
def start():
    print("당신은 어두운 숲 속에 서 있습니다.")
    print("1) 왼쪽 길로 간다")
    print("2) 오른쪽 길로 간다")
    choice = input("> ")

    if choice == "1":
        left_path_1()
    elif choice == "2":
        right_path_1()
    else:
        print("잘못된 입력입니다.")
        start()

# =========================
# 왼쪽 길
# =========================
def left_path_1():
    print("\n왼쪽 길로 가니 낡은 상자 하나를 발견했습니다.")
    print("상자 안에는 튼튼한 몽둥이가 들어 있습니다! 이제 몽둥이를 얻었습니다.")
    print("앞으로 가니 갈림길이 나타났습니다.")
    print("1) 숲속 다리로 간다")
    print("2) 숲속 호수로 간다")
    choice = input("> ")

    if choice == "1":
        left_path_2_bridge()
    elif choice == "2":
        left_path_2_lake()
    else:
        print("잘못된 입력입니다.")
        left_path_1()

def left_path_2_bridge():
    print("\n작은 다리를 건너려는데, 늑대가 나타났습니다!")
    print("1) 도망친다")
    print("2) 싸운다")
    choice = input("> ")

    if choice == "1":
        print("당신은 무사히 도망쳤습니다.")
    elif choice == "2":
        print("몽둥이를 휘두르며 늑대를 무찔렀습니다! 다리를 안전하게 건넜습니다.")
    else:
        print("잘못된 입력입니다.")
        left_path_2_bridge()

def left_path_2_lake():
    print("\n호수에 다다르자, 호수 안에서 반짝이는 무언가가 보입니다.")
    print("1) 호수에 들어가 본다")
    print("2) 돌아간다")
    choice = input("> ")

    if choice == "1":
        print("호수에서 마법의 물약을 발견했습니다! 마법의 물약을 소지품에 넣었습니다.")
    elif choice == "2":
        print("숲속으로 돌아가며 안전하게 진행합니다.")
    else:
        print("잘못된 입력입니다.")
        left_path_2_lake()

# =========================
# 오른쪽 길
# =========================
def right_path_1():
    print("\n오른쪽 길로 가니 작은 동굴 입구를 발견했습니다.")
    print("1) 동굴 안으로 들어간다")
    print("2) 동굴 주변을 탐색한다")
    choice = input("> ")

    if choice == "1":
        right_path_2_cave()
    elif choice == "2":
        right_path_2_explore()
    else:
        print("잘못된 입력입니다.")
        right_path_1()

def right_path_2_cave():
    print("\n동굴 안에는 미로 같은 복도가 있습니다.")
    print("1) 왼쪽으로 간다")
    print("2) 오른쪽으로 간다")
    choice = input("> ")

    if choice == "1":
        print("왼쪽 길 끝에서 금화가 담긴 상자를 발견했습니다! 게임 클리어!")
    elif choice == "2":
        print("오른쪽 길 끝에는 이상한 문양이 새겨진 방이 있습니다. 모험은 계속됩니다...")
    else:
        print("잘못된 입력입니다.")
        right_path_2_cave()

def right_path_2_explore():
    print("\n동굴 주변을 탐색하니, 숨겨진 작은 상자를 발견했습니다!")
    print("상자 안에는 마법의 물약과 작은 금화가 들어 있습니다. 모험은 계속됩니다...")
    
# =========================
# 게임 시작
# =========================
if __name__ == "__main__":
    start()
'''
import random
import time

# =============================
# 포켓몬 클래스 정의
# =============================
class Pokemon:
    def __init__(self, name, p_type, hp, moves):
        self.name = name
        self.type = p_type  # '전기', '물', '풀', '불'
        self.max_hp = hp
        self.hp = hp
        self.moves = moves  # {기술이름: (데미지, 타입)}

    def attack(self, move_name, target):
        if move_name not in self.moves:
            print("잘못된 기술 선택! 기본 공격 사용")
            move_name = list(self.moves.keys())[0]

        base_damage, move_type = self.moves[move_name]

        # 타입 상성 계산
        effectiveness = type_effectiveness(move_type, target.type)

        # 크리티컬 확률 10%
        crit = 1
        if random.random() < 0.1:
            crit = 2
            print("💥 크리티컬 히트!")

        damage = int(base_damage * effectiveness * crit)
        target.hp -= damage
        print(f"{self.name}의 {move_name}! {damage} 데미지! (타입 효과 x{effectiveness})")
        if target.hp < 0:
            target.hp = 0

# =============================
# 타입 상성 함수
# 전기 -> 물 -> 풀 -> 불 -> 전기
# =============================
def type_effectiveness(attack_type, target_type):
    type_chart = {
        '전기': '물',
        '물': '불',
        '풀': '물',
        '불': '풀'
    }
    if attack_type == target_type:
        return 1
    elif type_chart.get(attack_type) == target_type:
        return 2  # 강함
    elif type_chart.get(target_type) == attack_type:
        return 0.5  # 약함
    else:
        return 1

# =============================
# 포켓몬 정의
# =============================
bulbasaur = Pokemon("이상해씨", "풀", 100, {
    "덩굴채찍": (15, "풀"),
    "씨뿌리기": (20, "풀"),
    "몸통박치기": (10, "풀"),
    "속임수": (12, "풀")
})

charmander = Pokemon("파이리", "불", 100, {
    "불꽃세례": (20, "불"),
    "화염방사": (25, "불"),
    "몸통박치기": (10, "불"),
    "불꽃펀치": (15, "불")
})

squirtle = Pokemon("꼬부기", "물", 100, {
    "물대포": (20, "물"),
    "거품": (15, "물"),
    "몸통박치기": (10, "물"),
    "하이드로펀치": (25, "물")
})

pikachu = Pokemon("피카츄", "전기", 100, {
    "전기충격": (15, "전기"),
    "번개": (20, "전기"),
    "몸통박치기": (10, "전기"),
    "스파크": (18, "전기")
})

all_pokemon = [bulbasaur, charmander, squirtle, pikachu]

# =============================
# 플레이어 포켓몬 선택
# =============================
print("포켓몬 배틀 시작! 원하는 포켓몬을 선택하세요.")
for i, p in enumerate(all_pokemon, 1):
    print(f"{i}) {p.name} ({p.type})")
choice = input("> ")

try:
    player = all_pokemon[int(choice)-1]
except:
    print("잘못된 선택! 기본 포켓몬 피카츄로 설정합니다.")
    player = pikachu

# 상대 포켓몬 랜덤 선택 (플레이어와 중복되지 않게)
enemy = random.choice([p for p in all_pokemon if p != player])

print(f"\n당신은 {player.name}를 선택했습니다! 상대는 {enemy.name}!\n")

# =============================
# 턴제 배틀 루프
# =============================
turn = random.choice(["player", "enemy"])
print(f"먼저 공격하는 쪽은... {turn.upper()}!\n")

while player.hp > 0 and enemy.hp > 0:
    print(f"{player.name} HP: {player.hp}/{player.max_hp} | {enemy.name} HP: {enemy.hp}/{enemy.max_hp}\n")
    
    if turn == "player":
        print("기술 목록:")
        for i, move in enumerate(player.moves.keys(), 1):
            print(f"{i}) {move}")
        move_choice = input("> ")
        try:
            move_name = list(player.moves.keys())[int(move_choice)-1]
        except:
            print("잘못된 입력! 첫 번째 기술 사용")
            move_name = list(player.moves.keys())[0]

        player.attack(move_name, enemy)
        turn = "enemy"

    else:
        # 적은 랜덤으로 기술 선택
        move_name = random.choice(list(enemy.moves.keys()))
        enemy.attack(move_name, player)
        turn = "player"

    time.sleep(1)

# =============================
# 승패 판정
# =============================
if player.hp > 0:
    print(f"\n🎉 {enemy.name}를 쓰러뜨리고 승리했습니다! 🎉")
else:
    print(f"\n💀 {player.name}가 쓰러졌습니다... 패배")

