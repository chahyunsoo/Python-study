import pickle
# profile_file=open("profile.pickle","wb")
# profile={"이름":"차현수","나이":24,"취미":["축구","골프","코딩"]} 
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장하는 것
# profile_file.close()

# profile_file=open("profile.pickle","rb")
# profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


#with
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))



#파일 쓰기
with open("study.text","w",encoding="utf-8") as study_file:
    study_file.write("파이썬")

#파일 일기
with open("study.text","r",encoding="utf-8") as study_file:
    print(study_file.read())

