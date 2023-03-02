# name=input("이름이 뭡니까?")
# if name=="차현수":
#     print("제 이름입니다")
# elif name=="차현우":
#     print("동생이름입니다")
# else:
#     print("")



# temp=int(input("몇 도에요?"))
# if  30<=temp:
#     print("hot")
# elif 20<=temp and 30>temp:
#     print("nice")
# else:
#     print("cold")


#for문
# for waiting_no in [0,1,2,3,4]:
#     print("대기번호:{0}".format(waiting_no))  
# print("-----------------------------------")
# for waiting_no in range(1,6): #0,1,2,3,4
#     print("대기번호:{0}".format(waiting_no))

#while문
# customer="cha"
# index=5
# while index>=1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer,index))
#     index-=1
#     if index==0:
#         print("커피는 끝났어")

'''무한루프
custoemr="hyun"
index=1
while index>=1:
    print("{0}님 커피가 {1}회 남았습니다".format(customer,index))
    index+=1
'''

# customer="cha"
# person="unknown"
# while person!= customer:
#     print("{0},커피가 준비되었습니다".format(customer))
#     person=input("이름이 뭐임?")
#     if person=="cha":
#         print("커피 가져가세요")
#     elif person!="cha":
#         print("손님꺼 아닙니다")


#continue & break
# absent=[2,5]
# no_book=[7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("{0}때문에 수업 끝".format(student))
#         break
#     print("{0} 책 읽어봐".format(student))


# students=[1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]
# print(students)

# students=['cha','hyun','soo']
# students=[len(i) for i in students]
# print(students)

name=['cha','hyun','soo']
print([student.upper() for student in name])

