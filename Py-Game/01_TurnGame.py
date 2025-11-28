import random
import time

# =============================
# 캐릭터 클래스 정의 (궁극기 포함)
# =============================
class Character:
    def __init__(self, name, hp, atk, sp_atk_name, sp_atk_damage, ult_name, ult_damage, ult_cooldown):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.sp_atk_name = sp_atk_name
        self.sp_atk_damage = sp_atk_damage
        self.ult_name = ult_name
        self.ult_damage = ult_damage
        self.ult_cooldown = ult_cooldown  # 궁극기 쿨타임
        self.ult_ready_in = 0  # 남은 쿨타임

    def basic_attack(self, target):
        print(f"{self.name}의 기본 공격! {self.atk} 데미지!")
        target.hp -= self.atk

    def special_attack(self, target):
        print(f"{self.name}의 특수 공격 [{self.sp_atk_name}]! {self.sp_atk_damage} 데미지!")
        target.hp -= self.sp_atk_damage

    def ultimate_attack(self, target):
        if self.ult_ready_in == 0:
            print(f"{self.name}의 궁극기 [{self.ult_name}] 발동! {self.ult_damage} 데미지!")
            target.hp -= self.ult_damage
            self.ult_ready_in = self.ult_cooldown
        else:
            print(f"궁극기는 아직 준비되지 않았습니다. 남은 쿨타임: {self.ult_ready_in}")
            self.basic_attack(target)

    def reduce_cooldowns(self):
        if self.ult_ready_in > 0:
            self.ult_ready_in -= 1

# =============================
# 직업 캐릭터 정의
# =============================
jobs = {
    "1": ("전사", 150, 20, "파워 슬래시", 40, "분노의 강타", 100, 3),
    "2": ("마법사", 100, 22, "파이어볼", 55, "메테오 스트라이크", 150, 3),
    "3": ("궁수", 110, 22, "헤드샷", 50, "천벌의 화살", 120, 3),
    "4": ("도적", 100, 24, "백스탭", 40, "암살자 일격", 150, 3)
}

# =============================
# 적 캐릭터 정의
# =============================
enemies = [
    Character("슬라임", 60, 8, "점액 폭발", 10, "슬라임 대폭발", 12, 4),
    Character("고블린", 80, 12, "광폭화", 15, "고블린 난동", 20, 4),
    Character("해골 병사", 100, 20, "뼈 부수기", 25, "해골 폭격", 30, 4),
    Character("오크 전사", 150, 30, "분노의 일격", 35, "오크 광란", 40, 4)
]

# =============================
# 전투 함수
# =============================
def battle(player, enemy):
    print(f"\n=== 새로운 전투 시작! 적: {enemy.name} ===")

    # 선공 결정
    turn = random.choice(["player", "enemy"])
    print(f"먼저 공격하는 쪽은... {turn.upper()}!")

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp} | {enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        
        # 플레이어 턴
        if turn == "player":
            print("\n1. 기본 공격")
            print(f"2. 특수 공격 ({player.sp_atk_name})")
            print(f"3. 궁극기 ({player.ult_name}) - 남은 쿨타임: {player.ult_ready_in}")
            cmd = input("행동을 선택하세요: ")

            if cmd == "1":
                player.basic_attack(enemy)
            elif cmd == "2":
                player.special_attack(enemy)
            elif cmd == "3":
                player.ultimate_attack(enemy)
            else:
                print("잘못된 입력! 기본 공격!")
                player.basic_attack(enemy)

            player.reduce_cooldowns()
            turn = "enemy"
        
        # 적 턴
        else:
            action = random.choice(["basic", "special", "ultimate"])
            if action == "basic":
                enemy.basic_attack(player)
            elif action == "special":
                enemy.special_attack(player)
            else:
                enemy.ultimate_attack(player)
            enemy.reduce_cooldowns()
            turn = "player"

        time.sleep(0.5)

    # 승패 판정
    if player.hp > 0:
        print(f"\n🎉 {player.name} 승리! {enemy.name}을(를) 쓰러뜨렸다!")
        return True
    else:
        print(f"\n💀 {player.name} 패배... 게임 오버.")
        return False

# =============================
# 게임 시작
# =============================
print("=== 직업을 선택하세요 ===")
print("1. 전사   2. 마법사   3. 궁수   4. 도적")
job = input("번호 입력: ")

if job not in jobs:
    print("잘못된 선택입니다. 기본 직업 '전사'로 설정합니다.")
    job = "1"

job_info = jobs[job]
player = Character(*job_info)

print(f"\n당신은 '{player.name}'(으)로 선택했습니다!\n")

# 전투 루프
for enemy in enemies:
    # 전투 전 체력 회복
    print("\n전투 전 체력을 약간 회복합니다.")
    player.hp += 30
    if player.hp > player.max_hp:
        player.hp = player.max_hp

    if not battle(player, enemy):
        break
else:
    print("\n🎉 모든 적을 물리쳤습니다! 게임 클리어!! 🎉")

