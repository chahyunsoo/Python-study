# #함수
# commission=100
# def open_count():
#     print("새로운 계좌가 생성")

# def deposit(balance,money):
#     print("입금 완료. 잔액은 {0}원".format(balance+money))
#     return balance+money
# def withdraw(balance,money):
#     if balance>=money:
#         print("출금이 완료. 잔액은 {0}".format(balance-money))
#         return balance-money
#     else:
#         print("출금 완료 X")
#         return balance

# def withdraw_night(balance,money):
#     commission=100
#     return commission,balance-money-commission
# balance=0
# balance=deposit(balance,1000)
# # balance=withdraw(balance,500)
# commission,balance=withdraw_night(balance,500)
# print("수수료는 {0}원이며, 잔액은{1}입니다".format(commission,balance))

########################################################################
#기본값
# def profile(name,age,main_lang):
#     print("이름:{0}\t나이:{1}\t언어:{2}" \
#            .format(name,age,main_lang))
# profile("cha",24,"java")
# profile("hyun",25,"python")

#같은 학교 같은 학년 같은 반 수업
# def profile(name,age=17,main_lang="java"):
#     print("이름: {0}\t나이: {1}\t언어: {2}" \
#           .format(name,age,main_lang))
# profile("cha")
# profile("hyun")

# def profile(name,age=24,lang="java"):
#     print(name,age,lang)
# profile(name="cha")
# profile(lang="java",age=25,name="hyun")

# def profile(name,age,lang1,lagn2,lagn3):
#     print("이름: {0}\t 나이: {1}\t".format(name,age),end=" ")
#     print(lang1,lagn2,lagn3)

# def profile(name,age,*language):  #서로 다른 값을 넣어줄때 가변인자를 사용 *이용
#     print("이름: {0}\t 나이: {1}\t".format(name,age),end=" ")
#     for lang in language:
#         print(lang,end=" ")
#     print()
 
# profile("cha",20,"j","c","p","js")
# profile("hyun",21,"k","s"," ")

#지역변수 & 전역변수
gun=10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun 사용(함수 밖의 gun을 checkpoint 함수 내에서 쓰겠다)
    gun=gun-soldiers
    print("남은 총 : {0}".format(gun))

print("현재 총:{0}".format(gun))

def checkpoint_return(gun,soldiers):
    gun=gun-soldiers
    print("남은 총 : {0}".format(gun))
    return gun

#checkpoint(2)
gun=checkpoint_return(gun,4)
print("남은 총: {0}".format(gun))

