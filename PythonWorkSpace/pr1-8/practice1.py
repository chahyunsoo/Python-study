#튜플--->list와는 다르게 내용 변경이나 추가를  할 수 없다, but 속도가 list보다 빠르다
# team=("토트넘","아스날")
# print(team[0])
# print(team[1])
#team.add("첼시") 이렇게 추가 안됨

# name="차현수"
# age=24
# hobby="코딩"

# (name,age,hobby)=("차현수",24,"코딩")
# print(name,age,hobby)





# 집합(set)-->중복 안됨, 순서 없음
my_set={1,2,3,4,4}
print(my_set)
java={"케인","손흥민","로얄"}
python={"존","알파","로얄"}
# 교집합
print(java & python)
print(java.intersection(python))
# 합집합
print(java | python)
print(java.union(python))
# 차집합
print(java-python)
print(java.difference(python))
#추가
python.add("해리")
print(python)
#제거
python.remove("존")
print(python)
print(python)
