#파이썬 기초

# name='차현수'
# age=24
# print('내 이름은',name,'이고',age,'살 입니다')

# station='사당'
# print(station+'행 열차가 들어오고 있씁니다.')

# print(10//3)
# print(10/3)
# print(10%3)

# from random import *
# print(random()) #0.0~1.0 미만의 임의의 값을 생성
# print(random() *10) #0.0~10.0 미만의 임의의 값을 생성
# print(int(random() *10)) #소수점 제외
# print(int(random() *10)+1) #1~10이하의 임의의 값을 생성

# print(int(random()*45)+1) #1~45이하의 임의의 값을 생성

# print(randrange(1,45)) #1~45 미만의 임의의 값을 생성
# print(randrange(1,46)) #1~45 이하(46미만의)의 임의의 값을 생성
# print(randint(1,45))   #1~45 이하의 임의의 값을 생성

# sentence3="""
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# d="asdfasfasf"
# print(d[0:4])  #0부터 4직전까지
# print(d[:4])
# print(d[4:])
# print(d[-4:])

# python="Cha hoyUSN SOo"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(python.replace('Cha','ddd'))
# index=python.index('o')
# print(index)
# index=python.index('o',index+1)
# print(index)

# print(python.find('java'))
# '''print(python.index('java'))'''
# print('dd')
# print(python.count('o'))
# age=24
# print('나는 %s 살입니다' %age)
# print('나는 %s 을 좋아합니다' %'사과')
# print('나는 %s 을 좋아합니다' %"배")
# print('나는 %s와 %s 을 좋아합니다' %('배','사과'))

#print('나는 {}살 입니다'.format(20)) #{}안에 format함수를 이용해서
# print('나는 {0}색과 {2}색을 좋아해'.format('파란','빨강','노랑')) #{}안의 순번에 맞게
# print('나는 {color}살이며 {age}색을 좋아해'.format(age=24,color='파랑'))

#3.6버전 이상
# \' \" :문장 내에서 따옴표
# age=24
# color='파랑'
# print(f'나는 {age}살이며 \n{age}색을 좋아해')

# print("저는  \b차현수\\입니다")
# print("Red\tAPlle")


#리스트
# subway=[10,20,30]
# subway.append(10)
# print(subway)
# subway.insert(1,50)
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.count(10))

#정렬
# list=[10,40,30,20,100,2]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.clear()
# print(list)

# mlist=["차현수","20"]
# #print(mlist[0])
# list.extend(mlist)
# print(list)

# cabinet={3:"차","B-100":"현"}
# print(cabinet[3])
# print(cabinet[4])
# print(cabinet[5]) #key 5에 아무것도 없어서 오류남
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5,"토트넘"))
# print("asd")
# print(cabinet["B-100"])
# print(3 in cabinet)
# print("B-100" in cabinet)

# cabinet["C-20"]="첼시"
# print(cabinet)
# print("C-20" in cabinet)

# del cabinet["C-20"]
# cabinet["D-20"]="맨유"
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)
