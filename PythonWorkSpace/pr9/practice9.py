# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다".format(self.name))
#         print("체력 {0},공격력 {1}".format(self.hp,self.damage))

# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)
# tank=Unit("탱크",150,35)

# wraith1=Unit("레이스",80,5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name,wraith1.damage))

# wraith2=Unit("빼앗은 레이스",80,5)
# wraith2.clocking=True

# if wraith2.clocking==True:
#     print("{0}는 현재는 클로킹 상태입니다".format(wraith2.name))


#####메소드#####
# class AttackUnit:
#     def __init__(self,name,hp,damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
    
#     def attack(self,location):
#         print("{0} :{1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name,location,self.damage))
        
#     def damaged(self,damage):
#         print("{0} :{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0} :파괴되었습니다.".format(self.name))

# firebat1=AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# #두 번
# firebat1.damaged(25)
# firebat1.damaged(25)


#####상속#####
from random import *

class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛이 생성되었습니다".format(self.name))
        # print("체력 {0},공격력 {1}".format(self.hp,self.damage))
    def move(self,location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))
    
    def damaged(self,damage):
        print("{0} :{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0} :현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} :파괴되었습니다.".format(self.name))


class AttackUnit(Unit): #Unit을 상속
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage
    
    def attack(self,location):
        print("{0} :{1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage))
        

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다, [속도 {2}]".format(name,location,self.flying_speed)) 

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        self.fly(self.name,location)
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 스팀팩을 사용합니다(HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

class Tank(AttackUnit):
    seize_developed =False  #개발 여부
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode=False

    def set_seize_mode(self):
        if Tank.seize_developed==False:
            return
        
        if self.seize_mode==False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage*=2
            self.seize_mode=True
        else:
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.damage/=2
            self.seize_mode=False


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked=False #해제 상태
    
    def clocking(self):
        if self.clocked==True:
            print("{0} ; 클로킹 모드를 해제합니다".format(self.name))
            self.clocked=True
        else: #해제 -> 설정
            print("{0} : 클로킹 모드를 설정합니다".format(self.name))
            self.clocked=True
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다")
def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하였습니다.")


#진행
game_start()
m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

#일괄 관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#모두 이동
for unit in attack_units:
    unit.move("1시")

#시즈모드 개발
Tank.seize_developed=True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다")

#공격 모드 준비(마린:스팀팩, 탱크:시즈모드, 레이스:클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

#모두 공격
for unit in attack_units:
    unit.attack("1시")

#모두 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 5~20

#게임 종료
game_over()