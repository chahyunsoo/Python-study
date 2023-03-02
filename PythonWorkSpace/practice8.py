# scr={"수학":0,"영어":10,"과학":20}
# for subject, score in scr.items():
#     print(subject.ljust(8),str(score).rjust(4),sep=":")

#결과값
# 수학      :   0
# 영어      :  10
# 과학      :  20

#대기순번표처럼 1,2,3이 아니라 001,002,003처럼 출력하고 싶을때
#zfill()을 이용한다
#zfill() 는 문자열 타입 메서드입니다.
# for num in range(1,21):
#     print("대기번호:",str(num).zfill(3))


#answer=input("입력:")
#########사용자의 입력에 의해 값을 받게 되면 항상 문자열 형태로 저장이 된다
# answer=10
# print(type(answer))
#print(str(answer))


#출력 포맷
#빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리의 공간을 확보
##print("{0: >+10}".format(500))
#양수일 땐 +로 표시,음수일 땐 -로 표시
##print("{0: >+10}".format(-500))
#10자리 만큼 확보를 하고 왼쪽 정렬하고 빈칸으로 _채움
##print("{0:_<+10}".format(-500))
#3자리마다 콤마 찍어주기
##print("{0:,}".format(1000000000))
#3자리마다 콤마 찍어주기, +-부호 찍어주기
##print("{0:+,}".format(1000000000))
##print("{0:+,}".format(-1000000000))
#3자리마다 콤마 찍어주고, 부호도 붙이고, 자릿수도 확보
#빈 자리는 ^로 채워주기
##print("{0:^<+30,}".format(1000000000))
#소수점 출력
##print("{0:f}".format(5/3))
#소수점 특정자리까지만 출력 (소수점 4째 자리에서 반올림)
##print("{0:.3f}".format(5/3))


#파일 입출력
# score_file=open("score.txt","w",encoding="utf-8")
# print("수학:0",file=score_file)
# print("영어:40",file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf-8")
# score_file.write("과학:80")
# score_file.write("\n코딩:100")
# score_file.close()

# # score_file=open("score.txt","r",encoding="utf-8")
# # print(score_file.read()) #줄별로 일기, 한 줄 읽고 커서는 다음 줄로 이동
# # score_file.close()
# score_file=open("score.txt","r",encoding="utf-8")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

#몇 줄인지 모를때 처리하는 방법
# score_file=open("score.txt","r",encoding="utf-8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

score_file=open("score.txt","r",encoding="utf-8")
lines=score_file.readlines() #list형태로 저장
for line in lines:
    print(line,end="")
    
score_file.close()