# import theather_moudle #모듈  사용
# theather_moudle.price(3) #3명이서 영화 보러 갔을 때 가격
# theather_moudle.price_morning(4)
# theather_moudle.price_soldier(5)

# import theather_moudle as mv #theater_module.(모듈명)이 너무 기니까 별명을 붙혀서 사용, mv로만 호출 가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theather_moudle import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theather_moudle import price,price_morning
# price(5)
# price_morning(6)

# # from theather_moudle import price_soldier as ps
# # ps(5)

# import travel.thailand
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel import *
# # # trip_to=vietnam.VietnamPackage()
# # trip_to=thailand.ThailandPackage()
# # trip_to.detail()


# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#input(내장함수) :사용자 입력을 받는 함수
#dir :어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst=[1,2,3]
# print(dir(lst))

# name="jim"
# print(dir(name))

#glob :경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py인 모든 파일

#os :운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) #현재 디렉토리 표시

# folder="sample_dir"
# if os.path.exists(folder): #sample_dir이라는 폴더가 있으면 이 구문을 실행해라
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder,"폴더를 생성하였습니다.")

print(os.listdir())

#time: 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는",datetime.date.today())
# timedelta: 두 날짜 사이의 간격

today=datetime.date.today() #오늘 날짜르 저장
td=datetime.timedelta(days=100)
print("100일후:",today+td)